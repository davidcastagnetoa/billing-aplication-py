from cx_Freeze import setup, Executable

# Lista de archivos adicionales (ejemplo: imágenes, fuentes, etc.)
# Si no tienes archivos adicionales, simplemente deja la lista vacía.
additional_files = ['path/to/image1.png', 'path/to/font.ttf'] 

build_options = {
    'packages': ['pywin32', 'python_dotenv'],# Puedes añadir paquetes adicionales que no sean detectados automáticamente
    'excludes': [],  # Puedes excluir paquetes que no desees incluir
    'include_files': additional_files
}

setup(
    name="Retailing Billing System",
    version="1.0",
    description="Generate invoice of products",
    options={'build_exe': build_options},
    executables=[Executable("main.py")]  # Punto de entrada de tu aplicación
)
