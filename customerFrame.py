import tkinter as tk
from palette import get_colors
import os
from billing_app import BillingSearch
from productsFrame import ProductFrame


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
        # self.product_frame = ProductFrame(parent)

    def create_customer_frame_top(self, parent):
        # texarea = productFrame.textarea
        
        # LabelFrame de cliente = tk.LabelFrame()
        customerFrame = tk.LabelFrame(
            parent,
            text="Customer Details",
            font=("titillium web regular", 14),
            bg=colors["bg"],
            fg=colors["font"],
            pady=5,
            bd=0
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
        name_details_frame.grid(
            row=0,
            column=0,
            sticky="w"
        )

        # Contenedor Entrada Email
        email_details_frame = tk.Frame(customerFrame, bg=colors["bg"])
        email_details_frame.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        # Contenedor Entrada Telefono
        phone_details_frame = tk.Frame(customerFrame, bg=colors["bg"])
        phone_details_frame.grid(
            row=0,
            column=2,
            sticky="nsew"
        )

        # Contenedor Entrada Factura
        invoice_details_frame = tk.Frame(customerFrame, bg=colors["bg"])
        invoice_details_frame.grid(
            row=0,
            column=3,
            sticky="nsew"
        )

        # Contenedor Entrada Direccion
        address_details_frame = tk.Frame(customerFrame, bg=colors["bg"])
        address_details_frame.grid(
            row=1,
            column=0,
            sticky="w"
        )

        # Contenedor Entrada Codigo Postal
        zip_details_frame = tk.Frame(customerFrame, bg=colors["bg"])
        zip_details_frame.grid(
            row=1,
            column=1,
            sticky="e"
        )

        # Contenedor Entrada Provincia
        city_details_frame = tk.Frame(customerFrame, bg=colors["bg"])
        city_details_frame.grid(
            row=1,
            column=2,
            sticky="e"
        )

        # Contenedor Entrada Pais
        country_details_frame = tk.Frame(customerFrame, bg=colors["bg"])
        country_details_frame.grid(
            row=1,
            column=3,
            columnspan=2,
            sticky="e"
        )

        # Nombre del cliente = tk.Label()
        nameLabel = tk.Label(
            name_details_frame,
            text="Name",
            font=("titillium web light", 10),
            bg=colors["bg"],
            fg=colors["font"],
        )
        nameLabel.grid(row=0, column=0, padx=10)
        
        # NameInputField = tk.Entry()
        self.nameEntry = tk.Entry(
            name_details_frame,
            font=("titillium web light", 10),
            bg=colors["entry"],
            fg=colors["font"],
            width=28,
            insertbackground=colors['font'],  # color del cursor
            # bd=0,  # remover borde
            # highlightthickness=0,  # remover highlight
        )
        self.nameEntry.grid(row=0, column=1, padx=6, pady=6, sticky="e")

        # Email del cliente = tk.Label()
        emailLabel = tk.Label(
            email_details_frame,
            text="Email",
            font=("titillium web light", 10),
            bg=colors["bg"],
            fg=colors["font"],
        )
        emailLabel.grid(row=0, column=0, padx=10)

        # EmailInputField = tk.Entry()
        self.emailEntry = tk.Entry(
            email_details_frame,
            font=("titillium web light", 10),
            bg=colors["entry"],
            fg=colors["font"],
            width=32,
            # bd=0,  # remover borde
            # highlightthickness=0,  # remover highlight
            insertbackground="gray",  # color del cursor
        )
        self.emailEntry.grid(row=0, column=1, padx=6)

        # Telefono del cliente, Label
        phoneLabel = tk.Label(
            phone_details_frame,
            text="Phone",
            font=("titillium web light", 10),
            bg=colors["bg"],
            fg=colors["font"],
        )
        phoneLabel.grid(row=0, column=0, padx=10)

        # PhoneInputField = tk.Entry()
        self.phoneEntry = tk.Entry(
            phone_details_frame,
            font=("titillium web light", 10),
            bg=colors["entry"],
            fg=colors["font"],
            width=15,
            # bd=0,  # remover borde
            # highlightthickness=0,  # remover highlight
            insertbackground="gray",  # color del cursor
        )
        self.phoneEntry.grid(row=0, column=1, padx=6)

        # Factura del cliente, Label
        billLabel = tk.Label(
            invoice_details_frame,
            text="Invoice number",
            font=("titillium web light", 10),
            bg=colors["bg"],
            fg=colors["font"],
        )
        billLabel.grid(row=0, column=0, padx=10)

        # BillInputField = tk.Entry()
        self.billEntry = tk.Entry(
            invoice_details_frame,
            font=("titillium web light", 10),
            bg=colors["entry"],
            fg=colors["font"],
            width=20,
            # bd=0,  # remover borde
            # highlightthickness=0,  # remover highlight
            insertbackground="gray",  # color del cursor
        )
        self.billEntry.grid(row=0, column=1, padx=6)

        # Dirección del cliente, Label
        addressLabel = tk.Label(
            address_details_frame,
            text="Address",
            font=("titillium web light", 10),
            bg=colors["bg"],
            fg=colors["font"],
        )
        addressLabel.grid(row=0, column=0, padx=10)

        # addressInputField = tk.Entry()
        self.addressEntry = tk.Entry(
            address_details_frame,
            font=("titillium web light", 10),
            bg=colors["entry"],
            fg=colors["font"],
            width=44,
            # bd=0,  # remover borde
            # highlightthickness=0,  # remover highlight
            insertbackground="gray",  # color del cursor
        )
        self.addressEntry.grid(row=0, column=1, padx=6, pady=6)

        # Ciudad del cliente, Label
        cityLabel = tk.Label(
            city_details_frame,
            text="City",
            font=("titillium web light", 10),
            bg=colors["bg"],
            fg=colors["font"],
        )
        cityLabel.grid(row=0, column=0, padx=10)

        # CityInputField = tk.Entry()
        self.cityEntry = tk.Entry(
            city_details_frame,
            font=("titillium web light", 10),
            bg=colors["entry"],
            fg=colors["font"],
            width=16,
            # bd=0,  # remover borde
            # highlightthickness=0,  # remover highlight
            insertbackground="gray",  # color del cursor
        )
        self.cityEntry.grid(row=0, column=1, padx=6, pady=6)

        # CP del cliente, Label
        zipLabel = tk.Label(
            zip_details_frame,
            text="Zip",
            font=("titillium web light", 10),
            bg=colors["bg"],
            fg=colors["font"],
        )
        zipLabel.grid(row=0, column=0, padx=10)

        # ZipInputField = tk.Entry()
        self.zipEntry = tk.Entry(
            zip_details_frame,
            font=("titillium web light", 10),
            bg=colors["entry"],
            fg=colors["font"],
            width=12,
            # bd=0,  # remover borde
            # highlightthickness=0,  # remover highlight
            insertbackground="gray",  # color del cursor
        )
        self.zipEntry.grid(row=0, column=1, padx=6, pady=6)

        # Pais del cliente, Label
        countryLabel = tk.Label(
            country_details_frame,
            text="Country",
            font=("titillium web light", 10),
            bg=colors["bg"],
            fg=colors["font"],
        )
        countryLabel.grid(row=0, column=0, padx=10)

        # CountryInputField = tk.Entry()
        self.countryEntry = tk.Entry(
            country_details_frame,
            font=("titillium web light", 10),
            bg=colors["entry"],
            fg=colors["font"],
            width=16,
            # bd=0,  # remover borde
            # highlightthickness=0,  # remover highlight
            insertbackground="gray",  # color del cursor
        )
        self.countryEntry.grid(row=0, column=1, padx=6, pady=6)

        # Creando instancia de la clase BillingSearch
        billing_instance = BillingSearch(self.nameEntry, self.emailEntry, self.phoneEntry, self.billEntry, self.addressEntry, self.cityEntry, self.zipEntry, self.countryEntry)

        # Boton de busqueda = tk.Button()
        searchButton = tk.Button(
            customerFrame,
            text="Search",
            font=("titillium web bold", 10),
            bg=colors['button'],
            fg=colors["bg"],
            padx=20,
            bd=0,

            command=billing_instance.searchBill
        )
        searchButton.grid(row=0, column=5, padx=10, sticky='nse')

        return customerFrame
