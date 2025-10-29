# Importamos las librerías
import tkinter as tk
from tkinter import messagebox
import json
import os

# Cargamos las preguntas desde el archivo JSON externo
try:
    # Obtiene la ruta del archivo JSON (debe estar en la misma carpeta que el script)
    ruta_json = os.path.join(os.path.dirname(__file__), 'preguntas.json')
    
    with open(ruta_json, 'r', encoding='utf-8') as archivo:
        datos = json.load(archivo)
        preguntas = datos["preguntas"]
        
except FileNotFoundError:
    messagebox.showerror("Error", "No se encontró el archivo 'preguntas.json'\nAsegúrate de que esté en la misma carpeta que el programa.")
    exit()
except json.JSONDecodeError:
    messagebox.showerror("Error", "El archivo 'preguntas.json' tiene un formato inválido.")
    exit()
except KeyError:
    messagebox.showerror("Error", "El archivo JSON debe tener una clave 'preguntas'.")
    exit()

# Variable para trackear la pregunta actual
pregunta_actual = 0
puntaje = 0

# Configuramos la ventana
ventana = tk.Tk()
ventana.title("Completa el código")
ventana.geometry("800x600")
ventana.config(background='#242424')

# Variable para almacenar la respuesta seleccionada
respuesta_seleccionada = tk.StringVar()
respuesta_seleccionada.set(None)  # Iniciamos con None para que ninguno esté seleccionado

# Función para cargar una pregunta
def cargar_pregunta():
    global pregunta_actual
    
    if pregunta_actual < len(preguntas):
        # Limpiamos la selección anterior
        respuesta_seleccionada.set(None)  # Cambiado a None
        
        # Obtenemos la pregunta actual
        p = preguntas[pregunta_actual]
        
        # Actualizamos el texto de la pregunta
        pregunta_label.config(text=p["pregunta"])
        
        # Actualizamos las opciones de los radiobuttons
        for i, opcion in enumerate(opciones_radiobuttons):
            if i < len(p["opciones"]):
                opcion.config(text=p["opciones"][i], value=p["opciones"][i], state='normal')
            else:
                opcion.config(text="", value="", state='disabled')
        
        # Actualizamos el contador
        contador_label.config(text=f"Pregunta {pregunta_actual + 1} de {len(preguntas)}")
        
        # Actualizamos el puntaje
        puntaje_label.config(text=f"Puntaje: {puntaje}/{len(preguntas)}")
    else:
        # Fin del quiz
        mostrar_resultado_final()

# Función para comprobar la respuesta
def comprobar_respuesta():
    global pregunta_actual, puntaje
    
    respuesta = respuesta_seleccionada.get()
    
    if respuesta == "":
        messagebox.showwarning("Aviso", "Por favor, selecciona una respuesta")
        return
    
    # Verificamos si es correcta
    if respuesta == preguntas[pregunta_actual]["respuesta_correcta"]:
        puntaje += 1
        messagebox.showinfo("¡Correcto!", f"¡Excelente! La respuesta correcta es '{respuesta}'")
    else:
        messagebox.showerror("Incorrecto", 
                           f"La respuesta no es correcta.\nLa respuesta correcta era: '{preguntas[pregunta_actual]['respuesta_correcta']}'")
    
    # Pasamos a la siguiente pregunta
    pregunta_actual += 1
    cargar_pregunta()

# Función para mostrar el resultado final
def mostrar_resultado_final():
    porcentaje = (puntaje / len(preguntas)) * 100
    
    # Limpiamos la ventana
    for widget in ventana.winfo_children():
        widget.destroy()
    
    # Mostramos el resultado
    resultado_frame = tk.Frame(ventana, background='#242424')
    resultado_frame.pack(expand=True)
    
    titulo_final = tk.Label(resultado_frame, text="¡Quiz Completado!", 
                           font=("Arial", 30, "bold"), background='#242424', foreground="white")
    titulo_final.pack(pady=20)
    
    puntaje_final = tk.Label(resultado_frame, 
                            text=f"Puntaje Final: {puntaje}/{len(preguntas)}\n({porcentaje:.1f}%)", 
                            font=("Arial", 20), background='#242424', foreground="white")
    puntaje_final.pack(pady=20)
    
    if porcentaje == 100:
        mensaje = "¡Perfecto! 🎉"
    elif porcentaje >= 70:
        mensaje = "¡Muy bien! 👏"
    elif porcentaje >= 50:
        mensaje = "¡Buen intento! 💪"
    else:
        mensaje = "Sigue practicando 📚"
    
    mensaje_label = tk.Label(resultado_frame, text=mensaje, 
                            font=("Arial", 18, "bold"), background='#242424', foreground="#4CAF50")
    mensaje_label.pack(pady=20)
    
    boton_reiniciar = tk.Button(resultado_frame, text="Reiniciar Quiz", 
                               command=reiniciar_quiz, relief="groove",
                               font=("Cascadia Code", 15, "bold"),
                               background="#4CAF50", foreground="white", cursor="hand2")
    boton_reiniciar.pack(pady=20)

# Función para reiniciar el quiz
def reiniciar_quiz():
    global pregunta_actual, puntaje
    pregunta_actual = 0
    puntaje = 0
    
    # Recreamos la ventana
    ventana.destroy()
    import sys
    import os
    os.execl(sys.executable, sys.executable, *sys.argv)

# Creamos los widgets principales
titulo = tk.Label(ventana, text="¡Completa el código!", 
                 font=("Arial", 25, "bold"), background='#242424', foreground="white")

contador_label = tk.Label(ventana, text="", font=("Arial", 12), 
                         background='#242424', foreground="#888888")

puntaje_label = tk.Label(ventana, text=f"Puntaje: 0/{len(preguntas)}", 
                        font=("Arial", 12, "bold"), background='#242424', foreground="#4CAF50")

pregunta_label = tk.Label(ventana, text="", font=("Arial", 15, "bold"), 
                         background='#242424', foreground="white")

# Frame para contener los radiobuttons
frame_opciones = tk.Frame(ventana, background='#242424')

# Creamos 4 radiobuttons (suficiente para nuestras preguntas)
opciones_radiobuttons = []
for i in range(4):
    rb = tk.Radiobutton(frame_opciones, text="", variable=respuesta_seleccionada, 
                       value="", font=("Arial", 14), background='#242424', 
                       foreground="white", selectcolor="#161414", 
                       activebackground='#242424', activeforeground="white")
    rb.pack(anchor='w', pady=5, padx=50)
    opciones_radiobuttons.append(rb)

comprobar = tk.Button(ventana, text="¡Comprobar!", command=comprobar_respuesta,
                     relief="groove", font=("Cascadia Code", 15, "bold"),
                     background="#4CAF50", foreground="white", cursor="hand2")

# Posición de los widgets
titulo.grid(row=0, pady=20)
contador_label.grid(row=1, pady=5)
puntaje_label.grid(row=2, pady=5)
pregunta_label.grid(row=3, pady=20)
frame_opciones.grid(row=4, pady=20)
comprobar.grid(row=5, pady=20)

# Especificamos el comportamiento de las filas y columnas
for i in range(6):
    ventana.rowconfigure(i, weight=1)
ventana.columnconfigure(0, weight=1)

# Cargamos la primera pregunta
cargar_pregunta()

# Creamos un bucle para que la ventana no se cierre
ventana.mainloop()