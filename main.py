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

    # Configurar la columna 0 para que consuma espacio extra
    # customer_details_frame.grid_columnconfigure(0, weight=1)
    customer_details_frame.grid_columnconfigure(1, weight=1)
    customer_details_frame.grid_columnconfigure(2, weight=1)
    customer_details_frame.grid_columnconfigure(3, weight=1)
    # customer_details_frame.grid_columnconfigure(4, weight=1)
    # customer_details_frame.grid_columnconfigure(5, weight=1)
    # customer_details_frame.grid_columnconfigure(6, weight=1)
    # customer_details_frame.grid_columnconfigure(7, weight=1)

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
        # bd=0,  # remover borde
        # highlightthickness=0,  # remover highlight
        insertbackground="gray",  # color del cursor
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

    root.mainloop()


if __name__ == "__main__":
    main()
