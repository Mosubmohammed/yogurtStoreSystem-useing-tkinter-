import tkinter as tk
from tkinter import ttk
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

class CustomersAcc:
    def __init__(self):
        self.customersList = []

    def addCustomer(self, customer):
        self.customersList.append(customer)
    def getCustomerPass(self):
        return self.__password

class LoginAccount(Customer):
    def __init__(self, email, password):
        super().__init__("", "", "", "", email, password)

    def searchForCustomers(self, customers_acc, callback):
        for customer in customers_acc.customersList:
            if self.email == customer.email and self._Customer__password == customer._Customer__password:
                messagebox.showinfo('Welcome', 'Welcome back!')
                callback()  # Call the callback function after showing the messagebox
                return
        messagebox.showerror('Error', 'You don\'t have an account.')

class ItemSearch:
    def __init__(self, items_list):
        self.items_list = items_list

    def search_item(self, search_query):
        for item in self.items_list:
            if item['name'].lower() == search_query.lower():
                return item
        return None
class ItemsForm:
    def __init__(self, items_list):
        self.items_list = items_list
        self.window = tk.Tk()  # Create a new Tkinter window
        self.window.title('Items List')

        self.label_title = ttk.Label(self.window, text='Items List', font=('Helvetica', 16, 'bold'))
        self.label_title.pack()

        for item in self.items_list:
            formatted_item_name = f"{item['name']}"
            formatted_item_price = f"${item['price']:.2f}"

            label_item_name = ttk.Label(self.window, text=formatted_item_name, foreground='blue')
            label_item_price = ttk.Label(self.window, text=formatted_item_price, foreground='green')

            label_item_name.pack()
            label_item_price.pack()

        self.button_close = ttk.Button(self.window, text='Close', command=self.window.destroy)
        self.button_close.pack()

    def show(self):
        self.window.mainloop()

LARGEFONT =("Verdana", 12)



class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs): 
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self) 
        container.pack(side="top", fill="both", expand=True) 

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        customers_acc = CustomersAcc()  # Create an instance of CustomersAcc

        for F in (StartPage, Page1, Page2, Page3, Page4, Page5):
            frame = F(container, self, customers_acc)  # Pass customers_acc
            self.frames[F] = frame 
            frame.grid(row=0, column=0, sticky="nsew")
        self.geometry("300x318")
        
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

        if cont == Page3:
            self.geometry("300x165")  # Adjust the height as needed for Page3
        elif cont==Page1:
            self.geometry("300x330")
        elif cont==Page2:
            self.geometry("300x200")
        elif cont==StartPage:
            self.geometry("240x240")    
        else:
            self.geometry("300x318")
            
