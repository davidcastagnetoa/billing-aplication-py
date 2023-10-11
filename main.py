import os
import tkinter as tk
from productsFrame import ProductFrame
from customerFrame import CustomerFrame
from palette import get_colors
from utils import setup_resize_event
import webbrowser
import ttkbootstrap as ttk
from ttkbootstrap import Toplevel

# new approach
# root = tk.Tk()
root = ttk.Window(themename="superhero")

env_file = ".env"


def createLocalEnv():
    # Crea el archivo
    your_Email = emailEntryData.get()
    your_Password = passwordEntryData.get()
    your_Keyword = keywordEntryData.get()
    your_Account_sid = AccountSidEntryData.get()
    your_Auth_token = AuthTokenEntryData.get()
    your_phone = PhoneEntryData.get()
    env_contain = f"EMAIL={your_Email}\nPASSWORD={your_Password}\nKEY={your_Keyword}\nACCOUNT_SID={your_Account_sid}\nAUTH_TOKEN={your_Auth_token}\nPHONE={your_phone}"
    with open(env_file, "w") as key_file:
        key_file.write(env_contain)

    os.system(f"attrib +s +h {env_file}")
    root2.destroy()


if not os.path.exists(env_file):
    # Crear una ventana que permita al usuario introducir su mail ,
    # contraseña de mail para aplicaciones externas y su palabra clave
    root2 = Toplevel(root)
    # setup_resize_event(root2) # Solo para desarrollo, borrar en produccion
    # root2.iconphoto()
    root2.title("Enter your email data")
    root2.geometry("550x340+650+300")
    root2.resizable(False, False)
    root2.grab_set()  # Bloquea root, acceso a ventana padre

    dataFrame = ttk.Frame(root2, bootstyle="default")
    dataFrame.pack(ipadx=10, ipady=10, pady=(12, 0), padx=10, fill="x")

    # Email

    emailDataFrame = ttk.Frame(dataFrame, bootstyle="default")
    emailDataFrame.pack(padx=10, ipady=10, fill="x")
    emailDataFrame.columnconfigure(0, weight=1)
    emailDataFrame.columnconfigure(1, weight=1)

    emailLabelData = tk.Label(emailDataFrame, text="Enter your email :", font=("titillium web light", 10))
    emailLabelData.grid(row=0, column=0, sticky="w")

    emailEntryData = tk.Entry(emailDataFrame, width=45)
    emailEntryData.grid(row=0, column=1, sticky="e")

    # Password

    passwordDataFrame = ttk.Frame(dataFrame, bootstyle="default")
    passwordDataFrame.pack(padx=10, ipady=10, fill="x")
    passwordDataFrame.columnconfigure(0, weight=1)
    passwordDataFrame.columnconfigure(1, weight=1)

    passwordLabelData = tk.Label(passwordDataFrame, text="Enter your password :", font=("titillium web light", 10))
    passwordLabelData.grid(row=0, column=0, sticky="w")

    passwordEntryData = tk.Entry(passwordDataFrame, show="*", width=45)
    passwordEntryData.grid(row=0, column=1, sticky="e")

    # Keyword

    keywordDataFrame = ttk.Frame(dataFrame, bootstyle="default")
    keywordDataFrame.pack(padx=10, ipady=10, fill="x")
    keywordDataFrame.columnconfigure(0, weight=1)
    keywordDataFrame.columnconfigure(1, weight=1)

    keywordLabelData = tk.Label(keywordDataFrame, text="Enter your Keyword :", font=("titillium web light", 10))
    keywordLabelData.grid(row=0, column=0, sticky="w")

    keywordEntryData = tk.Entry(keywordDataFrame, width=45)
    keywordEntryData.grid(row=0, column=1, sticky="e")

    # your Phone

    PhoneDataFrame = ttk.Frame(dataFrame, bootstyle="default")
    PhoneDataFrame.pack(padx=10, ipady=10, fill="x")
    PhoneDataFrame.columnconfigure(0, weight=1)
    PhoneDataFrame.columnconfigure(1, weight=1)

    PhoneLabelData = tk.Label(PhoneDataFrame, text="Enter your Phone number :", font=("titillium web light", 10))
    PhoneLabelData.grid(row=0, column=0, sticky="w")

    PhoneEntryData = tk.Entry(PhoneDataFrame, width=45)
    PhoneEntryData.grid(row=0, column=1, sticky="e")

    # Account_sid

    AccountSidDataFrame = ttk.Frame(dataFrame, bootstyle="default")
    AccountSidDataFrame.pack(padx=10, ipady=10, fill="x")
    AccountSidDataFrame.columnconfigure(0, weight=1)
    AccountSidDataFrame.columnconfigure(1, weight=1)

    AccountSidLabelData = tk.Label(AccountSidDataFrame, text="Enter your Account Sid :", font=("titillium web light", 10))
    AccountSidLabelData.grid(row=0, column=0, sticky="w")

    AccountSidEntryData = tk.Entry(AccountSidDataFrame, width=45)
    AccountSidEntryData.grid(row=0, column=1, sticky="e")

    # Auth_token

    AuthTokenDataFrame = ttk.Frame(dataFrame, bootstyle="default")
    AuthTokenDataFrame.pack(padx=10, ipady=10, fill="x")
    AuthTokenDataFrame.columnconfigure(0, weight=1)
    AuthTokenDataFrame.columnconfigure(1, weight=1)

    AuthTokenLabelData = tk.Label(AuthTokenDataFrame, text="Enter your Token :", font=("titillium web light", 10))
    AuthTokenLabelData.grid(row=0, column=0, sticky="w")

    AuthTokenEntryData = tk.Entry(AuthTokenDataFrame, width=45)
    AuthTokenEntryData.grid(row=0, column=1, sticky="e")

    # Buttons

    buttonsFrame = ttk.Frame(dataFrame, bootstyle="default")
    buttonsFrame.pack(padx=10, ipady=10, fill="x")
    buttonsFrame.columnconfigure(0, weight=1)
    buttonsFrame.columnconfigure(1, weight=1)

    saveData = ttk.Button(
        buttonsFrame, 
        bootstyle="success", 
        text="Save Data", 
        command=createLocalEnv
    )
    saveData.pack(fill="x", pady=(12, 0))

    cancelButton = ttk.Button(
        buttonsFrame, 
        bootstyle="secondary", 
        text="Cancel", 
        command=root2.destroy
    )
    cancelButton.pack(fill="x", pady=(12, 0))


