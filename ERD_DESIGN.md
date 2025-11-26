
---

# ✅ **5. ERD_DESIGN.md**

```markdown
# 📊 Entity Relationship Diagram (ERD)

Below is the conceptual data model for the ecommerce backend.

---

## 🧑 Users
| Field | Type | Notes |
|-------|------|-------|
| id | UUID / Auto | Primary Key |
| username | String | Unique |
| email | String | Unique |
| password | Hashed | — |

---

## 🛒 Products
| Field | Type | Notes |
|-------|------|-------|
| id | Auto | Primary Key |
| name | String | Required |
| description | Text | — |
| price | Decimal | Required |
| stock | Integer | Required |
| created_at | DateTime | — |

---

## 🧺 CartItem
| Field | Type | Relation |
|-------|------|----------|
| id | Auto | PK |
| user | FK → User | One user has many cart items |
| product | FK → Product | A product can be in many carts |
| quantity | Integer | — |

---

## 📦 Orders
| Field | Type | Relation |
|-------|------|----------|
| id | Auto | PK |
| user | FK → User | One user can place many orders |
| total_amount | Decimal | — |
| created_at | DateTime | — |

---

## 📦 OrderItems
| Field | Type | Relation |
|-------|------|----------|
| id | Auto | PK |
| order | FK → Order | One order has many items |
| product | FK → Product | — |
| quantity | Integer | — |
| price | Decimal | Price at checkout |

---

# 📐 Relationships Summary

- **User 1 → M Orders**
- **User 1 → M CartItems**
- **Order 1 → M OrderItems**
- **Product 1 → M CartItems**
- **Product 1 → M OrderItems**

This ERD supports ecommerce workflows reliably and efficiently.


Tips
Entities (Models) and Key Attributes
1. CustomUser (accounts_app)

Attributes:

id (PK)

email (unique)

first_name

last_name

phone_number

role (user/admin)

is_superuser

is_staff

is_active

password

Relationships:

One-to-many with Order (a user can have multiple orders)

One-to-one with Cart (a user has one cart)

2. Product (products_app)

Attributes:

id (PK)

name

description

price

stock

image_url (optional)

created_at

updated_at

Relationships:

One-to-many with OrderItem (a product can appear in many order items)

One-to-many with CartItem (a product can appear in many cart items)

3. Cart (cart_app)

Attributes:

id (PK)

user_id (FK to CustomUser)

created_at

updated_at

Relationships:

One-to-one with CustomUser (each user has one cart)

One-to-many with CartItem (a cart can have multiple items)

4. CartItem (cart_app)

Attributes:

id (PK)

cart_id (FK to Cart)

product_id (FK to Product)

quantity

added_at

Relationships:

Many-to-one with Cart

Many-to-one with Product

5. Order (orders_app)

Attributes:

id (PK)

user_id (FK to CustomUser)

total_amount

status (pending, completed, canceled)

created_at

updated_at

Relationships:

One-to-many with OrderItem

Many-to-one with CustomUser (a user can have many orders)

6. OrderItem (orders_app)

Attributes:

id (PK)

order_id (FK to Order)

product_id (FK to Product)

quantity

price (price at time of order)

Relationships:

Many-to-one with Order

Many-to-one with Product

Relationships Overview
Relationship	Type	Description
CustomUser → Cart	One-to-One	Each user has exactly one cart
CustomUser → Order	One-to-Many	A user can place multiple orders
Cart → CartItem	One-to-Many	A cart contains multiple cart items
Product → CartItem	One-to-Many	A product can be in multiple cart items
Order → OrderItem	One-to-Many	An order can contain multiple products (order items)
Product → OrderItem	One-to-Many	A product can appear in multiple order items
Visual ERD (Text Version)
CustomUser (1) ── (1) Cart
CustomUser (1) ── (M) Order
Cart (1) ── (M) CartItem ── (1) Product
Order (1) ── (M) OrderItem ── (1) Product


(1) = one

(M) = many

Tips for Mapping to a Diagram Tool

Start with CustomUser in the center.

Draw a one-to-one line to Cart.

Draw a one-to-many line to Order.

From Cart, draw one-to-many to CartItem → connects to Product.

From Order, draw one-to-many to OrderItem → connects to Product.

Add attributes inside each entity box (PKs at the top, FKs, other fields below).

If you want, I can draw a clean ASCII-style ERD that you can directly paste into documentation, or I can give a diagram-ready dbdiagram.io script for easy visualization.

Do you want me to do that next?