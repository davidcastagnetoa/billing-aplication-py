# VERIFICA TAMAÑO DE VENTANA
def on_resize(event):
    # Imprime las dimensiones actuales de la ventana
    print(f"Width: {event.width}, Height: {event.height}")


def setup_resize_event(parent):
    # Vincula el evento <Configure> a la función on_resize
    parent.bind("<Configure>", on_resize)
