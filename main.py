import tkinter as tk
from productsFrame import create_products_frame
from customerFrame import CustomerFrame
# from customerFrame import create_customer_frame_top
from palette import get_colors
from utils import setup_resize_event
import webbrowser

def open_web_link():
    webbrowser.open('http://www.davidcastagneto.es')  # URL webpage

def main():
    # Importar colores
    colors = get_colors()
    
    # Ventana
    root = tk.Tk()

    # Solo para desarrollo, borrar en produccion
    # setup_resize_event(root)

    root.title("Retail Billing System")
    root.iconbitmap("static/icon.ico")
    root.geometry("1241x781")
    root.config(bg=colors["bg"])
    root.minsize(1241, 781)


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

    # customer_details_frame_top = create_customer_frame_top(root)
    # customer_details_frame_top.pack(fill="x", padx=10, pady=10)

    customerFrame = CustomerFrame(root)
    customerFrame.frame.pack(fill="x", padx=10, pady=10)

    ##################################
    # Panel de Productos y Facturación
    ##################################

    # productFrame = create_products_frame(root)
    # productFrame.pack(fill="x", padx=10, pady=10)

    productFrame = create_products_frame(root, customerFrame)
    productFrame.pack(fill="x", padx=10, pady=10)

    footerFrame = tk.Frame(root, bg=colors["entry"])
    footerFrame.pack(side="bottom", fill="x")

    footerLabel = tk.Label(
        footerFrame, 
        text="Developed by David Castagneto - 2023",
        font=("titillium web regular", 9),
        bg=colors["entry"],
        fg=colors['font'],
        cursor="hand2"
        )
    footerLabel.pack(anchor='e', padx=5)
    footerLabel.bind("<Button-1>", lambda e: open_web_link())

    root.mainloop()


if __name__ == "__main__":
    main()
