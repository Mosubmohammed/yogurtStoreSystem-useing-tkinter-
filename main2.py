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
    def __init__(self, email, password, callback=None):
        super().__init__("", "", "", "", email, password)
        self.callback = callback  # Store the callback function

    def searchForCustomers(self, customers_acc):
        for customer in customers_acc.customersList:
            if self.email == customer.email and self._Customer__password == customer._Customer__password:
                messagebox.showinfo('Welcome', 'Welcome back!')
                if self.callback:
                    self.callback()  # Call the callback function if provided
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
class ItemsForm(tk.Frame):
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

    def show(self):
        self.window.mainloop()


class Cart:
    def __init__(self):
        self.orderList = []

    def add_item(self, item_name):
        self.orderList.append(item_name)


LARGEFONT =("Verdana", 12)





class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs): 
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self) 
        container.pack(side="top", fill="both", expand=True) 

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        customers_acc = CustomersAcc()  # Move the CustomersAcc instantiation here
        cart = Cart()  # Create a single instance of the Cart class

        for F in (StartPage, Page1, Page2, Page3, Page4, Page5, Page6):
            if F == Page1:
                frame = F(container, self, customers_acc)  # Pass customers_acc only
            elif F == Page5:
                page6_frame = Page6(container, self, itemsList, customers_acc, cart)  # Create an instance of Page6
                frame = F(container, self, itemsList, customers_acc, page6_frame, cart)  # Pass itemsList, customers_acc, and cart
                self.page6_frame = page6_frame  # Store the instance as an attribute




            else:
                frame = F(container, self, itemsList, customers_acc, cart)  # Pass itemsList, customers_acc, and cart
            self.frames[F] = frame 
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)





    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

        if cont == Page3:
            self.geometry("300x165")  # Adjust the height as needed for Page3
        elif cont == Page1:
            self.geometry("300x330")
        elif cont == Page2:
            self.geometry("300x200")
        elif cont == Page4:
            self.geometry("250x500")
        elif cont == Page5:
            self.geometry("300x600")    
        elif cont == StartPage:
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

        button6 = ttk.Button(
            self, text="Cart", command=lambda: controller.show_frame(Page6)
        )
        button6.grid(row=6, column=6, padx=0, pady=5)


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
    def __init__(self, parent, controller, items_list, customers_acc, *args, **kwargs):
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
        login_account = LoginAccount(email, password, self.go_to_start_page)  # Pass the callback method
        login_account.searchForCustomers(self.customers_acc)

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