class StartPage(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        

        label = ttk.Label(self, text="Welcome to our store", font=LARGEFONT)
        label.grid(row=0, column=6, padx=0, pady=0)

        button1 = ttk.Button(
            self, text="CREATE NEW ACCOUNT", command=lambda: controller.show_frame(Page1)
        )
        button1.grid(row=1, column=6, padx=0, pady=5)

        button2 = ttk.Button(
            self, text="LOGIN to your account", command=lambda: controller.show_frame(Page2)
        )
        button2.grid(row=2, column=6, padx=0, pady=5)

        button3 = ttk.Button(
            self, text="SEARCH FOR ITEMS", command=lambda: controller.show_frame(Page3)
        )
        button3.grid(row=3, column=6, padx=0, pady=5)

        button4 = ttk.Button(
            self, text="VIEW THE ITEMS", command=lambda: controller.show_frame(Page4)
        )
        button4.grid(row=4, column=6, padx=0, pady=5)

        button5 = ttk.Button(
            self, text="ORDER", command=lambda: controller.show_frame(Page5)
        )
        button5.grid(row=5, column=6, padx=0, pady=5)


class Page1(tk.Frame):
    def __init__(self, parent, controller, customers_acc):
        self.customers_acc = customers_acc
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Create New Account", font=LARGEFONT)
        label.grid(row=0, column=2, padx=5, pady=5)

        self.label_name = ttk.Label(self, text='Name:')
        self.label_name.grid(row=6, column=1, padx=8, pady=8)

        self.entry_name = tk.Entry(self)
        self.entry_name.grid(row=6, column=2, padx=8, pady=8)

        self.label_age = tk.Label(self, text='Age:')
        self.label_age.grid(row=7, column=1, padx=8, pady=8)

        self.entry_age = tk.Entry(self)
        self.entry_age.grid(row=7, column=2, padx=8, pady=8)

        self.label_phone = tk.Label(self, text='Phone:')
        self.label_phone.grid(row=8, column=1, padx=8, pady=8)

        self.entry_phone = tk.Entry(self)
        self.entry_phone.grid(row=8, column=2, padx=8, pady=8)

        self.label_address = tk.Label(self, text='Address:')
        self.label_address.grid(row=9, column=1, padx=8, pady=8)

        self.entry_address = tk.Entry(self)
        self.entry_address.grid(row=9, column=2, padx=8, pady=8)

        self.label_email = tk.Label(self, text='Email:')
        self.label_email.grid(row=10, column=1, padx=8, pady=8)

        self.entry_email = tk.Entry(self)
        self.entry_email.grid(row=10, column=2, padx=8, pady=8)

        self.label_password = tk.Label(self, text='Password:')
        self.label_password.grid(row=11, column=1, padx=8, pady=8)

        self.entry_password = tk.Entry(self, show='*')  # Password entry with '*' as a show character
        self.entry_password.grid(row=11, column=2, padx=8, pady=8)

        button2 = ttk.Button(self, text="Create", command=lambda: self.create_account(controller))
        button2.grid(row=12, column=2, padx=10, pady=10)

        button3 = ttk.Button(self, text="GoBack", command=lambda: controller.show_frame(StartPage))
        button3.grid(row=13, column=2, padx=0, pady=0)

    def create_account(self, controller):
        name = self.entry_name.get()
        age = self.entry_age.get()
        phone = self.entry_phone.get()
        address = self.entry_address.get()
        email = self.entry_email.get()
        password = self.entry_password.get()

        customer = Customer(name, age, phone, address, email, password)
        self.customers_acc.addCustomer(customer)
        messagebox.showinfo('Success', 'Account created successfully!')
        controller.show_frame(StartPage)

        # Remove the existing widgets from grid
        self.label_name.grid_remove()
        self.entry_name.grid_remove()
        self.label_age.grid_remove()
        self.entry_age.grid_remove()
        self.label_phone.grid_remove()
        self.entry_phone.grid_remove()
        self.label_address.grid_remove()
        self.entry_address.grid_remove()
        self.label_email.grid_remove()
        self.entry_email.grid_remove()
        self.label_password.grid_remove()
        self.entry_password.grid_remove()

        # Add new widgets to grid
        self.label_name.grid(row=6, column=1, padx=10, pady=10)
        self.entry_name.grid(row=6, column=2, padx=10, pady=10)
        self.label_age.grid(row=7, column=1, padx=10, pady=10)
        self.entry_age.grid(row=7, column=2, padx=10, pady=10)
        self.label_phone.grid(row=8, column=1, padx=10, pady=10)
        self.entry_phone.grid(row=8, column=2, padx=10, pady=10)
        self.label_address.grid(row=9, column=1, padx=10, pady=10)
        self.entry_address.grid(row=9, column=2, padx=10, pady=10)
        self.label_email.grid(row=10, column=1, padx=10, pady=10)
        self.entry_email.grid(row=10, column=2, padx=10, pady=10)
        self.label_password.grid(row=11, column=1, padx=10, pady=10)
        self.entry_password.grid(row=11, column=2, padx=10, pady=10)



class Page2(tk.Frame):
    def __init__(self, parent, controller, customers_acc, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        self.customers_acc = customers_acc
        self.controller = controller

        label = ttk.Label(self, text="Login", font=LARGEFONT)
        label.grid(row=0, column=2, padx=10, pady=10)

        label_name = ttk.Label(self, text='Email:')
        label_name.grid(row=6, column=1, padx=10, pady=10)

        entry_name = tk.Entry(self)
        entry_name.grid(row=6, column=2, padx=10, pady=10)

        label_password = tk.Label(self, text='Password:')
        label_password.grid(row=7, column=1, padx=10, pady=10)

        entry_password = tk.Entry(self, show='*')  # Password entry with '*' as a show character
        entry_password.grid(row=7, column=2, padx=10, pady=10)

        # button to show frame 1 with text
        # layout1
        button1 = ttk.Button(self, text="Login", command=lambda: self.login(entry_name, entry_password))
        button1.grid(row=8, column=2, padx=5, pady=5)
        button2 = ttk.Button(self, text="GoBack", command=lambda: controller.show_frame(StartPage))
        button2.grid(row=9, column=2, padx=0, pady=0)

    def login(self, entry_name, entry_password):
        email = entry_name.get()
        password = entry_password.get()
        login_account = LoginAccount(email, password)
        login_account.searchForCustomers(self.customers_acc, self.go_to_start_page)

    def go_to_start_page(self):
        self.controller.show_frame(StartPage)


class Page3(tk.Frame):
    def __init__(self, parent, controller, items_list, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.items_list = items_list

        label = ttk.Label(self, text="SEARCH FOR ITEMS", font=LARGEFONT)
        label.grid(row=0, column=2, padx=10, pady=10)

        self.label_search = ttk.Label(self, text='Item Name:')
        self.label_search.grid(row=2, column=1, padx=5, pady=0)

        self.entry_search = tk.Entry(self)
        self.entry_search.grid(row=2, column=2, padx=0, pady=0)

        button_search = ttk.Button(self, text="SEARCH", command=self.search)
        button_search.grid(row=4, column=2, padx=10, pady=10)
        self.result_var = tk.StringVar()
        label_result = tk.Label(self, textvariable=self.result_var)
        label_result.grid(row=5, column=1, padx=0, pady=0)

        button2 = ttk.Button(self, text="GoBack", command=lambda: controller.show_frame(StartPage))
        button2.grid(row=5, column=2, padx=1, pady=1)

    def search(self):
        search_query = self.entry_search.get()
        item_search = ItemSearch(itemsList)
        result = item_search.search_item(search_query)
        if result:
            self.result_var.set(f"Item found:\nName: {result['name']}\nPrice: {result['price']}")
        else:
            self.result_var.set('Item not found')


class ItemsForm:
    def __init__(self, items_list):
        self.items_list = items_list
        self.window = tk.Tk()  # Create a new Tkinter window
        self.window.title('Items List')

        self.label_title = ttk.Label(self.window, text='Items List', font=('Helvetica', 16, 'bold'))
        self.label_title.pack()

        for item in self.items_list:
            formatted_item_name = f"{item['name']}"
            formatted_item_price = f"${item['price']:.2f}"

            label_item_name = ttk.Label(self.window, text=formatted_item_name, foreground='blue')
            label_item_price = ttk.Label(self.window, text=formatted_item_price, foreground='green')

            label_item_name.pack()
            label_item_price.pack()

        self.button_close = ttk.Button(self.window, text='Close', command=self.window.destroy)
        self.button_close.pack()

    def show(self):
        self.window.mainloop()

class Page4(tk.Frame):
    def __init__(self, parent, controller, items_list, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Menu", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

    



class Page5(tk.Frame): 
	def __init__(self, parent, controller, *args, **kwargs):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Page 5", font = LARGEFONT)
		label.grid(row = 0, column = 4, padx = 10, pady = 10) 
# Driver Code
app = tkinterApp()
app.mainloop()
