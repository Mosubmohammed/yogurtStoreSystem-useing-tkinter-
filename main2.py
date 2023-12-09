import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
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
                messagebox.showinfo('Welcome', 'Welcome to our store')
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
        self.page6_frame = None  # Initialize self.page6_frame to None

        for F in (StartPage, Page1, Page2, Page3, Page4, Page5, Page6):
            if F == Page1:
                frame = F(container, self, customers_acc)  # Pass customers_acc only
            elif F == Page5:
                frame = F(container, self, itemsList, customers_acc, self.page6_frame, cart)
                self.page6_frame = frame  # Store the instance as an attribute
            else:
                frame = F(container, self, itemsList, customers_acc, cart)  # Pass itemsList, customers_acc, and cart

            self.frames[F] = frame 
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

        if cont == Page3:
            self.geometry("300x320")  # Adjust the height as needed for Page3
        elif cont == Page1:
            self.geometry("300x330")
        elif cont == Page2:
            self.geometry("300x320")
        elif cont == Page4:
            self.geometry("300x500")
        elif cont == Page5:
            self.geometry("300x600")    
        elif cont == StartPage:
            self.geometry("300x320")    
        else:
            self.geometry("300x318")



class StartPage(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent)

        # Load the background image
        image_path = "C:\\Users\\mosup\\OneDrive\\Desktop\\cows-eating-grass-on-summer-pasture-landscape-vector-35428331.png"
        background_image = PhotoImage(file=image_path)
        
        # Resize the image by subsampling (adjust the factors as needed)
        subsample_factor = 3  # Adjust this factor as needed
        background_image = background_image.subsample(subsample_factor, subsample_factor)

        background_label = ttk.Label(self, image=background_image)
        background_label.place(relwidth=1, relheight=1)

        label = ttk.Label(self, text="Welcome to our store", font=LARGEFONT,foreground='#4682B4')
        label.place(relx=0.5, rely=0.1, anchor="center")

        # Calculate the vertical spacing between buttons
        button_spacing = 0.08

        button1 = ttk.Button(
            self, text="CREATE NEW ACCOUNT", command=lambda: controller.show_frame(Page1)
        )
        button1.place(relx=0.5, rely=0.2, anchor="center")
        
        button2 = ttk.Button(
            self, text="LOGIN to your account", command=lambda: controller.show_frame(Page2)
        )
        button2.place(relx=0.5, rely=0.2 + button_spacing, anchor="center")

        button3 = ttk.Button(
            self, text="SEARCH FOR ITEMS", command=lambda: controller.show_frame(Page3)
        )
        button3.place(relx=0.5, rely=0.2 + 2 * button_spacing, anchor="center")

        button4 = ttk.Button(
            self, text="VIEW THE ITEMS", command=lambda: controller.show_frame(Page4)
        )
        button4.place(relx=0.5, rely=0.2 + 3 * button_spacing, anchor="center")

        button5 = ttk.Button(
            self, text="ORDER", command=lambda: controller.show_frame(Page5)
        )
        button5.place(relx=0.5, rely=0.2 + 4 * button_spacing, anchor="center")

        button6 = ttk.Button(
            self, text="Cart", command=lambda: controller.show_frame(Page6)
        )
        button6.place(relx=0.5, rely=0.2 + 5 * button_spacing, anchor="center")

        # Keep a reference to the image to prevent it from being garbage collected
        self.background_image = background_image


