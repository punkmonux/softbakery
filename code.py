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
            tk.Label(segunda_ventana, text=f"Seleccionaste: {seleccion}").pack(padx=20, pady=10)

    for boton in botones:
        tk.Button(segunda_ventana, text=boton, command=lambda b=boton: mostrar_opciones(b)).pack(padx=20, pady=10)

    # Botón para enviar y cerrar el segundo menú
    def enviar_y_cerrar():
        tk.Label(segunda_ventana, text="Enviado exitosamente, ir a cocina!!!").pack(padx=20, pady=10)
        segunda_ventana.destroy()
        root.deiconify()

    boton_enviar = tk.Button(segunda_ventana, text="Enviar", command=enviar_y_cerrar)
    boton_enviar.pack(padx=20, pady=10)

    # Botón para cerrar el segundo menú sin enviar
    boton_cerrar = tk.Button(segunda_ventana, text="Cerrar", command=cerrar_segundo_menu)
    boton_cerrar.pack(padx=20, pady=20)

# Función para cerrar la aplicación
def cerrar_aplicacion():
    root.destroy()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Pastelería Yolis")

# Etiqueta en el menú principal
label_menu_principal = tk.Label(root, text="Pastelería Yolis", font=("Helvetica", 24))
label_menu_principal.pack(padx=20, pady=20)

# Botón para iniciar y abrir el segundo menú
boton_iniciar = tk.Button(root, text="Iniciar", command=abrir_segundo_menu)
boton_iniciar.pack(padx=20, pady=20)

# Botón para cerrar la aplicación
boton_cerrar_app = tk.Button(root, text="Cerrar Aplicación", command=cerrar_aplicacion)
boton_cerrar_app.pack(padx=20, pady=20)

# Iniciar el bucle principal de la aplicación
root.mainloop()

