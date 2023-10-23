# github.com/punkmonux

import tkinter as tk
from tkinter import simpledialog

# Función para abrir el segundo menú y cerrar la ventana principal
def abrir_segundo_menu():
    # Oculta la ventana principal
    root.withdraw()

    # Crea una nueva ventana
    global segunda_ventana
    segunda_ventana = tk.Toplevel(root)
    segunda_ventana.title("Menú de Pastelería Yolis")
    segunda_ventana.configure(bg="#FFDDC1")  # Color de fondo pastel

    # Botones en el segundo menú
    botones = ["Betun", "Relleno", "Pan", "Decoracion", "Tamaño", "Forma", "Fondant"]
    opciones = {
        "Betun": ["Suizo", "Italiano", "Buttercream"],
        "Relleno": ["Ganache", "Crema", "Chantilly", "Dulce de leche"],
        "Pan": ["Vainilla", "Chocolate"],
        "Decoracion": ["Infantil", "Boda", "Ejecutivo"],
        "Tamaño": ["Grande", "Enorme", "Gigante"],
        "Forma": ["Cuadrado", "Redondo", "Especial"],
        "Fondant": ["Sí", "No"]
    }

    # Función para mostrar las opciones en una ventana personalizada
    def mostrar_opciones(tipo):
        seleccion = simpledialog.askstring("Seleccionar opción", f"Selecciona una opción de {tipo}:", parent=segunda_ventana)
        if seleccion:
            tk.Label(segunda_ventana, text=f"Seleccionaste: {seleccion}", bg="#FFDDC1").pack(padx=20, pady=10)

    for boton in botones:
        tk.Button(segunda_ventana, text=boton, bg="#FFABAB", command=lambda b=boton: mostrar_opciones(b)).pack(padx=20, pady=10)

    # Botón para enviar y cerrar el segundo menú
    def enviar_y_cerrar():
        tk.Label(segunda_ventana, text="Enviado exitosamente, ir a cocina!!!", bg="#FFDDC1").pack(padx=20, pady=10)
        segunda_ventana.destroy()
        root.deiconify()

    boton_enviar = tk.Button(segunda_ventana, text="Enviar", bg="#FFC3A0", command=enviar_y_cerrar)
    boton_enviar.pack(padx=20, pady=10)

    # Botón para cerrar el segundo menú sin enviar
    boton_cerrar = tk.Button(segunda_ventana, text="Cerrar", bg="#FF677D", command=cerrar_segundo_menu)
    boton_cerrar.pack(padx=20, pady=20)

# Función para cerrar la aplicación
def cerrar_aplicacion():
    root.destroy()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Pastelería Yolis")
root.configure(bg="#FFDDC1")  # Color de fondo pastel

# Etiqueta en el menú principal
label_menu_principal = tk.Label(root, text="Pastelería Yolis", font=("Helvetica", 24), bg="#FFDDC1")  # Color de fondo pastel
label_menu_principal.pack(padx=20, pady=20)

# Botón para iniciar y abrir el segundo menú
boton_iniciar = tk.Button(root, text="Iniciar", bg="#FFABAB", command=abrir_segundo_menu)  # Color botón pastel
boton_iniciar.pack(padx=20, pady=20)

# Botón para cerrar la aplicación
boton_cerrar_app = tk.Button(root, text="Cerrar Aplicación", bg="#FF677D", command=cerrar_aplicacion)  # Color botón pastel
boton_cerrar_app.pack(padx=20, pady=20)

# Iniciar el bucle principal de la aplicación
root.mainloop()
