from cx_Freeze import setup, Executable, sys

# Lista de archivos adicionales (ejemplo: imágenes, fuentes, etc.)
# Si no tienes archivos adicionales, simplemente deja la lista vacía.
additional_files = ["static/icon.ico"]

build_options = {
    "base": None,
    "packages": [
        "pywin32",
        "python_dotenv",
    ],  # Puedes añadir paquetes adicionales que no sean detectados automáticamente
    "excludes": [],  # Puedes excluir paquetes que no desees incluir
    "include_files": additional_files,
}

if sys.platform == "win32":
    base = "Win32GUI"

shortcut_table = [
    (
        "DesktopShortcut",  # Shortcut
        "DesktopFolder",  # Directory_
        "Retail Billing System",  # Name
        "TARGETDIR",  # Component_
        "TARGETDIR",  # Component_
        "[TARGETDIR]\main.exe",  # Target,or # "[TARGETDIR]main.py",     # Target
        None,  # Arguments
        None,  # Description
        None,  # Hotkey
        None,
        None,
        None,
        "TARGETDIR",
    )
]
msi_data = {"Shortcut": shortcut_table}
bdist_msi_options = {"data": msi_data}

setup(
    name="Retailing Billing System",
    version="1.0",
    author="David Castagneto Aguirre",
    description="Generate invoice of products",
    options={
        "build_exe": build_options,
        "bdist_msi": bdist_msi_options,
    },
    executables=[
        Executable(script="main.py", base=base, icon="static/icon.ico")
    ],  # Punto de entrada de tu aplicación
)