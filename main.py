import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Billing Application")

    label = tk.Label(root, text="Hi there!")
    label.pack(padx=200, pady=30)

    root.mainloop()


if __name__ == "__main__":
    main()
