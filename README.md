# Ecommerce Backend (Django + DRF + PostgreSQL)

This project is a production-ready backend API for an ecommerce system.  
It includes user accounts, product management, cart handling, and order processing.

The application is built using:

- Django 5+
- Django REST Framework
- PostgreSQL
- JWT Authentication (SimpleJWT)
- CORS Headers
- Deployment on Vercel (via serverless functions)

---

## 🚀 Features

### Accounts
- User registration
- Login with JWT
- Protected endpoints
- Token refresh

### Products
- Create, update, delete products
- Public product listing endpoint

### Cart
- Add/remove/update cart items
- Retrieve cart for authenticated users

### Orders
- Checkout
- Order creation & order history

---

## 🛠 Tech Stack

| Component | Technology |
|----------|------------|
| Backend | Django + DRF |
| Database | PostgreSQL |
| Deployment | Vercel |
| Auth | SimpleJWT |
| API Testing | Postman / Thunder Client |

---

## 📦 Local Setup

### 1. Clone the project
```bash
git clone https://github.com/<your-username>/ecommerce_backend.git
cd ecommerce_backend
