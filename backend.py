import tkinter as tk
from tkinter import messagebox
import os, tempfile, win32api, win32print, atexit, smtplib
from palette import get_colors
from utils import setup_resize_event
import base64
from dotenv import load_dotenv

# Ensures that any temporary files created by the program are deleted when the program is finished running.
TEMP_FILES = []

def cleanup_temp_files():
    for file in TEMP_FILES:
        try:
            os.remove(file)
        except Exception as e:
            print(f"Error al eliminar el archivo temporal {file}: {e}")


atexit.register(cleanup_temp_files)



class BillingApp:
    def __init__(
        self,
        entries,
        cosmeticPriceEntry,
        groceriesPriceEntry,
        drinksPricesEntry,
        cosmeticTaxesEntry,
        groceriesTaxesEntry,
        drinksTaxesEntry,
        nameEntry,
        emailEntry,
        phoneEntry,
        billEntry,
        addressEntry,
        zipEntry,
        cityEntry,
        countryEntry,
        textarea,
    ):
        # Si tienes algún código de inicialización, ponlo aquí.

        # Customer data inputs
        self.nameEntry = nameEntry
        self.emailEntry = emailEntry
        self.phoneEntry = phoneEntry
        self.billEntry = billEntry
        self.addressEntry = addressEntry
        self.zipEntry = zipEntry
        self.cityEntry = cityEntry
        self.countryEntry = countryEntry

        # Products Data inputs

        
        # Bill Menu entries
        self.cosmeticPriceEntry = cosmeticPriceEntry
        self.groceriesPriceEntry = groceriesPriceEntry
        self.drinksPricesEntry = drinksPricesEntry
        self.cosmeticTaxesEntry = cosmeticTaxesEntry
        self.groceriesTaxesEntry = groceriesTaxesEntry
        self.drinksTaxesEntry = drinksTaxesEntry
        self.textarea = textarea

        self.total_general = 0.0
        self.entries = entries

    def total(self):
        # Precios de productos
        self.prices = {
            # Cosmetics
            "cosmetics": {
                "soap": 3.90,
                "cream": 8.12,
                "wash": 6.85,
                "spray": 5.60,
                "gel": 8.90,
                "lotion": 10.20,
                "eye": 4.30,
                "lip": 6.50,
            },
            # Groceries
            "groceries": {
                "rice": 2.50,
                "oil": 4.50,
                "eggs": 2.10,
                "sugar": 2.60,
                "tea": 2.10,
                "cinnamon": 3.10,
                "bread": 1.20,
                "salt": 2.40,
            },
            # Drinks
            "drinks": {
                "beer": 4.10,
                "soda": 3.20,
                "water": 1.20,
                "coffee": 2.25,
                "fanta": 1.80,
                "pepsy": 1.80,
                "aquarius": 1.60,
                "lemonade": 1.10,
            },
        }

        # Porcentaje de Impuestos de los productos
        taxes = {"cosmetics": 21, "groceries": 21, "drinks": 15}

        # Calcula los totales por segmento y el total general
        total_cosmetics = sum(
            self.prices["cosmetics"][product]
            * (
                float(self.entries["cosmetics"][product].get())
                if self.entries["cosmetics"][product].get()
                else 0
            )
            for product in self.prices["cosmetics"]
        )

        total_groceries = sum(
            self.prices["groceries"][product]
            * (
                float(self.entries["groceries"][product].get())
                if self.entries["groceries"][product].get()
                else 0
            )
            for product in self.prices["groceries"]
        )
        total_drinks = sum(
            self.prices["drinks"][product]
            * (
                float(self.entries["drinks"][product].get())
                if self.entries["drinks"][product].get()
                else 0
            )
            for product in self.prices["drinks"]
        )

        selected_products = []

        for category, products in self.prices.items():
            for product in products:
                value = (
                    int(self.entries[category][product].get())
                    if self.entries[category][product].get()
                    else 0
                )
                if value > 0:
                    print(f"Selected product from {category}: {product}, {value}")
                    selected_products.append((category, product, value))

        self.total_general = total_cosmetics + total_groceries + total_drinks
        print("\n----------------------------------------------\n")
        # Totales sin Impuestos
        self.cosmeticPriceEntry.delete(0, tk.END)
        self.cosmeticPriceEntry.insert(0, str(round(total_cosmetics, 2)) + " €")

        self.groceriesPriceEntry.delete(0, tk.END)
        self.groceriesPriceEntry.insert(0, str(round(total_groceries, 2)) + " €")

        self.drinksPricesEntry.delete(0, tk.END)
        self.drinksPricesEntry.insert(0, str(round(total_drinks, 2)) + " €")

        print("\nTotal cosmetics is:", round(total_cosmetics, 2))
        print("Total groceries is:", round(total_groceries, 2))
        print("Total drinks is:", round(total_drinks, 2))
        print("\n----------------------------------------------\n")
        print("Total general is:", round(self.total_general, 2))

        # Calculo Añadiento impuestos
        cosmetics_taxes = total_cosmetics * taxes["cosmetics"] / 100
        groceries_taxes = total_groceries * taxes["groceries"] / 100
        drinks_taxes = total_drinks * taxes["drinks"] / 100

        self.total_taxes = cosmetics_taxes + groceries_taxes + drinks_taxes

        bill_cosmetics = total_cosmetics + cosmetics_taxes
        bill_groceries = total_groceries + groceries_taxes
        bill_drinks = total_drinks + drinks_taxes

        self.total_general_taxes = bill_cosmetics + bill_groceries + bill_drinks

        # Totales con Impuestos
        self.cosmeticTaxesEntry.delete(0, tk.END)
        self.cosmeticTaxesEntry.insert(0, str(round(cosmetics_taxes, 2)) + " €")

        self.groceriesTaxesEntry.delete(0, tk.END)
        self.groceriesTaxesEntry.insert(0, str(round(groceries_taxes, 2)) + " €")

        self.drinksTaxesEntry.delete(0, tk.END)
        self.drinksTaxesEntry.insert(0, str(round(drinks_taxes, 2)) + " €")

        print("Total cosmetics with taxes is:", round(bill_cosmetics, 2))
        print("Total groceries with taxes is:", round(bill_groceries, 2))
        print("Total drinks with taxes is:", round(bill_drinks, 2))
        print("----------------------------------------------\n")
        print("Total to bill is :", round(self.total_general_taxes, 2))

        result = {
            "total_general": self.total_general,
            "total_general_taxes": self.total_general_taxes,
            "selected_products": selected_products,
            "total_taxes": self.total_taxes,
        }
        return result

    def toBill(self):
        name = self.nameEntry.get()
        email = self.emailEntry.get()
        phone = self.phoneEntry.get()
        invoice = self.billEntry.get()
        address = self.addressEntry.get()
        cp = self.zipEntry.get()
        city = self.cityEntry.get()
        country = self.countryEntry.get()
        # cosmetics = self.cosmeticPriceEntry.get()
        # groceries = self.groceriesPriceEntry.get()
        # drinks = self.drinksPricesEntry.get()
        textarea = self.textarea
        textarea.configure(state="normal")
        result = self.total()
        if name == "":
            messagebox.showerror(
                "Denegado!", "Debe rellenar todos los datos del cliente"
            )
            print("Denied! name entry value is required!")
        # Force the user to fill a products frame
        # elif result["total_general"] == 0 :
        #     print('Entry products')
        #     messagebox.showerror("Denegado!", "No hay datos que facturar")
        #     print('Denied! there is not invoice data to bill')
        else:
            print("The total is : ", round(result["total_general"], 2))
            print("The total with taxes is : ", round(result["total_general_taxes"], 2))
            textarea.delete(1.0, tk.END)
            textarea.insert(tk.END, f"\n\t\t*** Welcome {name} ***")
            textarea.insert(tk.END, f"\n\nBill Number : {invoice}")
            textarea.insert(tk.END, f"\nName : {name} \t\tEmail : {email}")
            # textarea.insert(tk.END, f'\nCustomer Email : {email}')
            textarea.insert(tk.END, f"\nPhone : {phone}")
            textarea.insert(tk.END, f"\nAddress : {address} {cp}")
            # textarea.insert(tk.END, f'\nCustomer CP : {cp}')
            textarea.insert(tk.END, f"\nCity/Country : {city} - {country}")
            # textarea.insert(tk.END, f'\nCustomer Country : {country}')
            textarea.insert(
                tk.END, "\n====================================================="
            )
            textarea.insert(tk.END, "\nProducts\t\t\tQty \t\t\tPrice (€)")
            textarea.insert(
                tk.END, "\n====================================================="
            )

            print(result["selected_products"])

            products = result["selected_products"]

            for category, product, value in products:
                price = round(self.prices[category][product], 2)
                total_price = round(price * value, 2)
                # print(category.capitalize())
                # print(product)
                # print(value)
                # print(price * value)
                textarea.insert(
                    tk.END,
                    f"\n{product.capitalize()} \t\t\t{value} \t\t\t{total_price}",
                )

            textarea.insert(
                tk.END, "\n====================================================="
            )

            subtotal = round(result["total_general"], 2)
            taxes = round(result["total_taxes"], 2)
            total = round(result["total_general_taxes"], 2)
            textarea.insert(tk.END, f"\nSubtotal:  \t\t\t\t\t\t{subtotal}")
            textarea.insert(tk.END, f"\nTaxes:  \t\t\t\t\t\t{taxes}")

            textarea.insert(
                tk.END, "\n====================================================="
            )
            textarea.insert(tk.END, f"\nTOTAL TO PAY: \t\t\t\t\t\t{total} €\n")

            # for debugging
            bill_content = self.textarea.get(1.0, tk.END).strip()
            print(bill_content)

            textarea.configure(state="disabled")

    def save_bill(self):
        bill_content = self.textarea.get(1.0, tk.END).strip()
        invoice = self.billEntry.get()
        total_amount = self.total()["total_general"]

        if not bill_content:
            messagebox.showerror("Error", "No text to be saved! First, generate a bill.")
            print("No text to be saved! First, generate a bill.")
            return

        if not invoice:
            messagebox.showerror("Error", "Invoice number is required!")
            print("Invoice number is required!")
            return

        # Comentar esta funcion en caso de que se requiera que el usuario genere facturas con importe cero
        if total_amount == 0:
            messagebox.showerror("Error", "Select values in products!")
            print("Select values in products!")
            return

        if not messagebox.askyesno("Confirm", "Do you want to save the bill?"):
            return

        with open(f"bills/{invoice}.txt", "w", encoding="utf-8") as file:
            file.write(bill_content)

        messagebox.showinfo(
            "Success", f"The invoice number: {invoice} is saved successfully!"
        )
        print(f"The invoice number: {invoice} is saved successfully!")

    def printBill(self):
        content = self.textarea.get(1.0, tk.END).strip()
        if not content:
            print("Error, Bill is empty")
            messagebox.showerror("Error", "Bill is empty!")
        else:
            # obtener el nombre de la impresora predeterminada
            printer_name = win32print.GetDefaultPrinter()
            # Usar NamedTemporaryFile y no eliminarlo automáticamente cuando se cierre
            with tempfile.NamedTemporaryFile(
                mode="w+t", delete=False, suffix=".txt"
            ) as temp_file:
                TEMP_FILES.append(temp_file.name)
                temp_file.write(content)
                temp_file.flush()  # Asegurarse de que todo se haya escrito en el disco
                # os.startfile(temp_file.name, 'print') #Abre el archivo primero, no necesario
                # Intentar imprimir el archivo
                win32api.ShellExecute(
                    0, "printto", temp_file.name, '"%s"' % printer_name, ".", 0
                )

    def email_form(self):
        invoice = self.billEntry.get()
        colors = get_colors()
        textarea = self.textarea
        
        # Loads environment variables from .env into process's enviroment variable list , and encoded password
        load_dotenv()
        password = os.getenv("PASSWORD")
        encoded_password = base64.b64encode(password.encode()).decode()
        decoded_password = base64.b64decode(encoded_password).decode()

        if not invoice :
            messagebox.showerror('Error', 'Invoice number is required!')
            return

        def send_email():
            ## Valorar metodo o funcion para cambiar variable password que por defecto obtiene su valor de la vairable local, con el boton change login data
            # passwordSender = passwordEntry.get()
            # password = passwordSender

            smtpserver = "smtp.gmail.com"  # SMTP server address (Gmail used here)
            sender = senderEntry.get()
            reciever = recipientEntry.get()
            message = messageTextarea.get(1.0, tk.END)
            encoded_message = message.encode('utf-8')

            if not sender:
                messagebox.showerror('Error', "The sender's email is required!")
                print('Error', "The sender's email is required!")
                return
            
            if not reciever:
                messagebox.showerror('Error', "The reciever's email is required!")
                print('Error', "The reciever's email is required!")
                return
            
            try:
                ob = smtplib.SMTP(smtpserver, 587)
                ob.starttls()
                ob.login(sender, decoded_password) 
                ob.sendmail(sender, reciever, encoded_message)
                ob.quit()
                messagebox.showinfo('Success', f'Bill {invoice} is successfully sent')
            except smtplib.SMTPAuthenticationError as e:
                print("Authentication Error:", e)
                messagebox.showerror('Authentication Error', 'Failed to login. Please check your email and password.')
            except Exception as e:
                print("Error:", e)
                messagebox.showerror('Error', 'Something went wrong!, Please try again')

        # Oculta o muestra la contraseña en el Entry.
        def toggle_password():
            if passwordEntry.cget("show") == "":
                passwordEntry.config(show="*")
                showpasswordButton.config(text="Show Password")
            else:
                passwordEntry.config(show="")
                showpasswordButton.config(text="Hide Password")

        # Desbloquea Sender y Password Entries
        def changeLoginData():
            if passwordEntry.cget("state") == "disabled" and senderEntry.cget("state") == "disabled":
                passwordEntry.config(state='normal')
                senderEntry.config(state='normal')
            else:
                passwordEntry.config(state='disabled')
                senderEntry.config(state='disabled')

        if textarea.get(1.0, tk.END) == "\n":
            messagebox.showerror("Error", "Bill is empty!")
        else:
            root1 = tk.Toplevel()
            # setup_resize_event(root1) # Solo para desarrollo, borrar en produccion
            root1.config(bg=colors["bg"])
            root1.title("Send Email")
            root1.geometry("500x620+650+300")
            root1.resizable(False, False)
            root1.grab_set()  # Bloquea root, acceso a ventana padre

            sender_frame = tk.Frame(root1, bg=colors["bg"])
            sender_frame.pack(pady=(30, 0), ipadx=10, ipady=10, padx=10, fill="x")
            senderFrame = tk.LabelFrame(
                sender_frame,
                text="Send Email",
                font=("titillium web regular", 14),
                bg=colors["bg"],
                fg=colors["font"],
                bd=0,
            )
            senderFrame.pack(padx=10, ipady=10, fill="x")
            senderFrame.columnconfigure(0, weight=1)

            senderLabel = tk.Label(
                senderFrame,
                text="Your Email",
                font=("titillium web light", 10),
                bg=colors["bg"],
                fg=colors["font"],
            )
            senderLabel.grid(row=0, column=0, padx=10, pady=(20, 0), sticky="w")
            senderEntry = tk.Entry(
                senderFrame,
                font=("titillium web light", 10),
                bg=colors["entry"],
                fg=colors["font"],
                width=45,
                insertbackground=colors["font"],  # color del cursor
            )
            senderEntry.grid(row=0, column=1, padx=8, pady=(20, 0), sticky="w")
            senderEntry.insert(0, 'davidcastagnetoa@gmail.com') # Establece el valor predeterminado para senderEntry
            senderEntry.config(state='disabled') # Deshabilita senderEntry

            passwordLabel = tk.Label(
                senderFrame,
                text="Your Password",
                font=("titillium web light", 10),
                bg=colors["bg"],
                fg=colors["font"],
            )
            passwordLabel.grid(row=1, column=0, padx=10, pady=8, sticky="w")
            passwordEntry = tk.Entry(
                senderFrame,
                font=("titillium web light", 10),
                bg=colors["entry"],
                fg=colors["font"],
                show="*",
                width=45,
                insertbackground=colors["font"],  # color del cursor
            )
            passwordEntry.grid(row=1, column=1, padx=8, pady=8, sticky="w")
            passwordEntry.insert(0, encoded_password) # Establece el valor predeterminado para passwordEntry, contraseña codificada
            passwordEntry.config(state='disabled') # Deshabilita passwordEntry

            loginButtonFrame = tk.Frame(
                senderFrame,
                bg=colors["bg"],
            )
            loginButtonFrame.grid(row=2, column=0, columnspan=2, sticky="ew")
            loginButtonFrame.columnconfigure(0, weight=1)
            loginButtonFrame.columnconfigure(1, weight=1)

            showpasswordButton = tk.Button(
                loginButtonFrame,
                font=("titillium web semibold", 9),
                text="Show Password",
                bg=colors["button"],
                fg=colors["bg"],
                # padx= 15,
                bd=0,
                width=18,
                command=toggle_password
            )
            showpasswordButton.grid(row=0, column=0, pady=5, padx=8)

            changeLoginButton = tk.Button(
                loginButtonFrame,
                font=("titillium web semibold", 9),
                text="Change Login Data",
                bg=colors["button"],
                fg=colors["bg"],
                # padx= 15,
                bd=0,
                width=18,
                command=changeLoginData
            )
            changeLoginButton.grid(row=0, column=1, pady=5, padx=8)

            recipientFrame = tk.LabelFrame(
                sender_frame,
                text="Recipient Email",
                font=("titillium web regular", 14),
                bg=colors["bg"],
                fg=colors["font"],
                bd=0,
            )
            recipientFrame.pack(padx=10, ipady=15, fill="x")
            recipientFrame.columnconfigure(0, weight=1)
            recipientLabel = tk.Label(
                recipientFrame,
                text="To",
                font=("titillium web light", 10),
                bg=colors["bg"],
                fg=colors["font"],
            )
            recipientLabel.grid(row=0, column=0, padx=10, pady=(20, 10), sticky="w")
            recipientEntry = tk.Entry(
                recipientFrame,
                font=("titillium web light", 10),
                bg=colors["entry"],
                fg=colors["font"],
                width=45,
                insertbackground=colors["font"],  # color del cursor
            )
            recipientEntry.grid(row=0, column=1, padx=8, pady=(20, 0), sticky="w")
            messageLabel = tk.Label(
                recipientFrame,
                text="Message",
                font=("titillium web light", 10),
                bg=colors["bg"],
                fg=colors["font"],
            )
            messageLabel.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="w")
            messageTextarea = tk.Text(
                recipientFrame,
                font=("titillium web extralight", 10),
                bg=colors["entry"],
                fg=colors["font"],
                # bd=0,
                insertbackground=colors["font"],
                width=200,
                height=10,
            )
            messageTextarea.grid(
                row=2, column=0, pady=(0, 15), columnspan=2, sticky="we"
            )
            messageTextarea.configure(state="normal")
            messageTextarea.delete(1.0, tk.END)
            messageTextarea.insert(tk.END, textarea.get(1.0, tk.END).replace("=", ""))
            messageTextarea.configure(state="disabled")
            buttonsFrame = tk.Frame(
                recipientFrame,
                bg=colors["bg"],
                # bg="red",
            )
            buttonsFrame.grid(row=3, column=0, columnspan=2, sticky="we")
            buttonsFrame.columnconfigure(0, weight=1)
            buttonsFrame.columnconfigure(1, weight=1)

            # Send Email Button
            sendEmailButton = tk.Button(
                buttonsFrame,
                font=("titillium web semibold", 11),
                text="Send Email",
                bg=colors["button"],
                fg=colors["bg"],
                # padx= 15,
                bd=0,
                width=12,
                command=send_email,
            )
            sendEmailButton.grid(row=0, column=0, pady=5, padx=8, sticky="e")

            # Cancel Button
            cancelButton = tk.Button(
                buttonsFrame,
                font=("titillium web semibold", 11),
                text="Cancel",
                bg=colors["button"],
                fg=colors["bg"],
                # padx= 15,
                bd=0,
                width=12,
                command=root1.destroy,
            )
            cancelButton.grid(row=0, column=1, pady=5, padx=8, sticky="w")

    def clean_fields(self):
        
        # Customer data inputs
        self.nameEntry.delete(0,tk.END)
        self.emailEntry.delete(0,tk.END)
        self.phoneEntry.delete(0,tk.END)
        self.billEntry.delete(0,tk.END)
        self.addressEntry.delete(0,tk.END)
        self.zipEntry.delete(0,tk.END)
        self.cityEntry.delete(0,tk.END)
        self.countryEntry.delete(0,tk.END)

        # Products Data inputs
        for category, products in self.entries.items():
            for product, entry in products.items():
                entry.delete(0, tk.END)  # Borrar el contenido actual de la Entry
                entry.insert(0, "0")   # Insertar el nuevo valor "0,0"
        self.textarea.config(state='normal')
        self.textarea.delete(1.0,tk.END)
        self.textarea.config(state='disabled')

        # Bill Menu entries
        self.cosmeticPriceEntry.delete(0,tk.END)
        self.groceriesPriceEntry.delete(0,tk.END)
        self.drinksPricesEntry.delete(0,tk.END)
        self.cosmeticTaxesEntry.delete(0,tk.END)
        self.groceriesTaxesEntry.delete(0,tk.END)
        self.drinksTaxesEntry.delete(0,tk.END)
        print('Cleaned!')


# https://youtu.be/e7eRonTN8DI?si=ffABEqhM6nHo0IN3
# Developed by David Castagneto, version 1.0
