# FINTRACK PROJECT - CLI FINANCE MANAGER

# SQLAlchemy is used to connect Python with Database.

from sqlalchemy import create_engine,Column,Integer,String,ForeignKey,text
from sqlalchemy.orm import declarative_base,sessionmaker,relationship


# ----------------------DATABASE SETUP------------------------

engine = create_engine("sqlite:///fintrack.db")
Base = declarative_base()
Session = sessionmaker(bind = engine)
session = Session()


# -------------------- TABLE MODELS -------------------------------

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer,primary_key=True)
    name = Column(String,unique=True)
    expenses = relationship("Expense",back_populates="category")

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer,primary_key=True)
    title = Column(String)
    amount = Column(Integer)
    date = Column(String)

    category_id=Column(Integer,ForeignKey("categories.id"))

    category = relationship("Category",back_populates="expenses")


class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer,primary_key=True)
    name = Column(String)
    amount = Column(Integer)
    date = Column(String)

class Budget(Base):
    __tablename__ = "budgets"

    id = Column(Integer,primary_key=True)
    month = Column(String,unique=True)

    limit = Column(Integer)

Base.metadata.create_all(engine)


# CLI Functions

# Category 

def add_category():
    name=input("Category name: ")
    session.add(Category(name=name))
    session.commit()
    print("Category added successfully!!")



# Add EXPENSE

def add_expense():
    title = input("Expense title: ")
    amount = int(input("Amount: "))
    date = input("Date (YYYY-MM-DD): ")

    category_id = int(input("Category Id: "))

    session.add(
        Expense(title=title,
                amount=amount,
                date=date,
                category_id=category_id
            )
        )
    session.commit()
    print("Expense is added: ")

#

def update_expense():
    eid = int(input("Expense Id: "))

    expense = session.query(Expense).filter(Expense.id==eid).first()

    if expense:
        expense.amount = int(input("New amount: "))
        session.commit()
        print("Expense updated")
    else:
        print("Expense not found!")


#

def delete_expense():
    eid = int(input("Expense Id: "))

    expense = session.query(Expense).filter(Expense.id == eid).first()

    if expense:
        session.delete(expense)
        session.commit()
        print("Expense deleted: ")
    
    else:
        print("Expense not found: ")


# SEARCH BY DATE

def search_by_date():
    date = input("Enter date (YYYY-MM-DD): ")
    expenses = session.query(Expense).filter(Expense.date==date).all()

    for e in expenses:
        print(e.title,"-",e.amount,"-",e.category.name)


# CATEGORY WISE SPENDING

def category_report():
    sql = """ SELECT c.name, SUM(e.amount)
    FROM categories c
    JOIN expenses e ON c.id = e.category_id
    GROUP BY c.name """

    result = session.execute(text(sql))

    print("\n Category wise expense report: ")

    for row in result:
        print(row[0],"->",row[1])

# Set Monthly budgets

def set_budget():
    month = input("Enter Month (YYYY-MM): ")
    limit = int(input("Enter your monthly limit: "))

    session.add(Budget(month=month,limit=limit))
    session.commit()

    print("Budget saved succcessfully!!")

# Budget Alert

def budget_alert():
    month=input("Enter month (YYYY-MM): ")

    total = session.execute(
        text("SELECT SUM(amount) FROM expenses WHERE date LIKE :m"),
        {"m": f"{month}%"}
    ).scalar() or 0

    budget = session.query(Budget).filter(Budget.month == month).first()

    if budget and total > budget.limit:
        print("Budget exceeded:", total, "/", budget.limit)
    else:
        print("Within budget:", total)



# CLI MENUE


while True:
    print("""
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
""")

    ch = input("Choose: ")

    if ch == "1":
        add_category()
    elif ch == "2":
        add_expense()
    elif ch == "3":
        update_expense()
    elif ch == "4":
        delete_expense()
    elif ch == "5":
        search_by_date()
    elif ch == "6":
        category_report()
    elif ch == "7":
        set_budget()
    elif ch == "8":
        budget_alert()
    elif ch == "9":
        break
    else:
        print("Invalid choice")