if not os.path.exists("bills"):
    os.mkdir("bills")


def open_web_link():
    webbrowser.open("http://www.davidcastagneto.es")  # URL webpage


def main():
    # Importar colores
    colors = get_colors()

    # Ventana

    # Solo para desarrollo, borrar en produccion
    # setup_resize_event(root)

    root.title("Retail Billing System")
    root.iconbitmap("static/icon.ico")
    root.geometry("1241x808")
    # root.resizable(False, False)
    root.minsize(1241, 808)

    # Cabecera título = Label()
    headingLabel = ttk.Label(
        root,
        text="Retail Billing System",
        bootstyle="default",
        font=("titillium web regular", 22),
    )
    headingLabel.pack(pady=(10, 0), side="top", anchor="center")

    ####################
    # Panel de Cliente
    ####################

    customer_Frame = CustomerFrame(root)
    customer_Frame.frame.pack(fill="x", padx=10, pady=10)

    ##################################
    # Panel de Productos y Facturación
    ##################################

    # crea instancia para enviar widgets: customerFrame --> productsFrame
    product_frame_instance = ProductFrame(root, customer_Frame)
    productFrame = product_frame_instance.create_products_frame(root)
    productFrame.pack(fill="x", padx=10, pady=10)

    footerFrame = tk.Frame(root, bg=colors["entry"])
    footerFrame.pack(side="bottom", fill="x")

    footerLabel = tk.Label(
        footerFrame,
        text="Developed by David Castagneto - 2023",
        font=("titillium web regular", 9),
        bg=colors["entry"],
        fg=colors["font"],
        cursor="hand2",
    )
    footerLabel.pack(anchor="e", padx=5)
    footerLabel.bind("<Button-1>", lambda e: open_web_link())

    root.mainloop()


sizeRoot = root.geometry()
dimensions = sizeRoot.split("+")[0]

if __name__ == "__main__":
    main()

# DEPENDECIA CIRCULAR PROBLEMA INVESTIGAR
# Developed by David Castagneto, version 1.0
