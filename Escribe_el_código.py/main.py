# Importamos la librería
import tkinter as tk

# Configuramos la ventana
ventana = tk.Tk()
ventana.title("Completa el código")
ventana.geometry("800x600")

# Creamos los objetos
titulo = tk.Label()
pregunta = tk.Label()
#respuesta = tk.Text(ventana)
respuesta = tk.Radiobutton()
comprobar = tk.Button()

# Configuración de los objetos
#respuesta.config(width=50, height=15, font=("Cascadia Code", 15), background="#161414", foreground="white", insertbackground="white")
respuesta.config(background="#161414")
ventana.config(background='#242424')
titulo.config(text="¡Completa el código!", font=("Arial", 25, "bold"),background='#242424', foreground="white")
comprobar.config(text="¡Comprobar!", relief="groove", font=("Cascadia Code", 15, "bold"))

#preguntas
pregunta.config(text="¿Cómo mostrarías tu nombre en pantalla? \n\n_____(Mi nombre)", font=("Arial", 15, "bold"),background='#242424', foreground="white")

# Posición de los widget
titulo.grid(row=0)
pregunta.grid(row=1)
respuesta.grid(row=2)
comprobar.grid(row=3)

# Especificamos el comportamiento de las filas y columnas
ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)
ventana.rowconfigure(2, weight=1)
ventana.rowconfigure(3, weight=1)

ventana.columnconfigure(0, weight=1)


# Mostramos los objetos
"""titulo.pack(pady=(30, 10))
pregunta.pack(pady=(10))
respuesta.pack(pady=(10))
comprobar.pack(pady=(20))"""

# Creamos un bucle para que la ventana no se cierre
ventana.mainloop()