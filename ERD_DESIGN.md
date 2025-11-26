
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
