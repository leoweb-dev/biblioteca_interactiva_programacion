# Importamos la librería
import tkinter as tk

# Configuramos la ventana
ventana = tk.Tk()
ventana.title("Escribe el código correcto")
ventana.geometry("1366x768")

# Creamos los objetos
titulo = tk.Label(text="¡Escribe el código!", font=("Arial", 25, "bold"))
pregunta = tk.Label(text="¿Cómo mostrarías tu nombre en pantalla?", font=("Arial", 15, "bold"))
respuesta = tk.Entry(ventana, bd=1, relief="solid", font=("Cascadia Code", 15))
comprobar = tk.Button(text="¡Comprobar!", font=("Cascadia Code", 15, "bold"))

# Mostramos los objetos
titulo.pack()
pregunta.pack()
respuesta.pack()
comprobar.pack()

# Creamos un bucle para que la ventana no se cierre
ventana.mainloop()