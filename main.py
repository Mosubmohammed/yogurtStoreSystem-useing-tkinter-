from stringcolor import * 
import tkinter as tk
from tkinter import messagebox
itemsList = [
    {'name': 'LABNEH', 'price': 2.99},
    {'name': 'MILK', 'price': 1.50},
    {'name': 'SOUR CREAM', 'price': 2.00},
    {'name': 'EGGS', 'price': 0.50},
    {'name': 'GREEN OLIVES', 'price': 2.85},
    {'name': 'OLIVES OLI', 'price': 6.50},
    {'name': 'MAKDOOS WITH WALNUTS', 'price': 1.90},
    {'name': 'MORTADELLA', 'price': 4.20},
    {'name': 'YOGURT', 'price': 1.50},
    {'name': 'BUTTER', 'price': 2.50},
    {'name': 'MOZZARELLA CHEESE', 'price': 6.00},
    {'name': 'MWHITE CHEESE', 'price': 4.75},
    {'name': 'JAMEED KARAKI', 'price': 3.15},
    {'name': 'SHANINA', 'price': 0.80},
]


class Customer:
    def __init__(self, name, age, phone, address, email, password):
        self.name = name
        self.age = age
        self.phone = phone
        self.address = address
        self.email = email
        self.__password = password

    def getCustomerPass(self):
        return self.__password

class CustomersAcc:
    def __init__(self):
        self.customersList = []

    def addCustomer(self, customer):
        self.customersList.append(customer)

class LoginAccount(Customer):
    def __init__(self, email, password):
        super().__init__("", "", "", "", email, password)

    def searchForCustomers(self, customers_acc):
        for customer in customers_acc.customersList:
            if self.email == customer.email and self.getCustomerPass() == customer.getCustomerPass():
                messagebox.showinfo('Welcome', 'Welcome back!')
                return
        messagebox.showerror('Error', 'You don\'t have an account.')

def login_window(customers_acc):
    window = tk.Tk()
    window.title('Login')
    
    label_email = tk.Label(window, text='Email:')
    entry_email = tk.Entry(window)

    label_password = tk.Label(window, text='Password:')
    entry_password = tk.Entry(window, show='*')  

    def login():
        email = entry_email.get()
        password = entry_password.get()
        login_account = LoginAccount(email, password)
        login_account.searchForCustomers(customers_acc)
        window.destroy()

    button_login = tk.Button(window, text='Login', command=login)
    window.geometry("300x200+70+60")

    label_email.pack()
    entry_email.pack()
    label_password.pack()
    entry_password.pack()
    button_login.pack()

    window.mainloop()


class ItemsForm:
    def __init__(self, items_list):
        self.items_list = items_list
        self.window = tk.Tk()
        self.window.title('Items List')

        self.label_title = tk.Label(self.window, text='Items List', font=('Helvetica', 16, 'bold'))
        self.label_title.pack()

        for item in self.items_list:
            formatted_item_name = f"{item['name']}"
            formatted_item_price = f"${item['price']:.2f}"

            label_item_name = tk.Label(self.window, text=formatted_item_name, fg='blue')
            label_item_price = tk.Label(self.window, text=formatted_item_price, fg='green')

            label_item_name.pack()
            label_item_price.pack()

        self.button_close = tk.Button(self.window, text='Close', command=self.window.destroy)
        self.button_close.pack()

    def show(self):
        self.window.mainloop()

class ItemSearch:
    def __init__(self, items_list):
        self.items_list = items_list

    def search_item(self, search):
        for item in self.items_list:
            if search.lower() == item['name'].lower():
                return item
        return None

        
def search_window(items_list):
    window = tk.Tk()
    window.title('Search for Items')

    label_search = tk.Label(window, text='Enter the name of the item you want to search:')
    entry_search = tk.Entry(window)

    result_var = tk.StringVar()

    def search():
        search_query = entry_search.get()
        item_search = ItemSearch(items_list)
        result = item_search.search_item(search_query)
        if result:
            result_var.set(f"Item found:\nName: {result['name']}\nPrice: {result['price']}")
        else:
            result_var.set('Item not found')

    button_search = tk.Button(window, text='Search', command=search)
    label_result = tk.Label(window, textvariable=result_var)

    label_search.pack()
    entry_search.pack()
    button_search.pack()
    label_result.pack()
    window.mainloop()



class CreateAccountForm:
    def __init__(self, customers_acc):
        self.customers_acc = customers_acc
        self.window = tk.Tk()
        self.window.title('Create New Account')

        label_name = tk.Label(self.window, text='Name:')
        entry_name = tk.Entry(self.window)

        label_age = tk.Label(self.window, text='Age:')
        entry_age = tk.Entry(self.window)

        label_phone = tk.Label(self.window, text='Phone:')
        entry_phone = tk.Entry(self.window)

        label_address = tk.Label(self.window, text='Address:')
        entry_address = tk.Entry(self.window)

        label_email = tk.Label(self.window, text='Email:')
        entry_email = tk.Entry(self.window)

        label_password = tk.Label(self.window, text='Password:')
        entry_password = tk.Entry(self.window, show='*')

        def create_account():
            name = entry_name.get()
            age = entry_age.get()
            phone = entry_phone.get()
            address = entry_address.get()
            email = entry_email.get()
            password = entry_password.get()

            customer = Customer(name, age, phone, address, email, password)
            self.customers_acc.addCustomer(customer)
            messagebox.showinfo('Success', 'Account created successfully!')
            self.window.destroy()

        button_create_account = tk.Button(self.window, text='Create Account', command=create_account)

        label_name.pack()
        entry_name.pack()
        label_age.pack()
        entry_age.pack()
        label_phone.pack()
        entry_phone.pack()
        label_address.pack()
        entry_address.pack()
        label_email.pack()
        entry_email.pack()
        label_password.pack()
        entry_password.pack()
        button_create_account.pack()

        self.window.geometry("300x300+70+60")
        self.window.mainloop()

print(cs('welcome to our yogurt store', "blue")) 
customers_acc = CustomersAcc()

class cart:
    def __init__(self,items):
        self.items = items
orderList = []
while True:
    print('1-CREATE NEW ACCOUNT')
    print('2-LOGIN to ur account')
    print('3-SEARCH FOR ITEMS')
    print('4-VIEW THE ITEMS')
    print('5-ORDER')
    print('6-VIEW THE ORDERS')
    choice = input(cs('PLEASE ENTER YOUR CHOICE :','red'))

    if choice == '1':
        create_account_form = CreateAccountForm(customers_acc)
        print(cs('Thanks for joining our business', 'red'))
        
    elif choice == '2':
        login_window(customers_acc)

    if choice == '3':
         search_window(itemsList)

    elif choice == '4':
        items_form = ItemsForm(itemsList)
        items_form.show()
    elif choice == '5':
        items_form = ItemsForm(itemsList)
        items_form.show()
        order1 = input(cs('Enter the name of the item: ', 'red')).upper()  
        item_found = False
        for item in itemsList:
            if order1 == item['name'].upper():
                orderList.append(item)
                item_found = True
                break  
        if item_found:
            print(cs(f"{order1} added to the order.", 'green'))
        else:
            print(cs(f"Item {order1} not found.", 'red'))  
    elif choice == '6':
         print(orderList)
    # else:
    #     print('Invalid choice. Please enter a valid option.')
    #     continue