class Page1(tk.Frame):
    def __init__(self, parent, controller, customers_acc):
        self.customers_acc = customers_acc
        tk.Frame.__init__(self, parent)
        
        image_path = "C:\\Users\\mosup\\OneDrive\\Desktop\\cows-eating-grass-on-summer-pasture-landscape-vector-35428331.png"
        background_image = PhotoImage(file=image_path)
        
        # Resize the image by subsampling (adjust the factors as needed)
        subsample_factor = 3  # Adjust this factor as needed
        background_image = background_image.subsample(subsample_factor, subsample_factor)

        background_label = ttk.Label(self, image=background_image)
        background_label.place(relwidth=1, relheight=1)

        label = ttk.Label(self, text="Create New Account", font=LARGEFONT, foreground='#4682B4')
        label.grid(row=0, column=2, padx=5, pady=5)

        self.label_name = ttk.Label(self, text='Name:', foreground='#4682B4')
        self.label_name.grid(row=6, column=1, padx=8, pady=8)

        self.entry_name = tk.Entry(self)
        self.entry_name.grid(row=6, column=2, padx=8, pady=8)
        self.entry_name.config(validate='key', validatecommand=(self.register(self.validate_name), '%P'))

        self.label_age = tk.Label(self, text='Age:', foreground='#4682B4')
        self.label_age.grid(row=7, column=1, padx=8, pady=8)

        self.entry_age = tk.Entry(self)
        self.entry_age.grid(row=7, column=2, padx=8, pady=8)
        self.entry_age.config(validate='key', validatecommand=(self.register(self.validate_age), '%P'))

        self.label_phone = tk.Label(self, text='Phone:', foreground='#4682B4')
        self.label_phone.grid(row=8, column=1, padx=8, pady=8)

        self.entry_phone = tk.Entry(self)
        self.entry_phone.grid(row=8, column=2, padx=8, pady=8)
        self.entry_phone.config(validate='key', validatecommand=(self.register(self.validate_phone), '%P'))

        self.label_address = tk.Label(self, text='Address:', foreground='#4682B4')
        self.label_address.grid(row=9, column=1, padx=8, pady=8)

        self.entry_address = tk.Entry(self)
        self.entry_address.grid(row=9, column=2, padx=8, pady=8)

        self.label_email = tk.Label(self, text='Email:', foreground='#4682B4')
        self.label_email.grid(row=10, column=1, padx=8, pady=8)

        self.entry_email = tk.Entry(self)
        self.entry_email.grid(row=10, column=2, padx=8, pady=8)

        self.label_password = tk.Label(self, text='Password:', foreground='#4682B4')
        self.label_password.grid(row=11, column=1, padx=8, pady=8)

        self.entry_password = tk.Entry(self, show='*')  # Password entry with '*' as a show character
        self.entry_password.grid(row=11, column=2, padx=8, pady=8)

        button2 = ttk.Button(self, text="Create", command=lambda: self.create_account(controller))
        button2.grid(row=12, column=2, padx=10, pady=10)

        button3 = ttk.Button(self, text="GoBack", command=lambda: controller.show_frame(StartPage))
        button3.grid(row=13, column=2, padx=0, pady=0)
        self.background_image = background_image

    def create_account(self, controller):
        name = self.entry_name.get()
        age = self.entry_age.get()
        phone = self.entry_phone.get()
        address = self.entry_address.get()
        email = self.entry_email.get()
        password = self.entry_password.get()

        # Check if any of the fields is empty
        if not name or not age or not phone or not address or not email or not password:
            messagebox.showerror('Error', 'Please fill in all fields.')
            return

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

    def validate_name(self, value):
        return all(char.isalpha() or char.isspace() for char in value)

    def validate_age(self, value):
        try:
            # Attempt to convert the input value to an integer
            age = int(value)
            return 0 <= age <= 150  # Allow ages between 0 and 150
        except ValueError:
            return False  # If the conversion fails, return False

    def validate_phone(self, value):
        return value.isdigit()


