# Importamos la librería
import tkinter as tk

# Configuramos la ventana
ventana = tk.Tk()
ventana.title("Escribe el código correcto")
ventana.geometry("1366x768")

# Creamos los objetos
titulo = tk.Label()
pregunta = tk.Label()
respuesta = tk.Text(ventana)
comprobar = tk.Button(text="¡Comprobar!", relief="groove", font=("Cascadia Code", 15, "bold"))

# Configuración de los objetos
respuesta.config(width=80, height=15, font=("Cascadia Code", 15), background="#080808", foreground="white", insertbackground="white")
ventana.config(background='#242424')
titulo.config(text="¡Escribe el código!", font=("Arial", 25, "bold"),background='#242424', foreground="white")
pregunta.config(text="¿Cómo mostrarías tu nombre en pantalla?", font=("Arial", 15, "bold"),background='#242424', foreground="white")

# Mostramos los objetos
titulo.pack()
pregunta.pack()
respuesta.pack()
comprobar.pack()

# Creamos un bucle para que la ventana no se cierre
ventana.mainloop()