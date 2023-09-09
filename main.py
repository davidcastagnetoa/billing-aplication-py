import tkinter as tk
from productsFrame import create_products_frame
from customerFrame import create_customer_frame_top


def main():
    # Ventana
    root = tk.Tk()
    root.title("Retail Billing System")

    root.iconbitmap("static/icon.ico")
    root.geometry("1285x500")
    root.config(bg='#101214')
    root.minsize(1285, 600)

    # Cabecera título = Label()
    headingLabel = tk.Label(
        root,
        text="Retail Billing System",
        font=("titillium web semibold", 18),
        bg="#101214",
        fg="white",
    )
    headingLabel.pack(padx=0, pady=0, ipadx=10, ipady=10, fill="x")

    ####################
    # Panel de Cliente
    ####################

    customer_details_frame_top = create_customer_frame_top(root)
    customer_details_frame_top.pack(fill="x", padx=10, pady=10)

    ####################
    # Panel de Productos
    ####################

    productFrame = create_products_frame(root)
    productFrame.pack(fill="x", padx=10, pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
