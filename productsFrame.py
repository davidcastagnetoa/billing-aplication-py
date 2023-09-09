import tkinter as tk


def create_products_frame(parent):
    productFrame = tk.LabelFrame(
        parent,
        text="Products",
        font=("titillium web regular", 14),
        bg="#101214",
        fg="white",
        pady=5,
        bd=0,
    )
    productFrame.pack(fill="x", padx=10, pady=10)

    # productFrame.grid_columnconfigure(0, weight=1)
    productFrame.grid_columnconfigure(1, weight=1)
    productFrame.grid_columnconfigure(2, weight=1)
    # productFrame.grid_columnconfigure(3, weight=1)

    # Columnas
    # columna de Cosmeticos
    cosmeticsColumn = tk.Frame(productFrame, bg="#101214")
    cosmeticsColumn.grid(
        row=0,
        column=0,
        sticky="n"
    )

    cosmeticsFrame = tk.LabelFrame(
        cosmeticsColumn,
        text="Cosmetics",
        font=("titillium web extralight", 13),
        bg="#101214",
        fg="white",
        pady=10,
        padx=6,
        bd=0
    )
    cosmeticsFrame.pack(fill="x")

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
        width=15,
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
        width=15,
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
        width=15,
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
        width=15,
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
        width=15,
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
    lotionBodyLabel.grid(row=5, column=0, padx=7, pady=5, sticky="w")

    # Locion de cuerpo = tk.Entry()
    lotionBodyEntry = tk.Entry(
        cosmeticsFrame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
        width=15,
        insertbackground="gray",
    )
    lotionBodyEntry.grid(row=5, column=1, padx=9, pady=5)

    # Alineador = tk.Label()
    eyeLinerLabel = tk.Label(
        cosmeticsFrame,
        text="Eye liner",
        font=("titillium web light", 10),
        bg="#101214",
        fg="white",
    )
    eyeLinerLabel.grid(row=6, column=0, padx=7, pady=5, sticky="w")

    # Alineador = tk.Entry()
    eyeLinerEntry = tk.Entry(
        cosmeticsFrame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
        width=15,
        insertbackground="gray",
    )
    eyeLinerEntry.grid(row=6, column=1, padx=9, pady=5)

    # Lapiz Labial = tk.Label()
    lipstickLabel = tk.Label(
        cosmeticsFrame,
        text="Lipstick",
        font=("titillium web light", 10),
        bg="#101214",
        fg="white",
    )
    lipstickLabel.grid(row=7, column=0, padx=7, pady=5, sticky="w")

    # Lapiz Labial = tk.Entry()
    lipstickEntry = tk.Entry(
        cosmeticsFrame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
        width=15,
        insertbackground="gray",
    )
    lipstickEntry.grid(row=7, column=1, padx=9, pady=5)

    # columna de Comestibles
    groceriesColumn = tk.Frame(productFrame, bg="#101214")
    groceriesColumn.grid(
        row=0,
        column=1,
        sticky="n"
    )

    groceriesFrame = tk.LabelFrame(
        groceriesColumn,
        text="Groceries",
        font=("titillium web extralight", 13),
        bg="#101214",
        fg="white",
        pady=10,
        padx=6,
        bd=0
    )
    groceriesFrame.pack(fill="x")

    # Listado de cosmeticos
    # Arroz = tk.Label()
    riceLabel = tk.Label(
        groceriesFrame,
        text="Rice",
        font=("titillium web light", 10),
        bg="#101214",
        fg="white",
    )
    riceLabel.grid(row=0, column=0, padx=7, pady=5, sticky="w")

    # Arroz = tk.Entry()
    riceEntry = tk.Entry(
        groceriesFrame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
        width=15,
        insertbackground="gray",
    )
    riceEntry.grid(row=0, column=1, padx=9, pady=5)

    # Oil = tk.Label()
    oilLabel = tk.Label(
        groceriesFrame,
        text="Oil",
        font=("titillium web light", 10),
        bg="#101214",
        fg="white",
    )
    oilLabel.grid(row=1, column=0, padx=7, pady=5, sticky="w")

    # Oil = tk.Entry()
    oilEntry = tk.Entry(
        groceriesFrame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
        width=15,
        insertbackground="gray",
    )
    oilEntry.grid(row=1, column=1, padx=9, pady=5)

    # Huevos = tk.Label()
    eggsLabel = tk.Label(
        groceriesFrame,
        text="Egg",
        font=("titillium web light", 10),
        bg="#101214",
        fg="white",
    )
    eggsLabel.grid(row=2, column=0, padx=7, pady=5, sticky="w")

    # Huevos = tk.Entry()
    eggsEntry = tk.Entry(
        groceriesFrame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
        width=15,
        insertbackground="gray",
    )
    eggsEntry.grid(row=2, column=1, padx=9, pady=5)

    # Sugar = tk.Label()
    sugarLabel = tk.Label(
        groceriesFrame,
        text="Sugar",
        font=("titillium web light", 10),
        bg="#101214",
        fg="white",
    )
    sugarLabel.grid(row=3, column=0, padx=7, pady=5, sticky="w")

    # Sugar = tk.Entry()
    sugarEntry = tk.Entry(
        groceriesFrame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
        width=15,
        insertbackground="gray",
    )
    sugarEntry.grid(row=3, column=1, padx=9, pady=5)

    # Te = tk.Label()
    teaLabel = tk.Label(
        groceriesFrame,
        text="Tea",
        font=("titillium web light", 10),
        bg="#101214",
        fg="white",
    )
    teaLabel.grid(row=4, column=0, padx=7, pady=5, sticky="w")

    # Te = tk.Entry()
    teaEntry = tk.Entry(
        groceriesFrame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
        width=15,
        insertbackground="gray",
    )
    teaEntry.grid(row=4, column=1, padx=9, pady=5)

    # Cinnamon = tk.Label()
    cinnamonLabel = tk.Label(
        groceriesFrame,
        text="Sugar",
        font=("titillium web light", 10),
        bg="#101214",
        fg="white",
    )
    cinnamonLabel.grid(row=5, column=0, padx=7, pady=5, sticky="w")

    # Cinnamon = tk.Entry()
    cinnamonEntry = tk.Entry(
        groceriesFrame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
        width=15,
        insertbackground="gray",
    )
    cinnamonEntry.grid(row=5, column=1, padx=9, pady=5)

    # Bread = tk.Label()
    breadLabel = tk.Label(
        groceriesFrame,
        text="Bread",
        font=("titillium web light", 10),
        bg="#101214",
        fg="white",
    )
    breadLabel.grid(row=6, column=0, padx=7, pady=5, sticky="w")

    # Bread = tk.Entry()
    breadEntry = tk.Entry(
        groceriesFrame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
        width=15,
        insertbackground="gray",
    )
    breadEntry.grid(row=6, column=1, padx=9, pady=5)

    # Salt = tk.Label()
    saltLabel = tk.Label(
        groceriesFrame,
        text="Salt",
        font=("titillium web light", 10),
        bg="#101214",
        fg="white",
    )
    saltLabel.grid(row=7, column=0, padx=7, pady=5, sticky="w")

    # Salt = tk.Entry()
    saltEntry = tk.Entry(
        groceriesFrame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
        width=15,
        insertbackground="gray",
    )
    saltEntry.grid(row=7, column=1, padx=9, pady=5)

    # columna de bebidas
    drinksColumn = tk.Frame(productFrame, bg="#101214")
    drinksColumn.grid(
        row=0,
        column=2,
        sticky="n"
    )

    drinksFrame = tk.LabelFrame(
        drinksColumn,
        text="Drinks",
        font=("titillium web extralight", 13),
        bg="#101214",
        fg="white",
        pady=10,
        padx=6,
        bd=0
    )
    drinksFrame.pack(fill="x")

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
        width=15,
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
        width=15,
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
        width=15,
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
        width=15,
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
        width=15,
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
        width=15,
        insertbackground="gray",
    )
    pepsyEntry.grid(row=5, column=1, padx=9, pady=5)

    # Aquarius = tk.Label()
    aquariusLabel = tk.Label(
        drinksFrame,
        text="Aquarius",
        font=("titillium web light", 10),
        bg="#101214",
        fg="white",
    )
    aquariusLabel.grid(row=6, column=0, padx=7, pady=5, sticky="w")

    # Aquarius = tk.Entry()
    aquariusEntry = tk.Entry(
        drinksFrame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
        width=15,
        insertbackground="gray",
    )
    aquariusEntry.grid(row=6, column=1, padx=9, pady=5)

    # Lemonade = tk.Label()
    lemonadeLabel = tk.Label(
        drinksFrame,
        text="Lemonade",
        font=("titillium web light", 10),
        bg="#101214",
        fg="white",
    )
    lemonadeLabel.grid(row=7, column=0, padx=7, pady=5, sticky="w")

    # Aquarius = tk.Entry()
    lemonadeEntry = tk.Entry(
        drinksFrame,
        font=("titillium web light", 10),
        bg="#1c2023",
        fg="white",
        width=15,
        insertbackground="gray",
    )
    lemonadeEntry.grid(row=7, column=1, padx=9, pady=5)

    billFrame = tk.Frame(productFrame, bg='#1c2023')
    billFrame.grid(row=0, column=3)

    billAreaFrame=tk.Label(
        billFrame, 
        text='Bill Area', 
        font=('titillium web regular', 12),
        fg="white",
        bg='#1c2023',
        bd=0
    )
    billAreaFrame.pack(fill="x", pady=5)

    textarea=tk.Text(
        billFrame,
        font=('titillium web extralight', 12),
        bg='#1c2023',
        fg="white",
        bd=0,
        width=60
    )
    textarea.pack()

    return productFrame
