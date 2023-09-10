import tkinter as tk
from palette import get_colors


# Importar colores
colors = get_colors()


def create_customer_frame_top(parent):
    # LabelFrame de cliente = tk.LabelFrame()
    customer_details_frame_top = tk.LabelFrame(
        parent,
        text="Customer Details",
        font=("titillium web regular", 14),
        bg=colors["bg"],
        fg=colors["font"],
        pady=5,
        bd=0
    )
    customer_details_frame_top.pack(fill="x", padx=10)

    # # Configura las columnas del contenedor padre para que se distribuyan equitativamente
    for col in range(4):
        customer_details_frame_top.columnconfigure(col, weight=1)

    # # Configura las filas del contenedor padre para que se distribuyan equitativamente
    for row in range(2):
        customer_details_frame_top.rowconfigure(row, weight=1)


        
    # Contenedor Entrada Nombre
    name_details_frame = tk.Frame(customer_details_frame_top, bg=colors["bg"])
    name_details_frame.grid(
        row=0,
        column=0,
        sticky="w"
    )

    # Contenedor Entrada Email
    email_details_frame = tk.Frame(customer_details_frame_top, bg=colors["bg"])
    email_details_frame.grid(
        row=0,
        column=1,
        sticky="nsew"
    )

    # Contenedor Entrada Telefono
    phone_details_frame = tk.Frame(customer_details_frame_top, bg=colors["bg"])
    phone_details_frame.grid(
        row=0,
        column=2,
        sticky="nsew"
    )

    # Contenedor Entrada Factura
    invoice_details_frame = tk.Frame(customer_details_frame_top, bg=colors["bg"])
    invoice_details_frame.grid(
        row=0,
        column=3,
        sticky="nsew"
    )

    # Contenedor Entrada Direccion
    address_details_frame = tk.Frame(customer_details_frame_top, bg=colors["bg"])
    address_details_frame.grid(
        row=1,
        column=0,
        sticky="w"
    )

    # Contenedor Entrada Codigo Postal
    zip_details_frame = tk.Frame(customer_details_frame_top, bg=colors["bg"])
    zip_details_frame.grid(
        row=1,
        column=1,
        sticky="e"
    )

    # Contenedor Entrada Provincia
    city_details_frame = tk.Frame(customer_details_frame_top, bg=colors["bg"])
    city_details_frame.grid(
        row=1,
        column=2,
        sticky="e"
    )

    # Contenedor Entrada Pais
    country_details_frame = tk.Frame(customer_details_frame_top, bg=colors["bg"])
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
    nameEntry = tk.Entry(
        name_details_frame,
        font=("titillium web light", 10),
        bg=colors["entry"],
        fg=colors["font"],
        width=28,
        insertbackground=colors['font'],  # color del cursor
        # bd=0,  # remover borde
        # highlightthickness=0,  # remover highlight
    )
    nameEntry.grid(row=0, column=1, padx=6, pady=6, sticky="e")

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
    emailEntry = tk.Entry(
        email_details_frame,
        font=("titillium web light", 10),
        bg=colors["entry"],
        fg=colors["font"],
        width=32,
        # bd=0,  # remover borde
        # highlightthickness=0,  # remover highlight
        insertbackground="gray",  # color del cursor
    )
    emailEntry.grid(row=0, column=1, padx=6)

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
    phoneEntry = tk.Entry(
        phone_details_frame,
        font=("titillium web light", 10),
        bg=colors["entry"],
        fg=colors["font"],
        width=15,
        # bd=0,  # remover borde
        # highlightthickness=0,  # remover highlight
        insertbackground="gray",  # color del cursor
    )
    phoneEntry.grid(row=0, column=1, padx=6)

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
    billEntry = tk.Entry(
        invoice_details_frame,
        font=("titillium web light", 10),
        bg=colors["entry"],
        fg=colors["font"],
        width=20,
        # bd=0,  # remover borde
        # highlightthickness=0,  # remover highlight
        insertbackground="gray",  # color del cursor
    )
    billEntry.grid(row=0, column=1, padx=6)

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
    addressEntry = tk.Entry(
        address_details_frame,
        font=("titillium web light", 10),
        bg=colors["entry"],
        fg=colors["font"],
        width=44,
        # bd=0,  # remover borde
        # highlightthickness=0,  # remover highlight
        insertbackground="gray",  # color del cursor
    )
    addressEntry.grid(row=0, column=1, padx=6, pady=6)

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
    cityEntry = tk.Entry(
        city_details_frame,
        font=("titillium web light", 10),
        bg=colors["entry"],
        fg=colors["font"],
        width=16,
        # bd=0,  # remover borde
        # highlightthickness=0,  # remover highlight
        insertbackground="gray",  # color del cursor
    )
    cityEntry.grid(row=0, column=1, padx=6, pady=6)

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
    zipEntry = tk.Entry(
        zip_details_frame,
        font=("titillium web light", 10),
        bg=colors["entry"],
        fg=colors["font"],
        width=12,
        # bd=0,  # remover borde
        # highlightthickness=0,  # remover highlight
        insertbackground="gray",  # color del cursor
    )
    zipEntry.grid(row=0, column=1, padx=6, pady=6)

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
    countryEntry = tk.Entry(
        country_details_frame,
        font=("titillium web light", 10),
        bg=colors["entry"],
        fg=colors["font"],
        width=16,
        # bd=0,  # remover borde
        # highlightthickness=0,  # remover highlight
        insertbackground="gray",  # color del cursor
    )
    countryEntry.grid(row=0, column=1, padx=6, pady=6)

    # Boton de busqueda = tk.Button()
    searchButton = tk.Button(
        customer_details_frame_top,
        text="Search",
        font=("titillium web bold", 10),
        bg=colors['button'],
        fg=colors["bg"],
        padx=20,
        bd=0,
    )
    searchButton.grid(row=0, column=5, padx=10, sticky='nse')

    return customer_details_frame_top
