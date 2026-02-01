
# Create a Library Management System where different library items calculate borrowing charges differently.
# Library item (parent class)
# Book and magazie (child class)
# LibraryApp(main class)

# Book IS-A libraryitem
# Magazine IS-A libraryitem
# LibraryApp HAS-A libraryitem

# Output format
# Item Type: Book
# Borrow Days: 5
# Borrowing Charge: 50
# Or 
# Item Type: Magazine
# Borrow Days: 3
# Borrowing Charge: 30


from abc import ABC, abstractmethod

# This class define rule for or structure for all
# Library item (book, magazine, etc.)

class LibraryItem(ABC):
    def __init__(self,item_type,borrow_days):

        # item_type store whethere the item is Book or Magazine
        self.item_type=item_type

        # borrow_days store the number of days item is borrowed.
        self.borrow_days=borrow_days


# ABSTRACT CLASS 

# Child classes MUST implement this method

@abstractmethod
def calculate_charge(self):
    pass

# CHILD CLASS BOOK
# Book IS-A LibraryItem

class Book(LibraryItem):

    def __init__(self,borrow_days):

        # calling parent method using super()
        super().__init__("Book",borrow_days)

        # Protected variable (Encapsulation)
        # rate per day for Book borrowing 

        self._rate_per_day = 10

    # method overriding (Polymorphism)
    # Book has its own way to calculate chargese

    def calculate_charge(self):
        return self.borrow_days*self._rate_per_day
    

# CHILD CLASS MAGAZINE
# Magazine IS-A LibraryItem

class Magazine(LibraryItem):
    def __init__(self,borrow_days):

        # calling parent method using super()
        super().__init__("Magazine",borrow_days)


        # protected variable (Encapsulation)
        # rate per for Magazine borrowing
        self._rate_per_day=12

    # method overriding (Polymorphis)
    # Magazine has its own way to calculate charges

    def calculate_charge(self):
        return self.borrow_days*self._rate_per_day

# CONTROLER CLASS
# LibraryApp HAS-A LibraryItem

class LibraryApp:
    def __init__(self):

        # This variable will hold Book or Magazine object
        self.item=None

    # Method to create library item object
    def creat_item(self,item_type,borrow_days):

        # Decide which object create

        if item_type =="Book":
            self.item = Book(borrow_days)

        elif item_type =="Magazine":
            self.item=Magazine(borrow_days)
        else:
            print("Invalid item type")

    # method to display final bill

    def show_bill(self):
        print("Item Type:",self.item.item_type)
        print("Borrow days:",self.item.borrow_days)
        print("Borrowing charge:",self.item.calculate_charge())

# Main Program (console output)

# Object of LibraryApp
app = LibraryApp()

# create book object
app.creat_item("Book",7)

# Display Borrow bill
app.show_bill()
print()

# Create another LibraryApp object
app1 = LibraryApp()

# Create Magazine object
app1.creat_item("Magazine",7)

# Display Borrow bill
app1.show_bill()









    