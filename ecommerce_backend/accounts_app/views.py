from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.request import Request
from .serializers import CustomUserSerializer, RegisterUserSerializer, LoginUserSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
import os
import logging

from django.conf import settings  # Added this import to fix the error

logger = logging.getLogger(__name__)

COOKIE_SECURE = False
COOKIE_SAMESITE = "Lax"

# Cookie settings
COOKIE_SETTINGS = {
    'httponly': True,
    'secure': COOKIE_SECURE,
    'samesite': COOKIE_SAMESITE,
    'max_age': None  # Session cookies
}

def set_auth_cookies(response, refresh_token, access_token):
    """Helper function to set authentication cookies consistently"""
    response.set_cookie(
        key="access_token",
        value=access_token,
        **COOKIE_SETTINGS
    )
    
    response.set_cookie(
        key="refresh_token", 
        value=refresh_token,
        **COOKIE_SETTINGS
    )

def clear_auth_cookies(response):
    """Helper function to clear authentication cookies"""
    response.delete_cookie("access_token", samesite=COOKIE_SAMESITE)
    response.delete_cookie("refresh_token", samesite=COOKIE_SAMESITE)

class UserInfoView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomUserSerializer

    def get_object(self):
        return self.request.user

class UserRegistrationView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        # Generate tokens
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        response = Response({
            "user": CustomUserSerializer(user).data,
            "message": "Registration successful"
        }, status=status.HTTP_201_CREATED)

        # Set authentication cookies
        set_auth_cookies(response, str(refresh), access_token)
        
        logger.info(f"User {user.email} registered successfully")
        return response

class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = LoginUserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data
            
            # Generate new tokens
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            response = Response({
                "user": CustomUserSerializer(user).data,
                "message": "Login successful"
            }, status=status.HTTP_200_OK)

            # Set authentication cookies
            set_auth_cookies(response, str(refresh), access_token)
            
            logger.info(f"User {user.email} logged in successfully")
            return response

        logger.warning(f"Failed login attempt for data: {request.data}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        refresh_token = request.COOKIES.get("refresh_token")
        
        response = Response({"message": "Successfully logged out!"}, status=status.HTTP_200_OK)
        
        # Clear cookies first
        clear_auth_cookies(response)

        # Try to blacklist the refresh token if it exists
        if refresh_token:
            try:
                refresh = RefreshToken(refresh_token)
                refresh.blacklist()
                logger.info(f"Refresh token blacklisted for user {request.user.email}")
            except TokenError as e:
                # Token might already be blacklisted or invalid
                logger.warning(f"Could not blacklist token: {str(e)}")
            except Exception as e:
                logger.error(f"Unexpected error during token blacklisting: {str(e)}")

        return response

class CookieTokenRefreshView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        refresh_token = request.COOKIES.get("refresh_token")

        if not refresh_token:
            return Response({
                "error": "Refresh token not provided",
                "code": "REFRESH_TOKEN_MISSING"
            }, status=status.HTTP_401_UNAUTHORIZED)

        try:
            refresh = RefreshToken(refresh_token)
            if hasattr(refresh, 'check_blacklist'):
                refresh.check_blacklist()
            
            access_token = str(refresh.access_token)
            new_refresh_token = str(refresh)
            
            if getattr(settings, 'SIMPLE_JWT', {}).get('ROTATE_REFRESH_TOKENS', False):
                user = refresh.get('user_id')
                if user:
                    from django.contrib.auth import get_user_model
                    User = get_user_model()
                    try:
                        user_obj = User.objects.get(id=user)
                        new_refresh = RefreshToken.for_user(user_obj)
                        new_refresh_token = str(new_refresh)
                        access_token = str(new_refresh.access_token)
                        refresh.blacklist()
                    except User.DoesNotExist:
                        return Response({
                            "error": "User not found",
                            "code": "USER_NOT_FOUND"
                        }, status=status.HTTP_401_UNAUTHORIZED)

            response = Response({
                "message": "Access token refreshed successfully"
            }, status=status.HTTP_200_OK)

            set_auth_cookies(response, new_refresh_token, access_token)
            logger.info("Token refreshed successfully")
            return response
            
        except TokenError as e:
            logger.warning(f"Token refresh failed - TokenError: {str(e)}")
            response = Response({
                "error": "Session expired, please log in again",
                "code": "INVALID_REFRESH_TOKEN"
            }, status=status.HTTP_401_UNAUTHORIZED)
            clear_auth_cookies(response)
            return response
            
        except Exception as e:
            logger.error(f"Unexpected error during token refresh: {str(e)}")
            response = Response({
                "error": "Token refresh failed",
                "code": "REFRESH_FAILED"
            }, status=status.HTTP_401_UNAUTHORIZED)
            clear_auth_cookies(response)
            return response