class Page2(tk.Frame):
    def __init__(self, parent, controller, items_list, customers_acc, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        self.customers_acc = customers_acc
        self.controller = controller

        image_path = "C:\\Users\\mosup\\OneDrive\\Desktop\\cows-eating-grass-on-summer-pasture-landscape-vector-35428331.png"
        background_image = PhotoImage(file=image_path)
        
        # Resize the image by subsampling (adjust the factors as needed)
        subsample_factor = 3  # Adjust this factor as needed
        background_image = background_image.subsample(subsample_factor, subsample_factor)

        background_label = ttk.Label(self, image=background_image)
        background_label.place(relwidth=1, relheight=1)
        self.background_image = background_image


        label = ttk.Label(self, text="Login", font=LARGEFONT,foreground='#4682B4')
        label.grid(row=0, column=2, padx=10, pady=10)

        label_name = ttk.Label(self, text='Email:',foreground='#4682B4')
        label_name.grid(row=6, column=1, padx=10, pady=10)

        entry_name = tk.Entry(self)
        entry_name.grid(row=6, column=2, padx=10, pady=10)

        label_password = tk.Label(self, text='Password:',foreground='#4682B4')
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

        # Use a more darker shade of blue
        style = ttk.Style()
        style.configure('TButton', background='#4682B4', foreground='#4682B4')

        image_path = "C:\\Users\\mosup\\OneDrive\\Desktop\\cows-eating-grass-on-summer-pasture-landscape-vector-35428331.png"
        background_image = PhotoImage(file=image_path)

        # Resize the image by subsampling (adjust the factors as needed)
        subsample_factor = 3  # Adjust this factor as needed
        background_image = background_image.subsample(subsample_factor, subsample_factor)

        background_label = ttk.Label(self, image=background_image)
        background_label.place(relwidth=1, relheight=1)

        self.background_image = background_image

        label = ttk.Label(self, text="SEARCH FOR ITEMS", font=LARGEFONT, foreground='#4682B4')
        label.grid(row=0, column=2, padx=10, pady=10)

        self.label_search = ttk.Label(self, text='Item Name:', foreground='#4682B4')
        self.label_search.grid(row=2, column=1, padx=5, pady=0)

        self.entry_search = tk.Entry(self)
        self.entry_search.grid(row=2, column=2, padx=0, pady=0)

        button_search = ttk.Button(self, text="SEARCH", command=self.search, style='TButton')
        button_search.grid(row=4, column=2, padx=10, pady=10)

        self.result_var = tk.StringVar()
        label_result = tk.Label(self, textvariable=self.result_var, foreground='#4682B4')
        label_result.grid(row=5, column=1, padx=0, pady=0)

        button2 = ttk.Button(self, text="GoBack", command=lambda: controller.show_frame(StartPage), style='TButton')
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

        image_path = "C:\\Users\\mosup\\OneDrive\\Desktop\\cows-eating-grass-on-summer-pasture-landscape-vector-35428331.png"
        background_image = PhotoImage(file=image_path)
        
        # Resize the image by subsampling (adjust the factors as needed)
        subsample_factor = 2  # Adjust this factor as needed
        background_image = background_image.subsample(subsample_factor, subsample_factor)

        background_label = ttk.Label(self, image=background_image)
        background_label.place(relwidth=1, relheight=1)

        self.background_image = background_image

        for index, item in enumerate(items_list, start=1):
            formatted_item_name = f"{item['name']}"
            formatted_item_price = f"${item['price']:.2f}"

            label_item_name = ttk.Label(self, text=formatted_item_name, foreground='#4682B4')
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
        self.page6_frame = page6_frame  # Use the existing page6_frame
        self.items_list = items_list   # Store items_list as an attribute

        image_path = "C:\\Users\\mosup\\OneDrive\\Desktop\\cows-eating-grass-on-summer-pasture-landscape-vector-35428331.png"
        background_image = PhotoImage(file=image_path)
        
        # Resize the image by subsampling (adjust the factors as needed)
        subsample_factor = 1  # Adjust this factor as needed
        background_image = background_image.subsample(subsample_factor, subsample_factor)

        background_label = ttk.Label(self, image=background_image)
        background_label.place(relwidth=1, relheight=1)

        self.background_image = background_image

        label = ttk.Label(self, text="Order Items", foreground='#4682B4')
        label.grid(row=0, column=3, padx=10, pady=10)

        for index, item in enumerate(items_list, start=1):
            formatted_item_name = f"{item['name']}"
            formatted_item_price = f"${item['price']:.2f}"

            label_item_name = ttk.Label(self, text=formatted_item_name, foreground='#4682B4')
            label_item_price = ttk.Label(self, text=formatted_item_price, foreground='green')

            label_item_name.grid(row=index, column=3, padx=10, pady=5)
            label_item_price.grid(row=index, column=4, padx=10, pady=5)

        button_back = ttk.Button(self, text="Go Back", command=lambda: controller.show_frame(StartPage))
        button_back.grid(row=19, column=3, padx=5, pady=5)

        self.label_name = ttk.Label(self, text='Item Name:', foreground='#4682B4')
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
                    # Print item details to the console (you can replace this with your desired action)
                    print(f'Item added to cart: {item_name} - Price: ${result["price"]:.2f}')

                    # Add the item to the cart
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

        image_path = "C:\\Users\\mosup\\OneDrive\\Desktop\\cows-eating-grass-on-summer-pasture-landscape-vector-35428331.png"
        background_image = PhotoImage(file=image_path)

        # Resize the image by subsampling (adjust the factors as needed)
        subsample_factor = 3  # Adjust this factor as needed
        background_image = background_image.subsample(subsample_factor, subsample_factor)

        background_label = ttk.Label(self, image=background_image)
        background_label.place(relwidth=1, relheight=1)

        self.background_image = background_image

        self.label_item_details = ttk.Label(self, text='', foreground='#4682B4')
        self.label_item_details.grid(row=5, column=9, padx=0, pady=8)

        label = ttk.Label(self, text="Cart", foreground='#4682B4')
        label.grid(row=0, column=10, padx=10, pady=10)

        self.label_cart = tk.Label(self, text='Items in Cart:', foreground='#4682B4')
        self.label_cart.grid(row=1, column=10, padx=0, pady=8)

        self.listbox_cart = tk.Listbox(self, selectmode=tk.SINGLE)
        self.listbox_cart.grid(row=2, column=10, padx=0, pady=0)

        button_back = ttk.Button(self, text="Go Back", command=lambda: controller.show_frame(StartPage))
        button_back.grid(row=3, column=10, padx=5, pady=5)


    def update_order_list(self, items_list):
    # Add the new items to the listbox without clearing the current items
        for item_name in self.cart.orderList:
            result = next((item for item in items_list if item['name'] == item_name), None)
            if result:
                item_info = f"{item_name}: ${result['price']:.2f}"
                self.listbox_cart.insert(tk.END, item_info)

                # Update the label with item details
                self.label_item_details.config(text=f"Selected Item: {item_info}")

                # Print item details to the console (you can replace this with your desired action)
                print(f'Item added to cart: {item_info}')

app = tkinterApp()
app.mainloop()