class Page4(tk.Frame):
    def __init__(self, parent, controller, items_list, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Menu", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        for index, item in enumerate(items_list, start=1):
            formatted_item_name = f"{item['name']}"
            formatted_item_price = f"${item['price']:.2f}"

            label_item_name = ttk.Label(self, text=formatted_item_name, foreground='blue')
            label_item_price = ttk.Label(self, text=formatted_item_price, foreground='green')

            label_item_name.grid(row=index, column=4, padx=10, pady=5)
            label_item_price.grid(row=index, column=5, padx=10, pady=5)

        button_back = ttk.Button(self, text="Go Back", command=lambda: controller.show_frame(StartPage))
        button_back.grid(row=len(items_list) + 1, column=4, columnspan=2, padx=10, pady=10)
    



class Page5(tk.Frame):
    def __init__(self, parent, controller, items_list, customers_acc, page6_frame, cart, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.cart = cart
        self.page6_frame = page6_frame
        self.items_list = items_list  # Store items_list as an attribute

        label = ttk.Label(self, text="Order Items", font=LARGEFONT)
        label.grid(row=0, column=3, padx=10, pady=10)

        for index, item in enumerate(items_list, start=1):
            formatted_item_name = f"{item['name']}"
            formatted_item_price = f"${item['price']:.2f}"

            label_item_name = ttk.Label(self, text=formatted_item_name, foreground='blue')
            label_item_price = ttk.Label(self, text=formatted_item_price, foreground='green')

            label_item_name.grid(row=index, column=3, padx=10, pady=5)
            label_item_price.grid(row=index, column=4, padx=10, pady=5)

        button_back = ttk.Button(self, text="Go Back", command=lambda: controller.show_frame(StartPage))
        button_back.grid(row=19, column=3, padx=0, pady=0)

        self.label_name = ttk.Label(self, text='Item Name:')
        self.label_name.grid(row=17, column=3, padx=0, pady=8)

        self.entry_name = tk.Entry(self)
        self.entry_name.grid(row=17, column=4, padx=0, pady=8)

        button_add_item = ttk.Button(self, text="Add Item", command=self.add_item_to_cart)
        button_add_item.grid(row=18, column=3, padx=0, pady=0)

    def add_item_to_cart(self):
        item_name = self.entry_name.get()
        item_search = ItemSearch(self.items_list)
        result = item_search.search_item(item_name)

        if not item_name:
            messagebox.showerror('Error', 'Please enter an item name.')
        elif result:
            if item_name in self.cart.orderList:
                messagebox.showerror('Error', f'{item_name} is already in the cart.')
            else:
                
                messagebox.showinfo('Item Added', f'{item_name} added to the cart!')
                self.cart.add_item(item_name)
                # Update the order list in Page6
                if self.page6_frame:
                    self.page6_frame.update_order_list(self.items_list)
        else:
            messagebox.showerror('Error', f'{item_name} not found.')




class Page6(tk.Frame):
    def __init__(self, parent, controller, items_list, customers_acc, cart, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.cart = cart
        self.items_list = items_list  # Store items_list as an attribute

        label = ttk.Label(self, text="Your Cart", font=LARGEFONT)
        label.grid(row=0, column=3, padx=10, pady=10)

        self.order_list_var = tk.StringVar()
        label_order_list = tk.Label(self, textvariable=self.order_list_var)
        label_order_list.grid(row=1, column=3, padx=10, pady=5)

        button_back = ttk.Button(self, text="Go Back", command=lambda: controller.show_frame(StartPage))
        button_back.grid(row=18, column=4, columnspan=2, padx=0, pady=0)

    def update_order_list(self, items_list):
        order_list_text = "Your Cart:\n"
        for item_name in self.cart.orderList:
            result = ItemSearch(items_list).search_item(item_name)
            if result:
                order_list_text += f"{result['name']} - ${result['price']:.2f}\n"
        
        self.order_list_var.set(order_list_text)





# class Page6(tk.Frame):
    # def __init__(self, parent, controller, items_list, customers_acc, cart, *args, **kwargs):
    #     tk.Frame.__init__(self, parent)
    #     self.controller = controller
    #     self.cart = cart

    #     label = ttk.Label(self, text="Your Order's", font=LARGEFONT)
    #     label.grid(row=0, column=3, padx=10, pady=10)

    #     self.order_frame = tk.Frame(self)  # Frame to hold the order labels
    #     self.order_frame.grid(row=1, column=3, padx=10, pady=10)

    #     button_back = ttk.Button(self, text="Go Back", command=lambda: controller.show_frame(StartPage))
    #     button_back.grid(row=2, column=3, padx=10, pady=10)

    #     self.label_item_name_list = []  # Initialize the label list
    #     self.label_item_price_list = []  # Initialize the label list

    # def update_order_list(self, items_list, new_item_name=None):
    #     # Clear existing labels
    #     for label_name in self.label_item_name_list:
    #         label_name.destroy()
    #     for label_price in self.label_item_price_list:
    #         label_price.destroy()

    #     self.label_item_name_list = []
    #     self.label_item_price_list = []

    #     # Display the items in the cart
    #     for index, item_name in enumerate(self.cart.orderList, start=1):
    #         item = ItemSearch(items_list=items_list).search_item(item_name)

    #         formatted_item_name = f"{item_name}"
    #         formatted_item_price = f"${item['price']:.2f}" if item else "Price not available"

    #         label_item_name = ttk.Label(self.order_frame, text=formatted_item_name, foreground='blue')
    #         label_item_price = ttk.Label(self.order_frame, text=formatted_item_price, foreground='green')

    #         label_item_name.grid(row=index, column=0, padx=10, pady=5)
    #         label_item_price.grid(row=index, column=1, padx=10, pady=5)

    #         self.label_item_name_list.append(label_item_name)
    #         self.label_item_price_list.append(label_item_price)

    #     # If a new item is provided, add it to the order list and update the display
    #     if new_item_name:
    #         self.cart.orderList.append(new_item_name)
    #         formatted_new_item_name = f"{new_item_name}"
    #         new_item = ItemSearch(items_list=items_list).search_item(new_item_name)
    #         formatted_new_item_price = f"${new_item['price']:.2f}" if new_item else "Price not available"

    #         label_new_item_name = ttk.Label(self.order_frame, text=formatted_new_item_name, foreground='blue')
    #         label_new_item_price = ttk.Label(self.order_frame, text=formatted_new_item_price, foreground='green')

    #         label_new_item_name.grid(row=len(self.cart.orderList), column=0, padx=10, pady=5)
    #         label_new_item_price.grid(row=len(self.cart.orderList), column=1, padx=10, pady=5)

    #         self.label_item_name_list.append(label_new_item_name)
    #         self.label_item_price_list.append(label_new_item_price)

    #     self.order_frame.update_idletasks()  # Force update the order_frame






# Driver Code
app = tkinterApp()
app.mainloop()
