Slide 1 — Title

Ecommerce Backend API
Tech Stack: Django + DRF + PostgreSQL + Vercel
Developer: [Your Name]

Slide 2 — Problem Statement

Challenges for Online Shops:

Secure user accounts

Product catalog management

Shopping cart functionality

Order processing & history

Scalable backend architecture

Solution: This project addresses all backend challenges with a modular, secure, and cloud-deployable API.

Slide 3 — System Architecture

Backend: Django REST Framework (DRF)

Database: PostgreSQL

Authentication: JWT with HTTP-only cookies

Deployment: Vercel serverless hosting

Modular Apps:

accounts_app – user registration, login, roles

products_app – product CRUD operations

cart_app – cart management

orders_app – order processing

Slide 4 — Features

User Management:

Registration, login

JWT authentication

Role-based access (admin & user)

Product Management: Create, update, delete, list products

Cart Management: Add/remove/update cart items

Order Management: Checkout, order history

Security: HTTP-only cookie tokens

Slide 5 — ERD Overview

Core relationships:

User ↔ Orders (1-to-many)

Order ↔ OrderItems (1-to-many)

User ↔ CartItems (1-to-many)

Product ↔ CartItems / OrderItems (1-to-many)

Full ERD diagram available in ERD_DESIGN.md

Slide 6 — Testing Strategy

Tools: Postman / Thunder Client

Validate all CRUD operations

Test authentication flows

Test cart and order workflows end-to-end

Slide 7 — Deployment Workflow

Hosting: Vercel (serverless)

Database: PostgreSQL (cloud-hosted)

Environment Management: .env for secret keys & credentials

CI/CD: Auto-deploy via Git push

Slide 8 — Demo

Live demo highlights:

User registration & login

Product listing

Add products to cart

Create an order

Token refresh & logout

Slide 9 — Conclusion

Fully functional ecommerce backend API

Secure authentication & role-based access

Modular & scalable architecture

Cloud deployment via Vercel

Ready for production

Thank you!