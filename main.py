import tkinter as tk
from productsFrame import create_products_frame
from customerFrame import create_customer_frame_top
# from billMenu import create_billMenu_frame
from palette import get_colors
from utils import setup_resize_event


def main():
    # Importar colores
    colors = get_colors()
    
    # Ventana
    root = tk.Tk()

    # Solo para desarrollo, borrar en produccion
    # setup_resize_event(root)

    root.title("Retail Billing System")
    root.iconbitmap("static/icon.ico")
    root.geometry("1241x766")
    root.config(bg=colors["bg"])
    root.minsize(1241, 766)


    # Cabecera título = Label()
    headingLabel = tk.Label(
        root,
        text="Retail Billing System",
        font=("titillium web semibold", 18),
        bg=colors["bg"],
        fg=colors['font'],
    )
    headingLabel.pack(padx=0, pady=0, ipadx=10, ipady=10, fill="x")

    ####################
    # Panel de Cliente
    ####################

    customer_details_frame_top = create_customer_frame_top(root)
    customer_details_frame_top.pack(fill="x", padx=10, pady=10)

    ##################################
    # Panel de Productos y Facturación
    ##################################

    # productFrame = create_products_frame(root)
    productFrame = create_products_frame(root)
    productFrame.pack(fill="x", padx=10, pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
