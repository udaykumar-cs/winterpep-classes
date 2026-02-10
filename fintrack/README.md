# FINTRACK PRO – CLI Finance Manager

FinTrack Pro is a command-line based personal finance management system built using **Python, SQLite, and SQLAlchemy ORM**.  
It helps users track expenses, manage budgets, and analyze spending patterns.

This project is ideal for **learning ORM concepts, CRUD operations, and SQL analytics**, and is suitable for **interviews and portfolios**.

---

## 🚀 Features

- Add and manage expense categories  
- Add, update, and delete expenses  
- Search expenses by date  
- Category-wise expense reports  
- Set monthly budgets  
- Budget limit alerts  
- SQLite database persistence  
- Interactive CLI menu  

---

## 🛠️ Technologies Used

- Python  
- SQLite  
- SQLAlchemy (ORM)  
- Raw SQL  
- Command Line Interface (CLI)  

---

## 🗄️ Database Schema

### Categories
| Column | Type |
|------|------|
| id | Integer (Primary Key) |
| name | String (Unique) |

### Expenses
| Column | Type |
|------|------|
| id | Integer (Primary Key) |
| title | String |
| amount | Integer |
| date | String (YYYY-MM-DD) |
| category_id | Integer (Foreign Key) |

### Subscriptions
| Column | Type |
|------|------|
| id | Integer (Primary Key) |
| name | String |
| amount | Integer |
| date | String |

### Budgets
| Column | Type |
|------|------|
| id | Integer (Primary Key) |
| month | String (YYYY-MM) |
| limit | Integer |

---

## 🔗 Relationships

- One **Category** → Many **Expenses**
- Each **Expense** belongs to one **Category**

---

## 📂 Project Structure

FINTRACK_PRO/
│
├── main.py
├── fintrack.db
├── README.md



---

## ▶️ How to Run the Project

### 1️⃣ Install dependency
```bash
pip install sqlalchemy

2️⃣ Run the application
python main.py


Sample CLI Menu

===== FINTRACK PRO =====
1. Add Category
2. Add Expense
3. Update Expense
4. Delete Expense
5. Search Expense by Date
6. Category Report
7. Set Monthly Budget
8. Budget Alert
9. Exit

Choose:
