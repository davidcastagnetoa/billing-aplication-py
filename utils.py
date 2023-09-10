import tkinter as tk

def on_resize(event):
    # Imprime las dimensiones actuales de la ventana
    print(f"Width: {event.width}, Height: {event.height}")

def setup_resize_event(root):
    # Vincula el evento <Configure> a la función on_resize
    root.bind('<Configure>', on_resize)
