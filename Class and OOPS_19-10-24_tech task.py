class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Salary: {self.salary}")
class Manager(Employee):
    def __init__(self, name, salary, department):
       
        super().__init__(name, salary)
        self.department = department
    def display_details(self):
        super().display_details()
        print(f"Department: {self.department}")
employee = Employee("Alice", 50000)
employee.display_details()
print()
manager = Manager("Bob", 75000, "HR")
##2##
class LibraryItem:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication Year: {self.publication_year}")
class Book(LibraryItem):
    def __init__(self, title, author, publication_year, genre):
        super().__init__(title, author, publication_year)
        self.genre = genre
    def display_info(self):
        super().display_info()
        print(f"Genre: {self.genre}")
library_item = LibraryItem("In Search of Lost Time", "Marcel Proust", 1913)
print("Library Item Details:")
library_item.display_info()
print("")
book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Novel")
print("Book Details:")
book.display_info()
##3##
class BankAccount:
    def __init__(self, owner_name, balance=0):
        self.owner_name = owner_name
        self.balance = balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance is {self.balance}.")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            print("Withdrawal amount must be positive.")

 
    def check_balance(self):
        print(f"Current balance: {self.balance}")
account = BankAccount("John Doe", 1000)
T=True
while T:
    print("1.Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    ch=int(input("Enter your choice(1-4)"))
    if ch==1:
        account.check_balance()
        T=True
    elif ch==2:
        mon_dep=int(input("Enter money value to bo deposited"))
        account.deposit(mon_dep)      
        account.check_balance()
        T=True
    elif ch==3:
        mon_wit=int(input("Enter money value to bo withdrawn"))
        if mon_wit>account.check_balance():
            account.withdraw(mon_wit)
            account.check_balance()
            T=True
    else:
        T=False
        quit()






















manager.display_details()
