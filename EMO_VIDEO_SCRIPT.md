# 🎬 Demo Video Script — Ecommerce Backend

This script guides the presenter through a smooth, professional backend demonstration.

---

## 1. Introduction (10 seconds)
“Hello, this is a demo of my Ecommerce Backend API built with Django, Django REST Framework, PostgreSQL, and deployed on Vercel.”

---

## 2. User Registration (20 seconds)
- Open Postman.
- Show request to `/api/auth/register/`.
- Submit with username, email, password.
- Show success response.

Narration:  
“This endpoint allows new users to register securely.”

---

## 3. Login and Token Retrieval (20 seconds)
- Send POST request to `/api/auth/login/`.
- Display access + refresh tokens.

Narration:  
“These tokens are used to authenticate future requests.”

---

## 4. Product Listing (20 seconds)
- GET `/api/products/`.
- Show sample products.

Narration:  
“The products endpoint supports listing and detailed views.”

---

## 5. Add Product (Admin Only) (20 seconds)
- Use admin token.
- POST `/api/products/create/`.

Narration:  
“Admins can add, update, or delete products.”

---

## 6. Add to Cart (20 seconds)
- POST `/api/cart/add/`.

Narration:  
“Authenticated users can add products to their cart.”

---

## 7. View Cart (15 seconds)
- GET `/api/cart/`.

Narration:  
“This returns all cart items for the logged-in user.”

---

## 8. Checkout (20 seconds)
- POST `/api/orders/create/`.
- Show success message.

Narration:  
“This endpoint creates an order from the items in the cart.”

---

## 9. View Order History (15 seconds)
- GET `/api/orders/`.

Narration:  
“Users can view all their previous orders.”

---

## 10. Conclusion (10 seconds)
“Thank you for watching. This backend is fully functional, scalable, and ready for production.”

