import tkinter as tk
from palette import get_colors
from productsFrame import ProductFrame, BillingSearch
import ttkbootstrap as ttk
from ttkbootstrap.constants import *



# Importar colores
colors = get_colors()


class CustomerFrame:
    def __init__(self, parent, product_frame=None):
        self.nameEntry = tk.Entry(parent)
        self.emailEntry = tk.Entry(parent)
        self.phoneEntry = tk.Entry(parent)
        self.billEntry = tk.Entry(parent)
        self.addressEntry = tk.Entry(parent)
        self.cityEntry = tk.Entry(parent)
        self.zipEntry = tk.Entry(parent)
        self.countryEntry = tk.Entry(parent)
        self.frame = self.create_customer_frame_top(parent)

        self.product_frame = product_frame

        # crea el frame ProductFrame
        self.product_frame = ProductFrame(parent, product_frame)

    def create_customer_frame_top(self, parent):
        # texarea = ProductFrame.textarea

        # Crea una instancia de Style
        # style = ttk.Style(parent)

        # Customize Fonts
        custom_font_LabelFrame = ('titillium web regular', 14)
        custom_font_Entry = ('titillium web light', 10)

        # LabelFrame de cliente = tk.LabelFrame()
        customerFrame = ttk.Labelframe(
            parent,
            text="Customer Details",
            bootstyle="default",
        )
        customerFrame.pack(fill="x", padx=10)

        # # Configura las columnas del contenedor padre para que se distribuyan equitativamente
        for col in range(4):
            customerFrame.columnconfigure(col, weight=1)

        # # Configura las filas del contenedor padre para que se distribuyan equitativamente
        for row in range(2):
            customerFrame.rowconfigure(row, weight=1)

        # Contenedor Entrada Nombre
        name_details_frame = tk.Frame(customerFrame, bg=colors["bg"])
        name_details_frame.grid(row=0, column=0, sticky="w")

        # Contenedor Entrada Email
        email_details_frame = tk.Frame(customerFrame, bg=colors["bg"])
        email_details_frame.grid(row=0, column=1, sticky="w")

        # Contenedor Entrada Telefono
        phone_details_frame = tk.Frame(customerFrame, bg=colors["bg"])
        phone_details_frame.grid(row=0, column=2, sticky="w")

        # Contenedor Entrada Factura
        invoice_details_frame = tk.Frame(customerFrame, bg=colors["bg"])
        invoice_details_frame.grid(row=0, column=3, sticky="w")

        # Contenedor Entrada Direccion
        address_details_frame = tk.Frame(customerFrame, bg=colors["bg"])
        address_details_frame.grid(row=1, column=0, sticky="w", pady=(0, 7))

        # Contenedor Entrada Codigo Postal
        zip_details_frame = tk.Frame(customerFrame, bg=colors["bg"])
        zip_details_frame.grid(row=1, column=1, sticky="e", pady=(0, 7))

        # Contenedor Entrada Provincia
        city_details_frame = tk.Frame(customerFrame, bg=colors["bg"])
        city_details_frame.grid(row=1, column=2, sticky="e", pady=(0, 7))

        # Contenedor Entrada Pais
        country_details_frame = tk.Frame(customerFrame, bg=colors["bg"])
        country_details_frame.grid(row=1, column=3, columnspan=2, sticky="e", pady=(0, 7))

        # Nombre del cliente = ttk.Label()
        nameLabel = ttk.Label(
            name_details_frame,
            text="Name",
            font=custom_font_Entry,
        )
        nameLabel.grid(row=0, column=0, padx=10)

        # NameInputField = ttk.Entry()
        self.nameEntry = tk.Entry(
            name_details_frame,
            font=custom_font_Entry,
            width=28,
        )
        self.nameEntry.grid(row=0, column=1, padx=6, sticky="e")

        # Email del cliente = ttk.Label()
        emailLabel = ttk.Label(
            email_details_frame,
            text="Email",
            font=custom_font_Entry,
        )
        emailLabel.grid(row=0, column=0, padx=10)

        # EmailInputField = ttk.Entry()
        self.emailEntry = tk.Entry(
            email_details_frame,
            font=custom_font_Entry,
            width=32,
        )
        self.emailEntry.grid(row=0, column=1, padx=6)

        # Telefono del cliente, Label
        phoneLabel = ttk.Label(
            phone_details_frame,
            text="Phone",
            font=custom_font_Entry,
        )
        phoneLabel.grid(row=0, column=0, padx=10)

        # PhoneInputField = ttk.Entry()
        self.phoneEntry = tk.Entry(
            phone_details_frame,
            font=custom_font_Entry,
        )
        self.phoneEntry.grid(row=0, column=1, padx=6)

        # Factura del cliente, Label
        billLabel = ttk.Label(
            invoice_details_frame,
            text="Invoice number",
            font=custom_font_Entry
        )
        billLabel.grid(row=0, column=0, padx=10)

        # BillInputField = ttk.Entry()
        self.billEntry = tk.Entry(
            invoice_details_frame,
            font=custom_font_Entry
        )
        self.billEntry.grid(row=0, column=1, padx=6)

        # Dirección del cliente, Label
        addressLabel = ttk.Label(
            address_details_frame,
            text="Address",
            font=custom_font_Entry
        )
        addressLabel.grid(row=0, column=0, padx=10)

        # addressInputField = ttk.Entry()
        self.addressEntry = tk.Entry(
            address_details_frame,
            font=custom_font_Entry
        )
        self.addressEntry.grid(row=0, column=1, padx=6, pady=6)

        # Ciudad del cliente, Label
        cityLabel = ttk.Label(
            city_details_frame,
            text="City",
            font=custom_font_Entry
        )
        cityLabel.grid(row=0, column=0, padx=10)

        # CityInputField = ttk.Entry()
        self.cityEntry = tk.Entry(
            city_details_frame,
            font=custom_font_Entry
        )
        self.cityEntry.grid(row=0, column=1, padx=6, pady=6)

        # CP del cliente, Label
        zipLabel = ttk.Label(
            zip_details_frame,
            text="Zip",
            font=custom_font_Entry
        )
        zipLabel.grid(row=0, column=0, padx=10)

        # ZipInputField = ttk.Entry()
        self.zipEntry = tk.Entry(
            zip_details_frame,
            font=custom_font_Entry
        )
        self.zipEntry.grid(row=0, column=1, padx=6, pady=6)

        # Pais del cliente, Label
        countryLabel = ttk.Label(
            country_details_frame,
            text="Country",
            font=custom_font_Entry
        )
        countryLabel.grid(row=0, column=0, padx=10)

        # CountryInputField = ttk.Entry()
        self.countryEntry = tk.Entry(
            country_details_frame,
            font=custom_font_Entry
        )
        self.countryEntry.grid(row=0, column=1, padx=6, pady=6)

        # Creando instancia de la clase BillingSearch
        billing_instance = BillingSearch(
            self.nameEntry,
            self.emailEntry,
            self.phoneEntry,
            self.billEntry,
            self.addressEntry,
            self.cityEntry,
            self.zipEntry,
            self.countryEntry,
        )

        # Boton de busqueda = tk.Button()
        # searchButton = tk.Button(
        #     customerFrame,
        #     text="Search",
        #     font=("titillium web bold", 10),
        #     bg=colors["button"],
        #     fg=colors["bg"],
        #     padx=20,
        #     bd=0,
        #     command=billing_instance.searchBill,
        # )
        # searchButton.grid(row=0, column=5, padx=10, sticky="nse")

        b1 = ttk.Button(
            customerFrame,
            text="Search",
            bootstyle=PRIMARY,
            command=billing_instance.searchBill,
        )
        b1.grid(row=0, column=6, padx=5, pady=10, sticky="nse")

        # b2 = ttk.Button(customerFrame, text="Button 2", bootstyle=(INFO, OUTLINE))
        # b2.pack(side=LEFT, padx=5, pady=10)


        return customerFrame


# Developed by David Castagneto, version 1.0
