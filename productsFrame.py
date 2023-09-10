import tkinter as tk
from tkinter import messagebox
from palette import get_colors
from billing_app import BillingApp

# Importar colores
colors = get_colors()


def create_products_frame(parent, customerFrame):
    nameEntry = customerFrame.nameEntry
    emailEntry = customerFrame.emailEntry
    phoneEntry = customerFrame.phoneEntry
    billEntry = customerFrame.billEntry
    addressEntry = customerFrame.addressEntry
    cityEntry = customerFrame.cityEntry
    zipEntry = customerFrame.zipEntry
    countryEntry = customerFrame.countryEntry

    productFrame = tk.LabelFrame(
        parent,
        text="Products",
        font=("titillium web regular", 14),
        bg=colors["bg"],
        fg=colors["font"],
        pady=5,
        bd=0,
    )
    productFrame.pack(fill="x", padx=10, pady=10)

    # productFrame.grid_columnconfigure(0, weight=1)
    # productFrame.grid_columnconfigure(1, weight=1)
    # productFrame.grid_columnconfigure(2, weight=1)
    productFrame.grid_columnconfigure(3, weight=4)
    # productFrame.grid_columnconfigure(4, weight=1)

    # Columnas
    # columna de Cosmeticos
    cosmeticsColumn = tk.Frame(productFrame, bg=colors["bg"])
    cosmeticsColumn.grid(
        row=0,
        column=0,
        sticky="n"
    )

    cosmeticsFrame = tk.LabelFrame(
        cosmeticsColumn,
        text="Cosmetics",
        font=("titillium web extralight", 13),
        bg=colors["bg"],
        fg=colors["font"],
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
        bg=colors["bg"],
        fg=colors["font"],
    )
    bathSoapLabel.grid(row=0, column=0, padx=7, pady=5, sticky="w")

    # Funcion para definir efecto placeholder
    def on_entry_click(event, entry, placeholder_text):
        """Función que se activa cuando el usuario hace clic en una entrada."""
        if entry.get() == placeholder_text:
            entry.delete(0, "end")
            entry.insert(0, '')
            entry.config(fg=colors["font"])

    def on_focusout(event, entry, placeholder_text):
        """Función que se activa cuando el usuario se aleja de una entrada."""
        if entry.get() == '':
            entry.insert(0, placeholder_text)
            entry.config(fg=colors["font"])

    def setup_entry_placeholder(entry, placeholder_text):
        entry.insert(0, placeholder_text)
        entry.config(fg='grey')
        entry.bind('<FocusIn>', lambda event, e=entry, p=placeholder_text: on_entry_click(event, e, p))
        entry.bind('<FocusOut>', lambda event, e=entry, p=placeholder_text: on_focusout(event, e, p))


    # Jabon de baño = tk.Entry()
    bathSoapEntry = tk.Entry(
        cosmeticsFrame,
        font=("titillium web light", 10),
        bg=colors["entry"],
        fg=colors["font"],
        width=15,
        insertbackground="gray",
    )
    bathSoapEntry.grid(row=0, column=1, padx=9, pady=5)
    setup_entry_placeholder(bathSoapEntry, '0')

    # Crema de cara = tk.Label()
    faceCreamLabel = tk.Label(
        cosmeticsFrame,
        text="Face Cream",
        font=("titillium web light", 10),
        bg=colors["bg"],
        fg=colors["font"],
    )
    faceCreamLabel.grid(row=1, column=0, padx=7, pady=5, sticky="w")

    # Crema de cara = tk.Entry()
    faceCreamEntry = tk.Entry(
        cosmeticsFrame,
        font=("titillium web light", 10),
        bg=colors["entry"],
        fg=colors["font"],
        width=15,
        insertbackground="gray",
    )
    faceCreamEntry.grid(row=1, column=1, padx=9, pady=5)
    setup_entry_placeholder(faceCreamEntry, '0')

    # Jabon de cara = tk.Label()
    faceWashLabel = tk.Label(
        cosmeticsFrame,
        text="Face Wash",
        font=("titillium web light", 10),
        bg=colors["bg"],
        fg=colors["font"],
    )
    faceWashLabel.grid(row=2, column=0, padx=7, pady=5, sticky="w")

    # Jabon de cara = tk.Entry()
    faceWashEntry = tk.Entry(
        cosmeticsFrame,
        font=("titillium web light", 10),
        bg=colors["entry"],
        fg=colors["font"],
        width=15,
        insertbackground="gray",
    )
    faceWashEntry.grid(row=2, column=1, padx=9, pady=5)
    setup_entry_placeholder(faceWashEntry, '0')

    # Spray de pelo = tk.Label()
    hairSprayLabel = tk.Label(
        cosmeticsFrame,
        text="Hair Spray",
        font=("titillium web light", 10),
        bg=colors["bg"],
        fg=colors["font"],
    )
    hairSprayLabel.grid(row=3, column=0, padx=7, pady=5, sticky="w")

    # Spray de pelo = tk.Entry()
    hairSprayEntry = tk.Entry(
        cosmeticsFrame,
        font=("titillium web light", 10),
        bg=colors["entry"],
        fg=colors["font"],
        width=15,
        insertbackground="gray",
    )
    hairSprayEntry.grid(row=3, column=1, padx=9, pady=5)
    setup_entry_placeholder(hairSprayEntry, '0')

    # Gel de pelo = tk.Label()
    hairGelLabel = tk.Label(
        cosmeticsFrame,
        text="Har Gel",
        font=("titillium web light", 10),
        bg=colors["bg"],
        fg=colors["font"],
    )
    hairGelLabel.grid(row=4, column=0, padx=7, pady=5, sticky="w")

    # Gel de pelo = tk.Entry()
    hairGelEntry = tk.Entry(
        cosmeticsFrame,
        font=("titillium web light", 10),
        bg=colors["entry"],
        fg=colors["font"],
        width=15,
        insertbackground="gray",
    )
    hairGelEntry.grid(row=4, column=1, padx=9, pady=5)
    setup_entry_placeholder(hairGelEntry, '0')

    # Locion de cuerpo = tk.Label()
    lotionBodyLabel = tk.Label(
        cosmeticsFrame,
        text="Lotion Body",
        font=("titillium web light", 10),
        bg=colors["bg"],
        fg=colors["font"],
    )
    lotionBodyLabel.grid(row=5, column=0, padx=7, pady=5, sticky="w")

    # Locion de cuerpo = tk.Entry()
    lotionBodyEntry = tk.Entry(
        cosmeticsFrame,
        font=("titillium web light", 10),
        bg=colors["entry"],
        fg=colors["font"],
        width=15,
        insertbackground="gray",
    )
    lotionBodyEntry.grid(row=5, column=1, padx=9, pady=5)
    setup_entry_placeholder(lotionBodyEntry, '0')

    # Alineador = tk.Label()
    eyeLinerLabel = tk.Label(
        cosmeticsFrame,
        text="Eye liner",
        font=("titillium web light", 10),
        bg=colors["bg"],
        fg=colors["font"],
    )
    eyeLinerLabel.grid(row=6, column=0, padx=7, pady=5, sticky="w")

    # Alineador = tk.Entry()
    eyeLinerEntry = tk.Entry(
        cosmeticsFrame,
        font=("titillium web light", 10),
        bg=colors["entry"],
        fg=colors["font"],
        width=15,
        insertbackground="gray",
    )
    eyeLinerEntry.grid(row=6, column=1, padx=9, pady=5)
    setup_entry_placeholder(eyeLinerEntry, '0')

    # Lapiz Labial = tk.Label()
    lipstickLabel = tk.Label(
        cosmeticsFrame,
        text="Lipstick",
        font=("titillium web light", 10),
        bg=colors["bg"],
        fg=colors["font"],
    )
    lipstickLabel.grid(row=7, column=0, padx=7, pady=5, sticky="w")

    # Lapiz Labial = tk.Entry()
    lipstickEntry = tk.Entry(
        cosmeticsFrame,
        font=("titillium web light", 10),
        bg=colors["entry"],
        fg=colors["font"],
        width=15,
        insertbackground="gray",
    )
    lipstickEntry.grid(row=7, column=1, padx=9, pady=5)
    setup_entry_placeholder(lipstickEntry, '0')

    # columna de Comestibles
    groceriesColumn = tk.Frame(productFrame, bg=colors["bg"])
    groceriesColumn.grid(
        row=0,
        column=1,
        sticky="n"
    )

    groceriesFrame = tk.LabelFrame(
        groceriesColumn,
        text="Groceries",
        font=("titillium web extralight", 13),
        bg=colors["bg"],
        fg=colors["font"],
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
        bg=colors["bg"],
        fg=colors["font"],
    )
    riceLabel.grid(row=0, column=0, padx=7, pady=5, sticky="w")

    # Arroz = tk.Entry()
    riceEntry = tk.Entry(
        groceriesFrame,
        font=("titillium web light", 10),
        bg=colors["entry"],
        fg=colors["font"],
        width=15,
        insertbackground="gray",
    )
    riceEntry.grid(row=0, column=1, padx=9, pady=5)
    setup_entry_placeholder(riceEntry, '0')

    # Oil = tk.Label()
    oilLabel = tk.Label(
        groceriesFrame,
        text="Oil",
        font=("titillium web light", 10),
        bg=colors["bg"],
        fg=colors["font"],
    )
    oilLabel.grid(row=1, column=0, padx=7, pady=5, sticky="w")

    # Oil = tk.Entry()
    oilEntry = tk.Entry(
        groceriesFrame,
        font=("titillium web light", 10),
        bg=colors["entry"],
        fg=colors["font"],
        width=15,
        insertbackground="gray",
    )
    oilEntry.grid(row=1, column=1, padx=9, pady=5)
    setup_entry_placeholder(oilEntry, '0')

    # Huevos = tk.Label()
    eggsLabel = tk.Label(
        groceriesFrame,
        text="Egg",
        font=("titillium web light", 10),
        bg=colors["bg"],
        fg=colors["font"],
    )
    eggsLabel.grid(row=2, column=0, padx=7, pady=5, sticky="w")

    # Huevos = tk.Entry()
    eggsEntry = tk.Entry(
        groceriesFrame,
        font=("titillium web light", 10),
        bg=colors["entry"],
        fg=colors["font"],
        width=15,
        insertbackground="gray",
    )
    eggsEntry.grid(row=2, column=1, padx=9, pady=5)
    setup_entry_placeholder(eggsEntry, '0')

    # Sugar = tk.Label()
    sugarLabel = tk.Label(
        groceriesFrame,
        text="Sugar",
        font=("titillium web light", 10),
        bg=colors["bg"],
        fg=colors["font"],
    )
    sugarLabel.grid(row=3, column=0, padx=7, pady=5, sticky="w")

    # Sugar = tk.Entry()
    sugarEntry = tk.Entry(
        groceriesFrame,
        font=("titillium web light", 10),
        bg=colors["entry"],
        fg=colors["font"],
        width=15,
        insertbackground="gray",
    )
    sugarEntry.grid(row=3, column=1, padx=9, pady=5)
    setup_entry_placeholder(sugarEntry, '0')

    # Te = tk.Label()
    teaLabel = tk.Label(
        groceriesFrame,
        text="Tea",
        font=("titillium web light", 10),
        bg=colors["bg"],
        fg=colors["font"],
    )
    teaLabel.grid(row=4, column=0, padx=7, pady=5, sticky="w")

    # Te = tk.Entry()
    teaEntry = tk.Entry(
        groceriesFrame,
        font=("titillium web light", 10),
        bg=colors["entry"],
        fg=colors["font"],
        width=15,
        insertbackground="gray",
    )
    teaEntry.grid(row=4, column=1, padx=9, pady=5)
    setup_entry_placeholder(teaEntry, '0')

    # Cinnamon = tk.Label()
    cinnamonLabel = tk.Label(
        groceriesFrame,
        text="Sugar",
        font=("titillium web light", 10),
        bg=colors["bg"],
        fg=colors["font"],
    )
    cinnamonLabel.grid(row=5, column=0, padx=7, pady=5, sticky="w")

    # Cinnamon = tk.Entry()
    cinnamonEntry = tk.Entry(
        groceriesFrame,
        font=("titillium web light", 10),
        bg=colors["entry"],
        fg=colors["font"],
        width=15,
        insertbackground="gray",
    )
    cinnamonEntry.grid(row=5, column=1, padx=9, pady=5)
    setup_entry_placeholder(cinnamonEntry, '0')

    # Bread = tk.Label()
    breadLabel = tk.Label(
        groceriesFrame,
        text="Bread",
        font=("titillium web light", 10),
        bg=colors["bg"],
        fg=colors["font"],
    )
    breadLabel.grid(row=6, column=0, padx=7, pady=5, sticky="w")

    # Bread = tk.Entry()
    breadEntry = tk.Entry(
        groceriesFrame,
        font=("titillium web light", 10),
        bg=colors["entry"],
        fg=colors["font"],
        width=15,
        insertbackground="gray",
    )
    breadEntry.grid(row=6, column=1, padx=9, pady=5)
    setup_entry_placeholder(breadEntry, '0')

    # Salt = tk.Label()
    saltLabel = tk.Label(
        groceriesFrame,
        text="Salt",
        font=("titillium web light", 10),
        bg=colors["bg"],
        fg=colors["font"],
    )
    saltLabel.grid(row=7, column=0, padx=7, pady=5, sticky="w")

    # Salt = tk.Entry()
    saltEntry = tk.Entry(
        groceriesFrame,
        font=("titillium web light", 10),
        bg=colors["entry"],
        fg=colors["font"],
        width=15,
        insertbackground="gray",
    )
    saltEntry.grid(row=7, column=1, padx=9, pady=5)
    setup_entry_placeholder(saltEntry, '0')

    # columna de bebidas
    drinksColumn = tk.Frame(productFrame, bg=colors["bg"])
    drinksColumn.grid(
        row=0,
        column=2,
        sticky="n"
    )

    drinksFrame = tk.LabelFrame(
        drinksColumn,
        text="Drinks",
        font=("titillium web extralight", 13),
        bg=colors["bg"],
        fg=colors["font"],
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
        bg=colors["bg"],
        fg=colors["font"],
    )
    beerLabel.grid(row=0, column=0, padx=7, pady=5, sticky="w")

    # Cerveza = tk.Entry()
    beerEntry = tk.Entry(
        drinksFrame,
        font=("titillium web light", 10),
        bg=colors["entry"],
        fg=colors["font"],
        width=15,
        insertbackground="gray",
    )
    beerEntry.grid(row=0, column=1, padx=9, pady=5)
    setup_entry_placeholder(beerEntry, '0')

    # Soda = tk.Label()
    sodaLabel = tk.Label(
        drinksFrame,
        text="Soda",
        font=("titillium web light", 10),
        bg=colors["bg"],
        fg=colors["font"],
    )
    sodaLabel.grid(row=1, column=0, padx=7, pady=5, sticky="w")

    # Soda = tk.Entry()
    sodaEntry = tk.Entry(
        drinksFrame,
        font=("titillium web light", 10),
        bg=colors["entry"],
        fg=colors["font"],
        width=15,
        insertbackground="gray",
    )
    sodaEntry.grid(row=1, column=1, padx=9, pady=5)
    setup_entry_placeholder(sodaEntry, '0')

    # Agua = tk.Label()
    waterLabel = tk.Label(
        drinksFrame,
        text="Water",
        font=("titillium web light", 10),
        bg=colors["bg"],
        fg=colors["font"],
    )
    waterLabel.grid(row=2, column=0, padx=7, pady=5, sticky="w")

    # Agua = tk.Entry()
    waterEntry = tk.Entry(
        drinksFrame,
        font=("titillium web light", 10),
        bg=colors["entry"],
        fg=colors["font"],
        width=15,
        insertbackground="gray",
    )
    waterEntry.grid(row=2, column=1, padx=9, pady=5)
    setup_entry_placeholder(waterEntry, '0')

    # Coffee = tk.Label()
    coffeeLabel = tk.Label(
        drinksFrame,
        text="Coffee",
        font=("titillium web light", 10),
        bg=colors["bg"],
        fg=colors["font"],
    )
    coffeeLabel.grid(row=3, column=0, padx=7, pady=5, sticky="w")

    # Coffee = tk.Entry()
    coffeeEntry = tk.Entry(
        drinksFrame,
        font=("titillium web light", 10),
        bg=colors["entry"],
        fg=colors["font"],
        width=15,
        insertbackground="gray",
    )
    coffeeEntry.grid(row=3, column=1, padx=9, pady=5)
    setup_entry_placeholder(coffeeEntry, '0')

    # Fanta = tk.Label()
    fantaLabel = tk.Label(
        drinksFrame,
        text="Fanta",
        font=("titillium web light", 10),
        bg=colors["bg"],
        fg=colors["font"],
    )
    fantaLabel.grid(row=4, column=0, padx=7, pady=5, sticky="w")

    # Fanta = tk.Entry()
    fantaEntry = tk.Entry(
        drinksFrame,
        font=("titillium web light", 10),
        bg=colors["entry"],
        fg=colors["font"],
        width=15,
        insertbackground="gray",
    )
    fantaEntry.grid(row=4, column=1, padx=9, pady=5)
    setup_entry_placeholder(fantaEntry, '0')

    # Pepsy = tk.Label()
    pepsyLabel = tk.Label(
        drinksFrame,
        text="Pepsy",
        font=("titillium web light", 10),
        bg=colors["bg"],
        fg=colors["font"],
    )
    pepsyLabel.grid(row=5, column=0, padx=7, pady=5, sticky="w")

    # Pepsy = tk.Entry()
    pepsyEntry = tk.Entry(
        drinksFrame,
        font=("titillium web light", 10),
        bg=colors["entry"],
        fg=colors["font"],
        width=15,
        insertbackground="gray",
    )
    pepsyEntry.grid(row=5, column=1, padx=9, pady=5)
    setup_entry_placeholder(pepsyEntry, '0')

    # Aquarius = tk.Label()
    aquariusLabel = tk.Label(
        drinksFrame,
        text="Aquarius",
        font=("titillium web light", 10),
        bg=colors["bg"],
        fg=colors["font"],
    )
    aquariusLabel.grid(row=6, column=0, padx=7, pady=5, sticky="w")

    # Aquarius = tk.Entry()
    aquariusEntry = tk.Entry(
        drinksFrame,
        font=("titillium web light", 10),
        bg=colors["entry"],
        fg=colors["font"],
        width=15,
        insertbackground="gray",
    )
    aquariusEntry.grid(row=6, column=1, padx=9, pady=5)
    setup_entry_placeholder(aquariusEntry, '0')

    # Lemonade = tk.Label()
    lemonadeLabel = tk.Label(
        drinksFrame,
        text="Lemonade",
        font=("titillium web light", 10),
        bg=colors["bg"],
        fg=colors["font"],
    )
    lemonadeLabel.grid(row=7, column=0, padx=7, pady=5, sticky="w")

    # Aquarius = tk.Entry()
    lemonadeEntry = tk.Entry(
        drinksFrame,
        font=("titillium web light", 10),
        bg=colors["entry"],
        fg=colors["font"],
        width=15,
        insertbackground="gray",
    )
    lemonadeEntry.grid(row=7, column=1, padx=9, pady=5)
    setup_entry_placeholder(lemonadeEntry, '0')

    billFrame = tk.Frame(
        productFrame, 
        # bg='#06141B',
        bg=colors['bg2'],
    )

    billFrame.grid(
        row=0, 
        column=3, 
        sticky='e'
    )

    billAreaFrame=tk.Label(
        billFrame, 
        text='Bill Area', 
        font=('titillium web regular', 12),
        fg=colors["font"],
        bg=colors['bg2']
    )
    billAreaFrame.pack(fill="x", pady=5)

    scrollbar = tk.Scrollbar(
        billFrame, orient="vertical",
        # width=14,
    )
    scrollbar.pack(side="right", fill="y")

    textarea=tk.Text(
        billFrame,
        font=('titillium web extralight', 10),
        bg=colors["entry"],
        fg=colors["font"],
        bd=0,
        width=60,
        height=14,
        insertbackground=colors['font'],
        yscrollcommand=scrollbar.set
    )
    textarea.pack()
    textarea.configure(state='disabled')

    scrollbar.config(command=textarea.yview)
    
    ########################
    # Panel de Facturacion #
    ########################
    
    billMenuFrame = tk.LabelFrame(
        parent,
        text="Bill Menu",
        font=("titillium web regular", 14),
        bg=colors["bg"],
        fg=colors["font"],
        pady=5,
        bd=0,
    )
    billMenuFrame.pack(fill="x", padx=10, pady=10)

    # Columnas
    # columna de Precios
    priceColumn = tk.Frame(billMenuFrame, bg=colors["bg"])
    priceColumn.grid(
        row=0,
        column=0,
        sticky="nswe"
    )

    # Precios de cosmeticos
    cosmeticPriceLabel = tk.Label(
        priceColumn,
        text="Cosmetics Price",
        font=("titillium web light", 10),
        bg=colors["bg"],
        fg=colors["font"],
    )
    cosmeticPriceLabel.grid(row=0, column=0, padx=7, pady=5, sticky="w")

    cosmeticPriceEntry = tk.Entry(
        priceColumn,
        font=("titillium web light", 10),
        bg=colors["entry"],
        fg=colors["font"],
        width=15,
        insertbackground="gray",
    )
    cosmeticPriceEntry.grid(row=0, column=1, padx=9, pady=5)

    # Precios de Comestibles
    groceriesPriceLabel = tk.Label(
        priceColumn,
        text="Groceries Price",
        font=("titillium web light", 10),
        bg=colors["bg"],
        fg=colors["font"],
    )
    groceriesPriceLabel.grid(row=1, column=0, padx=7, pady=5, sticky="w")

    groceriesPriceEntry = tk.Entry(
        priceColumn,
        font=("titillium web light", 10),
        bg=colors["entry"],
        fg=colors["font"],
        width=15,
        insertbackground="gray",
    )
    groceriesPriceEntry.grid(row=1, column=1, padx=9, pady=5)

    # Precios de Bebidas
    drinksPricesLabel = tk.Label(
        priceColumn,
        text="Drinks Price",
        font=("titillium web light", 10),
        bg=colors["bg"],
        fg=colors["font"],
    )
    drinksPricesLabel.grid(row=2, column=0, padx=7, pady=5, sticky="w")

    drinksPricesEntry = tk.Entry(
        priceColumn,
        font=("titillium web light", 10),
        bg=colors["entry"],
        fg=colors["font"],
        width=15,
        insertbackground="gray",
    )
    drinksPricesEntry.grid(row=2, column=1, padx=9, pady=5)

    # columna de Impuestos
    taxColumn = tk.Frame(billMenuFrame, bg=colors["bg"])
    taxColumn.grid(
        row=0,
        column=1,
        sticky='nswe'
    )
    
    # Impuestos de cosmeticos
    cosmeticTaxesLabel = tk.Label(
        taxColumn,
        text="Cosmetics Taxes",
        font=("titillium web light", 10),
        bg=colors["bg"],
        fg=colors["font"],
    )
    cosmeticTaxesLabel.grid(row=0, column=0, padx=7, pady=5, sticky="w")

    cosmeticTaxesEntry = tk.Entry(
        taxColumn,
        font=("titillium web light", 10),
        bg=colors["entry"],
        fg=colors["font"],
        width=15,
        insertbackground="gray",
    )
    cosmeticTaxesEntry.grid(row=0, column=1, padx=9, pady=5)
    
    # Impuestos de consumibles
    groceriesTaxesLabel = tk.Label(
        taxColumn,
        text="Groceries Taxes",
        font=("titillium web light", 10),
        bg=colors["bg"],
        fg=colors["font"],
    )
    groceriesTaxesLabel.grid(row=1, column=0, padx=7, pady=5, sticky="w")

    groceriesTaxesEntry = tk.Entry(
        taxColumn,
        font=("titillium web light", 10),
        bg=colors["entry"],
        fg=colors["font"],
        width=15,
        insertbackground="gray",
    )
    groceriesTaxesEntry.grid(row=1, column=1, padx=9, pady=5)
    
    # Impuestos de bebidas
    drinksTaxesLabel = tk.Label(
        taxColumn,
        text="Drinks Taxes",
        font=("titillium web light", 10),
        bg=colors["bg"],
        fg=colors["font"],
    )
    drinksTaxesLabel.grid(row=2, column=0, padx=7, pady=5, sticky="w")

    drinksTaxesEntry = tk.Entry(
        taxColumn,
        font=("titillium web light", 10),
        bg=colors["entry"],
        fg=colors["font"],
        width=15,
        insertbackground="gray",
    )
    drinksTaxesEntry.grid(row=2, column=1, padx=9, pady=5)

    # Columna de botones

    billMenuFrame.grid_columnconfigure(2, weight=1)

    buttonFrame = tk.Frame(
        billMenuFrame,
        bg=colors["bg"],
    )
    buttonFrame.grid(row=0, column=2, rowspan=3, sticky='e')

    ##############################
    # Funcionalidad de los Botones
    ##############################

    # class BillingApp:
    #     def __init__(self):
    #         # Si tienes algún código de inicialización, ponlo aquí.
    #         self.total_general = 0.0

    #     def total(self):
    #         # Precios de productos
    #         prices = {
    #             # Cosmetics
    #             'cosmetics': {
    #                 'soap': 3.90,
    #                 'cream': 8.12,
    #                 'wash': 6.85,
    #                 'spray': 5.60,
    #                 'gel': 8.90,
    #                 'lotion': 10.20,
    #                 'eye': 4.30,
    #                 'lip': 6.50,
    #             },

    #             # Groceries
    #             'groceries': {
    #                 'rice' : 2.50,
    #                 'oil' : 4.50,
    #                 'eggs' : 2.10,
    #                 'sugar' : 2.60,
    #                 'tea' : 2.10,
    #                 'cinnamon' : 3.10,
    #                 'bread' : 1.20,
    #                 'salt' : 2.40,
    #             },

    #             # Drinks
    #             'drinks': {
    #                 'beer' : 4.10,
    #                 'soda' : 3.20,
    #                 'water' : 1.20,
    #                 'coffee' : 2.25,
    #                 'fanta' : 1.80,
    #                 'pepsy' : 1.80,
    #                 'aquarius' : 1.60,
    #                 'lemonade' : 1.10
    #             }
    #         }

    #         # Entry widgets para cada producto
    #         entries = {
    #             # Cosmetics
    #             'cosmetics':{
    #                 'soap': bathSoapEntry,
    #                 'cream': faceCreamEntry,
    #                 'wash': faceWashEntry,
    #                 'spray': hairSprayEntry,
    #                 'gel': hairGelEntry,
    #                 'lotion': lotionBodyEntry,
    #                 'eye': eyeLinerEntry,
    #                 'lip': lipstickEntry,
    #             },

    #             # Groceries
    #             'groceries': {
    #                 'rice' : riceEntry,
    #                 'oil' : oilEntry,
    #                 'eggs' : eggsEntry,
    #                 'sugar' : sugarEntry,
    #                 'tea' : teaEntry,
    #                 'cinnamon' : cinnamonEntry,
    #                 'bread' : breadEntry,
    #                 'salt' : saltEntry,
    #             },

    #             # Drinks
    #             'drinks': {
    #                 'beer' : beerEntry,
    #                 'soda' : sodaEntry,
    #                 'water' : waterEntry,
    #                 'coffee' : coffeeEntry,
    #                 'fanta' : fantaEntry,
    #                 'pepsy' : pepsyEntry,
    #                 'aquarius' : aquariusEntry,
    #                 'lemonade' : lemonadeEntry
    #             },
    #         }

    #         # Porcentaje de Impuestos de los productos
    #         taxes = {
    #             'cosmetics': 15,
    #             'groceries' : 21,
    #             'drinks' : 10
    #         }

    #         # Calcula los totales por segmento y el total general
    #         total_cosmetics = sum(prices['cosmetics'][product] * (float(entries['cosmetics'][product].get()) if entries['cosmetics'][product].get() else 0) for product in prices['cosmetics'])
    #         total_groceries = sum(prices['groceries'][product] * (float(entries['groceries'][product].get()) if entries['groceries'][product].get() else 0) for product in prices['groceries'])
    #         total_drinks = sum(prices['drinks'][product] * (float(entries['drinks'][product].get()) if entries['drinks'][product].get() else 0) for product in prices['drinks'])

    #         self.total_general = total_cosmetics + total_groceries + total_drinks

    #         # Totales sin Impuestos
    #         cosmeticPriceEntry.delete(0, tk.END)
    #         cosmeticPriceEntry.insert(0, str(round(total_cosmetics, 2)) + ' €')

    #         groceriesPriceEntry.delete(0, tk.END)
    #         groceriesPriceEntry.insert(0, str(round(total_groceries, 2)) + ' €')

    #         drinksPricesEntry.delete(0, tk.END)
    #         drinksPricesEntry.insert(0, str(round(total_drinks, 2)) + ' €')

    #         print('Total cosmetics is:', round(total_cosmetics, 2))
    #         print('Total groceries is:', round(total_groceries, 2))
    #         print('Total drinks is:', round(total_drinks, 2))
    #         print('Total general is:', round(self.total_general, 2))

    #         # Calculo Añadiento impuestos
    #         cosmetics_taxes = (total_cosmetics * taxes["cosmetics"]/100)
    #         groceries_taxes = (total_groceries * taxes["groceries"]/100)
    #         drinks_taxes = (total_drinks * taxes["drinks"]/100)

    #         bill_cosmetics = total_cosmetics + cosmetics_taxes
    #         bill_groceries = total_groceries + groceries_taxes
    #         bill_drinks = total_drinks + drinks_taxes

    #         self.total_general_taxes = bill_cosmetics + bill_groceries + bill_drinks

    #         # Totales con Impuestos
    #         cosmeticTaxesEntry.delete(0, tk.END)
    #         cosmeticTaxesEntry.insert(0, str(round(cosmetics_taxes, 2)) + ' €')

    #         groceriesTaxesEntry.delete(0, tk.END)
    #         groceriesTaxesEntry.insert(0, str(round(groceries_taxes, 2)) + ' €')

    #         drinksTaxesEntry.delete(0, tk.END)
    #         drinksTaxesEntry.insert(0, str(round(drinks_taxes, 2)) + ' €')

    #         print('Total cosmetics with taxes is:', round(bill_cosmetics, 2))
    #         print('Total groceries with taxes is:', round(bill_groceries, 2))
    #         print('Total drinks with taxes is:', round(bill_drinks, 2))
    #         print('Total to bill is :', round(self.total_general_taxes, 2))

    #         return self.total_general, self.total_general_taxes

    #     def toBill(self):
    #         name = nameEntry.get()
    #         email = emailEntry.get()
    #         cosmetics = cosmeticPriceEntry.get()
    #         groceries = groceriesPriceEntry.get()
    #         drinks = drinksPricesEntry.get()
    #         if name == '' or email == '':
    #             messagebox.showerror("Denegado!", "Debe rellenar todos los datos del cliente")
    #             print(type(name))
    #             print(type(email))
    #             print('Entry values of name and email')
    #         elif cosmetics == '' or groceries == '' or drinks == '' :
    #             print('Entry products')
    #             messagebox.showerror("Denegado!", "No hay productos a facturar")
    #             print(name)
    #             print(email)
    #         else:
    #             print(round(self.total_general, 2))
    #             print(round(self.total_general_taxes, 2))
    #             print(billNumber)
    #             textarea.delete(1.0, tk.END)
    #             textarea.insert(tk.END, "\t\t*** Welcome Customer ***")
    #             textarea.insert(tk.END, f'\nBill Number : {billNumber}')
    #             # textarea.insert(tk.END, "\t\t*** Welcome Customer ***")
    #             # textarea.insert(tk.END, "\t\t*** Welcome Customer ***")

    #         # https://www.youtube.com/watch?v=_qfDSmtn6qA&ab_channel=CodingLifestyle4u


     # Entry widgets para cada producto
    entries = {
        # Cosmetics
        'cosmetics':{
            'soap': bathSoapEntry,
            'cream': faceCreamEntry,
            'wash': faceWashEntry,
            'spray': hairSprayEntry,
            'gel': hairGelEntry,
            'lotion': lotionBodyEntry,
            'eye': eyeLinerEntry,
            'lip': lipstickEntry,
        },

        # Groceries
        'groceries': {
            'rice' : riceEntry,
            'oil' : oilEntry,
            'eggs' : eggsEntry,
            'sugar' : sugarEntry,
            'tea' : teaEntry,
            'cinnamon' : cinnamonEntry,
            'bread' : breadEntry,
            'salt' : saltEntry,
        },

        # Drinks
        'drinks': {
            'beer' : beerEntry,
            'soda' : sodaEntry,
            'water' : waterEntry,
            'coffee' : coffeeEntry,
            'fanta' : fantaEntry,
            'pepsy' : pepsyEntry,
            'aquarius' : aquariusEntry,
            'lemonade' : lemonadeEntry
        },
    }

    # Creando instancia de la clase BillingApp
    billing_instance = BillingApp(entries, cosmeticPriceEntry, groceriesPriceEntry, drinksPricesEntry, cosmeticTaxesEntry, groceriesTaxesEntry, drinksTaxesEntry, nameEntry, emailEntry, phoneEntry, billEntry, addressEntry, zipEntry, cityEntry, countryEntry, textarea)

    # Boton Total
    totalButton = tk.Button(
        buttonFrame, 
        font=("titillium web semibold", 11),
        text="Total",
        bg=colors['button'],
        fg=colors["bg"],
        # padx= 15,
        bd=0,
        width=12,
        
        command=billing_instance.total
    )
    totalButton.grid(row=0, column=0, pady=30, padx=20)

    # Boton Factura
    billButton = tk.Button(
        buttonFrame, 
        font=("titillium web semibold", 11),
        text="Bill",
        bg=colors['button'],
        fg=colors["bg"],
        # padx= 15,
        bd=0,
        width=12,
        
        command=billing_instance.toBill
    )
    billButton.grid(row=0, column=1, pady=30, padx=20)

    # Boton Imprimir
    printButton = tk.Button(
        buttonFrame, 
        font=("titillium web semibold", 11),
        text="Print",
        bg=colors['button'],
        fg=colors["bg"],
        # padx= 15,
        bd=0,
        width=12,
        
        command=billing_instance.save_bill
    )
    printButton.grid(row=0, column=2, pady=30, padx=20)

    # Boton Email
    printButton = tk.Button(
        buttonFrame, 
        font=("titillium web semibold", 11),
        text="Email",
        bg=colors['button'],
        fg=colors["bg"],
        # padx= 15,
        bd=0,
        width=12,

        # command=email
    )
    printButton.grid(row=0, column=3, pady=30, padx=20)

    # Boton Limpiar
    printButton = tk.Button(
        buttonFrame, 
        font=("titillium web semibold", 11),
        text="Clean",
        bg=colors['button'],
        fg=colors["bg"],
        # padx= 15,
        bd=0,
        width=12,

        # command=clean
    )
    printButton.grid(row=0, column=4, pady=30, padx=20)

    return productFrame