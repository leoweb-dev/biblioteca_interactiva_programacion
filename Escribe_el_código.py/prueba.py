import tkinter as tk

ventana = tk.Tk()
ventana.geometry("800x600")

# Configurar la grilla para que se expanda
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_rowconfigure(1, weight=1)
ventana.grid_columnconfigure(0, weight=1)

# Widgets
titulo = tk.Label(ventana, text="¡Escribe el código!", font=("Arial", 25, "bold"))
titulo.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

respuesta = tk.Text(ventana, font=("Cascadia Code", 15))
respuesta.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)

ventana.mainloop()