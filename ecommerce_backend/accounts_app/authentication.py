# authentication_app/authentication.py
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed, InvalidToken, TokenError
import logging

logger = logging.getLogger(__name__)

class CookieJWTAuthentication(JWTAuthentication):
    """
    Custom JWT authentication that reads tokens from HTTP-only cookies
    instead of Authorization headers.
    """
    
    def authenticate(self, request):
        """
        Authenticate user using JWT token from cookies.
        Returns None if no token or invalid token (allowing AllowAny views to work).
        """
        token = request.COOKIES.get("access_token")
        
        if not token:
            return None
            
        try:
            validated_token = self.get_validated_token(token)
            user = self.get_user(validated_token)
            return user, validated_token
        except (InvalidToken, TokenError, AuthenticationFailed) as e:
            # Log for debugging but don't raise - allows AllowAny views to work
            logger.debug(f"Cookie JWT authentication failed: {str(e)}")
            return None