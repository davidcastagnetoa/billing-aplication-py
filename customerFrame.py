import tkinter as tk


def create_customer_frame_top(parent):
    # LabelFrame de cliente = tk.LabelFrame()
    customer_details_frame_top = tk.LabelFrame(
        parent,
        text="Customer Details",
        font=("titillium web regular", 14),
        bg="#101214",
        fg="white",
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



    # # Configurando las columnas para que se expandan de manera uniforme
    # for i in range(4):
    #     customer_details_frame_top.columnconfigure(i, weight=1)
    # customer_details_frame_top.columnconfigure(4, weight=0)

    # # Dado que tienes dos filas, también debes configurarlas para que se expandan uniformemente si es necesario
    # customer_details_frame_top.rowconfigure(0, weight=1)
    # customer_details_frame_top.rowconfigure(1, weight=1)


        
    # Contenedor Entrada Nombre
    name_details_frame = tk.Frame(customer_details_frame_top, bg="#101214")
    name_details_frame.grid(
        row=0,
        column=0,
        sticky="w"
    )

    # Contenedor Entrada Email
    email_details_frame = tk.Frame(customer_details_frame_top, bg="#101214")
    email_details_frame.grid(
        row=0,
        column=1,
        sticky="nsew"
    )

    # Contenedor Entrada Telefono
    phone_details_frame = tk.Frame(customer_details_frame_top, bg="#101214")
    phone_details_frame.grid(
        row=0,
        column=2,
        sticky="nsew"
    )

    # Contenedor Entrada Factura
    invoice_details_frame = tk.Frame(customer_details_frame_top, bg="#101214")
    invoice_details_frame.grid(
        row=0,
        column=3,
        sticky="nsew"
    )

    # Contenedor Entrada Direccion
    address_details_frame = tk.Frame(customer_details_frame_top, bg="#101214")
    address_details_frame.grid(
        row=1,
        column=0,
        sticky="w"
    )

    # Contenedor Entrada Codigo Postal
    zip_details_frame = tk.Frame(customer_details_frame_top, bg="#101214")
    zip_details_frame.grid(
        row=1,
        column=1,
        sticky="e"
    )

    # Contenedor Entrada Provincia
    city_details_frame = tk.Frame(customer_details_frame_top, bg="#101214")
    city_details_frame.grid(
        row=1,
        column=2,
        sticky="e"
    )

    # Contenedor Entrada Pais
    country_details_frame = tk.Frame(customer_details_frame_top, bg="#101214")
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
        bg="#101214",
        fg="white",
    )
    nameLabel.grid(row=0, column=0, padx=10)
    # NameInputField = tk.Entry()
    nameEntry = tk.Entry(
        name_details_frame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
        width=28,
        insertbackground="gray",  # color del cursor
        # bd=0,  # remover borde
        # highlightthickness=0,  # remover highlight
    )
    nameEntry.grid(row=0, column=1, padx=6, pady=6, sticky="e")

    # Email del cliente = tk.Label()
    emailLabel = tk.Label(
        email_details_frame,
        text="Email",
        font=("titillium web light", 10),
        bg="#101214",
        fg="white",
    )
    emailLabel.grid(row=0, column=0, padx=10)

    # EmailInputField = tk.Entry()
    emailEntry = tk.Entry(
        email_details_frame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
        width=32,
        # bd=0,  # remover borde
        # highlightthickness=0,  # remover highlight
        insertbackground="gray",  # color del cursor
    )
    emailEntry.grid(row=0, column=1, padx=6)

    # Telefono del cliente, Label
    phoneLabel = tk.Label(
        phone_details_frame,
        text="Teléfono",
        font=("titillium web light", 10),
        bg="#101214",
        fg="white",
    )
    phoneLabel.grid(row=0, column=0, padx=10)

    # PhoneInputField = tk.Entry()
    phoneEntry = tk.Entry(
        phone_details_frame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
        width=15,
        # bd=0,  # remover borde
        # highlightthickness=0,  # remover highlight
        insertbackground="gray",  # color del cursor
    )
    phoneEntry.grid(row=0, column=1, padx=6)

    # Factura del cliente, Label
    billLabel = tk.Label(
        invoice_details_frame,
        text="Número de Factura",
        font=("titillium web light", 10),
        bg="#101214",
        fg="white",
    )
    billLabel.grid(row=0, column=0, padx=10)

    # BillInputField = tk.Entry()
    billEntry = tk.Entry(
        invoice_details_frame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
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
        bg="#101214",
        fg="white",
    )
    addressLabel.grid(row=0, column=0, padx=10)

    # addressInputField = tk.Entry()
    addressEntry = tk.Entry(
        address_details_frame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
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
        bg="#101214",
        fg="white",
    )
    cityLabel.grid(row=0, column=0, padx=10)

    # CityInputField = tk.Entry()
    cityEntry = tk.Entry(
        city_details_frame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
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
        bg="#101214",
        fg="white",
    )
    zipLabel.grid(row=0, column=0, padx=10)

    # ZipInputField = tk.Entry()
    zipEntry = tk.Entry(
        zip_details_frame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
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
        bg="#101214",
        fg="white",
    )
    countryLabel.grid(row=0, column=0, padx=10)

    # CountryInputField = tk.Entry()
    countryEntry = tk.Entry(
        country_details_frame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
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
        font=("titillium web semibold", 8),
        bg="#282e32",
        fg="white",
        padx=12,
        bd=0,
    )
    searchButton.grid(row=0, column=4, padx=20)

    return customer_details_frame_top


def create_customer_frame_bottom(parent):
    customer_details_frame_bottom = tk.LabelFrame(
        parent,
        # text="Customer Details",
        # font=("titillium web regular", 14),
        bg="#101214",
        # fg="white",
        # pady=5,
        bd=0
    )
    customer_details_frame_bottom.pack(fill="x", padx=10)

    # Contenedor Entrada Direccion
    address_details_frame = tk.Frame(
        customer_details_frame_bottom, bg="#101214")
    address_details_frame.grid(
        row=1,
        column=0,
        sticky="w"
    )

    # Dirección del cliente, Label
    addressLabel = tk.Label(
        address_details_frame,
        text="Address",
        font=("titillium web light", 10),
        bg="#101214",
        fg="white",
    )
    addressLabel.grid(row=0, column=0, padx=10)

    # AddressInputField = tk.Entry()
    addressEntry = tk.Entry(
        address_details_frame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
        width=44,
        # bd=0,  # remover borde
        # highlightthickness=0,  # remover highlight
        insertbackground="gray",  # color del cursor
    )
    addressEntry.grid(row=0, column=1, padx=6)

    return customer_details_frame_bottom
