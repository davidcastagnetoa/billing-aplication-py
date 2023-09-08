import tkinter as tk


def main():
    # Ventana
    root = tk.Tk()
    root.title("Retail Billing System")

    root.iconbitmap("static/icon.ico")
    root.geometry("1280x720")
    root.minsize(1138, 500)

    # Cabecera título = Label()
    headingLabel = tk.Label(
        root,
        text="Retail Billing System",
        font=("titillium web light", 16),
        bg="#101214",
        fg="white",
    )
    headingLabel.pack(padx=0, pady=0, ipadx=10, ipady=10, fill="x")

    # Panel de cliente = tk.LabelFrame()
    customer_details_frame = tk.LabelFrame(
        root,
        text="Customer Details",
        font=("titillium web extralight", 13),
        bg="#101214",
        fg="white",
        pady=5,
    )
    customer_details_frame.pack(fill="x")

    # Contenedor Entrada Nombre
    name_details_frame = tk.Frame(customer_details_frame, bg="#101214")
    name_details_frame.grid(
        row=0,
        column=0,
    )

    # Contenedor Entrada Email
    email_details_frame = tk.Frame(customer_details_frame, bg="#101214")
    email_details_frame.grid(
        row=0,
        column=1,
    )

    # Contenedor Entrada Telefono
    phone_details_frame = tk.Frame(customer_details_frame, bg="#101214")
    phone_details_frame.grid(
        row=0,
        column=2,
    )

    # Contenedor Entrada Factura
    invoice_details_frame = tk.Frame(customer_details_frame, bg="#101214")
    invoice_details_frame.grid(
        row=0,
        column=3,
    )

    # Configurar la columnas para que consuma espacio extra (simular space-between)
    # customer_details_frame.grid_columnconfigure(0, weight=1)
    customer_details_frame.grid_columnconfigure(1, weight=1)
    customer_details_frame.grid_columnconfigure(2, weight=1)
    customer_details_frame.grid_columnconfigure(3, weight=1)
    # customer_details_frame.grid_columnconfigure(4, weight=1)

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
    nameEntry.grid(row=0, column=1, padx=6, pady=6)

    # Email del cliente = tk.Label()
    emailLabel = tk.Label(
        email_details_frame,
        text="Email",
        font=("titillium web light", 10),
        bg="#101214",
        fg="white",
    )
    emailLabel.grid(row=0, column=2, padx=10)

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
    emailEntry.grid(row=0, column=3, padx=6, pady=6)

    # Telefono del cliente, Label
    phoneLabel = tk.Label(
        phone_details_frame,
        text="Teléfono",
        font=("titillium web light", 10),
        bg="#101214",
        fg="white",
    )
    phoneLabel.grid(row=0, column=4, padx=10)

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
    phoneEntry.grid(row=0, column=5, padx=6, pady=6)

    # Factura del cliente, Label
    billLabel = tk.Label(
        invoice_details_frame,
        text="Número de Factura",
        font=("titillium web light", 10),
        bg="#101214",
        fg="white",
    )
    billLabel.grid(row=0, column=6, padx=10)

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
    billEntry.grid(row=0, column=7, padx=6, pady=6)

    # Boton de busqueda = tk.Button()
    searchButton = tk.Button(
        customer_details_frame,
        text="Search",
        font=("titillium web semibold", 8),
        bg="#282e32",
        fg="white",
        padx=12,
        bd=0,
    )
    searchButton.grid(row=0, column=8, padx=20)

    # Panel de Productos
    productFrame = tk.Frame(root)
    productFrame.pack()

    # Columnas

    # columna de Cosmeticos
    cosmeticsFrame = tk.LabelFrame(
        productFrame,
        text="Cosmetics",
        font=("titillium web extralight", 13),
        bg="#101214",
        fg="white",
        pady=10,
        padx=6,
    )
    cosmeticsFrame.grid(row=0, column=0)

    # Listado de cosmeticos
    # Jabon de baño = tk.Label()
    bathSoapLabel = tk.Label(
        cosmeticsFrame,
        text="Bath Soap",
        font=("titillium web light", 10),
        bg="#101214",
        fg="white",
    )
    bathSoapLabel.grid(row=0, column=0, padx=7, pady=5, sticky="w")

    # Jabon de baño = tk.Entry()
    bathSoapEntry = tk.Entry(
        cosmeticsFrame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
        width=8,
        insertbackground="gray",
    )
    bathSoapEntry.grid(row=0, column=1, padx=9, pady=5)

    # Crema de cara = tk.Label()
    faceCreamLabel = tk.Label(
        cosmeticsFrame,
        text="Face Cream",
        font=("titillium web light", 10),
        bg="#101214",
        fg="white",
    )
    faceCreamLabel.grid(row=1, column=0, padx=7, pady=5, sticky="w")

    # Crema de cara = tk.Entry()
    faceCreamEntry = tk.Entry(
        cosmeticsFrame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
        width=8,
        insertbackground="gray",
    )
    faceCreamEntry.grid(row=1, column=1, padx=9, pady=5)

    # Jabon de cara = tk.Label()
    faceWashLabel = tk.Label(
        cosmeticsFrame,
        text="Face Wash",
        font=("titillium web light", 10),
        bg="#101214",
        fg="white",
    )
    faceWashLabel.grid(row=2, column=0, padx=7, pady=5, sticky="w")

    # Jabon de cara = tk.Entry()
    faceWashEntry = tk.Entry(
        cosmeticsFrame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
        width=8,
        insertbackground="gray",
    )
    faceWashEntry.grid(row=2, column=1, padx=9, pady=5)

    # Spray de pelo = tk.Label()
    hairSprayLabel = tk.Label(
        cosmeticsFrame,
        text="Hair Spray",
        font=("titillium web light", 10),
        bg="#101214",
        fg="white",
    )
    hairSprayLabel.grid(row=3, column=0, padx=7, pady=5, sticky="w")

    # Spray de pelo = tk.Entry()
    hairSprayEntry = tk.Entry(
        cosmeticsFrame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
        width=8,
        insertbackground="gray",
    )
    hairSprayEntry.grid(row=3, column=1, padx=9, pady=5)

    # Gel de pelo = tk.Label()
    hairGelLabel = tk.Label(
        cosmeticsFrame,
        text="Har Gel",
        font=("titillium web light", 10),
        bg="#101214",
        fg="white",
    )
    hairGelLabel.grid(row=4, column=0, padx=7, pady=5, sticky="w")

    # Gel de pelo = tk.Entry()
    hairGelEntry = tk.Entry(
        cosmeticsFrame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
        width=8,
        insertbackground="gray",
    )
    hairGelEntry.grid(row=4, column=1, padx=9, pady=5)

    # Locion de cuerpo = tk.Label()
    lotionBodyLabel = tk.Label(
        cosmeticsFrame,
        text="Lotion Body",
        font=("titillium web light", 10),
        bg="#101214",
        fg="white",
    )
    lotionBodyLabel.grid(row=5, column=0, padx=7, pady=5)

    # Locion de cuerpo = tk.Entry()
    lotionBodyEntry = tk.Entry(
        cosmeticsFrame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
        width=8,
        insertbackground="gray",
    )
    lotionBodyEntry.grid(row=5, column=1, padx=9, pady=5)

    # columna de Comestibles
    groceryFrame = tk.LabelFrame(
        productFrame,
        text="Grocery",
        font=("titillium web extralight", 13),
        bg="#101214",
        fg="white",
        pady=10,
        padx=6,
    )
    groceryFrame.grid(row=0, column=1)

    # Listado de comestibles
    # Arroz = tk.Label()
    riceLabel = tk.Label(
        groceryFrame,
        text="Rice",
        font=("titillium web light", 10),
        bg="#101214",
        fg="white",
    )
    riceLabel.grid(row=0, column=0, padx=7, pady=5, sticky="w")

    # Arroz = tk.Entry()
    riceEntry = tk.Entry(
        groceryFrame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
        width=8,
        insertbackground="gray",
    )
    riceEntry.grid(row=0, column=1, padx=9, pady=5)

    # Oil = tk.Label()
    oilLabel = tk.Label(
        groceryFrame,
        text="Oil",
        font=("titillium web light", 10),
        bg="#101214",
        fg="white",
    )
    oilLabel.grid(row=1, column=0, padx=7, pady=5, sticky="w")

    # Oil = tk.Entry()
    oilEntry = tk.Entry(
        groceryFrame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
        width=8,
        insertbackground="gray",
    )
    oilEntry.grid(row=1, column=1, padx=9, pady=5)

    # Huevos = tk.Label()
    eggsLabel = tk.Label(
        groceryFrame,
        text="Egg",
        font=("titillium web light", 10),
        bg="#101214",
        fg="white",
    )
    eggsLabel.grid(row=2, column=0, padx=7, pady=5, sticky="w")

    # Huevos = tk.Entry()
    eggsEntry = tk.Entry(
        groceryFrame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
        width=8,
        insertbackground="gray",
    )
    eggsEntry.grid(row=2, column=1, padx=9, pady=5)

    # Sugar = tk.Label()
    sugarLabel = tk.Label(
        groceryFrame,
        text="Sugar",
        font=("titillium web light", 10),
        bg="#101214",
        fg="white",
    )
    sugarLabel.grid(row=3, column=0, padx=7, pady=5, sticky="w")

    # Sugar = tk.Entry()
    sugarEntry = tk.Entry(
        groceryFrame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
        width=8,
        insertbackground="gray",
    )
    sugarEntry.grid(row=3, column=1, padx=9, pady=5)

    # Te = tk.Label()
    teaLabel = tk.Label(
        groceryFrame,
        text="Tea",
        font=("titillium web light", 10),
        bg="#101214",
        fg="white",
    )
    teaLabel.grid(row=4, column=0, padx=7, pady=5, sticky="w")

    # Te = tk.Entry()
    teaEntry = tk.Entry(
        groceryFrame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
        width=8,
        insertbackground="gray",
    )
    teaEntry.grid(row=4, column=1, padx=9, pady=5)

    # Cinnamon = tk.Label()
    cinnamonLabel = tk.Label(
        groceryFrame,
        text="Sugar",
        font=("titillium web light", 10),
        bg="#101214",
        fg="white",
    )
    cinnamonLabel.grid(row=5, column=0, padx=7, pady=5, sticky="w")

    # Cinnamon = tk.Entry()
    cinnamonEntry = tk.Entry(
        groceryFrame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
        width=8,
        insertbackground="gray",
    )
    cinnamonEntry.grid(row=5, column=1, padx=9, pady=5)

    # columna de Bebidas
    drinksFrame = tk.LabelFrame(
        productFrame,
        text="Drinks",
        font=("titillium web extralight", 13),
        bg="#101214",
        fg="white",
        pady=10,
        padx=6,
    )
    drinksFrame.grid(row=0, column=2)

    # Listado de bebidas
    # Cerveza = tk.Label()
    beerLabel = tk.Label(
        drinksFrame,
        text="Beer",
        font=("titillium web light", 10),
        bg="#101214",
        fg="white",
    )
    beerLabel.grid(row=0, column=0, padx=7, pady=5, sticky="w")

    # Cerveza = tk.Entry()
    beerEntry = tk.Entry(
        drinksFrame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
        width=8,
        insertbackground="gray",
    )
    beerEntry.grid(row=0, column=1, padx=9, pady=5)

    # Soda = tk.Label()
    sodaLabel = tk.Label(
        drinksFrame,
        text="Soda",
        font=("titillium web light", 10),
        bg="#101214",
        fg="white",
    )
    sodaLabel.grid(row=1, column=0, padx=7, pady=5, sticky="w")

    # Soda = tk.Entry()
    sodaEntry = tk.Entry(
        drinksFrame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
        width=8,
        insertbackground="gray",
    )
    sodaEntry.grid(row=1, column=1, padx=9, pady=5)

    # Agua = tk.Label()
    waterLabel = tk.Label(
        drinksFrame,
        text="Water",
        font=("titillium web light", 10),
        bg="#101214",
        fg="white",
    )
    waterLabel.grid(row=2, column=0, padx=7, pady=5, sticky="w")

    # Agua = tk.Entry()
    waterEntry = tk.Entry(
        drinksFrame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
        width=8,
        insertbackground="gray",
    )
    waterEntry.grid(row=2, column=1, padx=9, pady=5)

    # Coffee = tk.Label()
    coffeeLabel = tk.Label(
        drinksFrame,
        text="Coffee",
        font=("titillium web light", 10),
        bg="#101214",
        fg="white",
    )
    coffeeLabel.grid(row=3, column=0, padx=7, pady=5, sticky="w")

    # Coffee = tk.Entry()
    coffeeEntry = tk.Entry(
        drinksFrame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
        width=8,
        insertbackground="gray",
    )
    coffeeEntry.grid(row=3, column=1, padx=9, pady=5)

    # Fanta = tk.Label()
    fantaLabel = tk.Label(
        drinksFrame,
        text="Fanta",
        font=("titillium web light", 10),
        bg="#101214",
        fg="white",
    )
    fantaLabel.grid(row=4, column=0, padx=7, pady=5, sticky="w")

    # Fanta = tk.Entry()
    fantaEntry = tk.Entry(
        drinksFrame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
        width=8,
        insertbackground="gray",
    )
    fantaEntry.grid(row=4, column=1, padx=9, pady=5)

    # Pepsy = tk.Label()
    pepsyLabel = tk.Label(
        drinksFrame,
        text="Pepsy",
        font=("titillium web light", 10),
        bg="#101214",
        fg="white",
    )
    pepsyLabel.grid(row=5, column=0, padx=7, pady=5, sticky="w")

    # Pepsy = tk.Entry()
    pepsyEntry = tk.Entry(
        drinksFrame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
        width=8,
        insertbackground="gray",
    )
    pepsyEntry.grid(row=5, column=1, padx=9, pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()
