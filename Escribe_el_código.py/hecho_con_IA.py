import tkinter as tk
from tkinter import scrolledtext, messagebox
import sys
from io import StringIO

class PythonQuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Código Python")
        self.root.geometry("800x600")
        self.root.configure(bg="#2b2b2b")
        
        self.puntos = 0
        self.pregunta_actual = 0
        
        # Definir las preguntas con sus soluciones esperadas
        self.preguntas = [
            {
                "pregunta": "Escribe un código que imprima 'Hola Mundo'",
                "pista": "Usa la función print()",
                "solucion": "print('Hola Mundo')",
                "verificar": lambda output: "Hola Mundo" in output
            },
            {
                "pregunta": "Crea una variable llamada 'edad' con el valor 25 e imprímela",
                "pista": "Primero asigna el valor, luego usa print()",
                "solucion": "edad = 25\nprint(edad)",
                "verificar": lambda output: "25" in output
            },
            {
                "pregunta": "Escribe un código que sume 10 + 15 e imprima el resultado",
                "pista": "Puedes hacer la operación directamente en print() o usar una variable",
                "solucion": "print(10 + 15)",
                "solucion_alt": "resultado = 10 + 15\nprint(resultado)",
                "verificar": lambda output: "25" in output
            },
            {
                "pregunta": "Crea una lista con los números [1, 2, 3, 4, 5] e imprime el tercer elemento",
                "pista": "Recuerda que los índices empiezan en 0",
                "solucion": "lista = [1, 2, 3, 4, 5]\nprint(lista[2])",
                "verificar": lambda output: "3" in output
            },
            {
                "pregunta": "Escribe un bucle for que imprima los números del 1 al 5",
                "pista": "Usa range() dentro del for",
                "solucion": "for i in range(1, 6):\n    print(i)",
                "verificar": lambda output: all(str(i) in output for i in range(1, 6))
            },
            {
                "pregunta": "Crea una función llamada 'saludar' que reciba un nombre y retorne 'Hola [nombre]'. Llama a la función con 'María' e imprime el resultado",
                "pista": "Define la función con def, usa return y luego llámala",
                "solucion": "def saludar(nombre):\n    return f'Hola {nombre}'\n\nprint(saludar('María'))",
                "verificar": lambda output: "Hola María" in output
            },
            {
                "pregunta": "Escribe un condicional if-else que imprima 'Mayor' si la variable num es mayor que 10, sino imprime 'Menor o igual'. Usa num = 15",
                "pista": "Define num primero, luego usa if-else",
                "solucion": "num = 15\nif num > 10:\n    print('Mayor')\nelse:\n    print('Menor o igual')",
                "verificar": lambda output: "Mayor" in output
            },
            {
                "pregunta": "Crea un diccionario con las claves 'nombre' y 'edad' con valores 'Ana' y 30. Imprime el valor de 'nombre'",
                "pista": "Usa llaves {} para crear el diccionario y corchetes [] para acceder",
                "solucion": "persona = {'nombre': 'Ana', 'edad': 30}\nprint(persona['nombre'])",
                "verificar": lambda output: "Ana" in output
            },
            {
                "pregunta": "Escribe una comprensión de lista que genere los cuadrados de los números del 1 al 5 e imprime la lista",
                "pista": "Usa [expresión for variable in rango]",
                "solucion": "cuadrados = [i**2 for i in range(1, 6)]\nprint(cuadrados)",
                "verificar": lambda output: "1" in output and "4" in output and "9" in output and "16" in output and "25" in output
            },
            {
                "pregunta": "Crea una clase llamada 'Persona' con un atributo 'nombre' en el __init__ y un método 'presentarse' que imprima 'Mi nombre es [nombre]'. Crea una instancia con nombre 'Carlos' y llama al método",
                "pista": "Usa class, __init__ con self, y define el método",
                "solucion": "class Persona:\n    def __init__(self, nombre):\n        self.nombre = nombre\n    \n    def presentarse(self):\n        print(f'Mi nombre es {self.nombre}')\n\np = Persona('Carlos')\np.presentarse()",
                "verificar": lambda output: "Mi nombre es Carlos" in output
            }
        ]
        
        self.crear_interfaz()
        self.mostrar_pregunta()
    
    def crear_interfaz(self):
        # Frame superior con título y puntuación
        header_frame = tk.Frame(self.root, bg="#1e1e1e", pady=10)
        header_frame.pack(fill=tk.X)
        
        self.label_titulo = tk.Label(
            header_frame,
            text="🐍 Quiz de Programación Python 🐍",
            font=("Arial", 18, "bold"),
            bg="#1e1e1e",
            fg="#4ec9b0"
        )
        self.label_titulo.pack()
        
        self.label_puntos = tk.Label(
            header_frame,
            text=f"Puntos: {self.puntos}/10 | Pregunta: {self.pregunta_actual + 1}/10",
            font=("Arial", 12),
            bg="#1e1e1e",
            fg="#ffffff"
        )
        self.label_puntos.pack(pady=5)
        
        # Frame de pregunta
        pregunta_frame = tk.Frame(self.root, bg="#2b2b2b", padx=20)
        pregunta_frame.pack(fill=tk.BOTH, pady=10)
        
        self.label_pregunta = tk.Label(
            pregunta_frame,
            text="",
            font=("Arial", 12, "bold"),
            bg="#2b2b2b",
            fg="#ffffff",
            wraplength=750,
            justify=tk.LEFT
        )
        self.label_pregunta.pack(anchor=tk.W, pady=5)
        
        self.label_pista = tk.Label(
            pregunta_frame,
            text="",
            font=("Arial", 10, "italic"),
            bg="#2b2b2b",
            fg="#9cdcfe",
            wraplength=750,
            justify=tk.LEFT
        )
        self.label_pista.pack(anchor=tk.W, pady=5)
        
        # Frame de código
        codigo_frame = tk.Frame(self.root, bg="#2b2b2b", padx=20)
        codigo_frame.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(
            codigo_frame,
            text="Escribe tu código aquí:",
            font=("Arial", 10, "bold"),
            bg="#2b2b2b",
            fg="#ffffff"
        ).pack(anchor=tk.W, pady=5)
        
        self.text_codigo = scrolledtext.ScrolledText(
            codigo_frame,
            height=10,
            font=("Consolas", 11),
            bg="#1e1e1e",
            fg="#d4d4d4",
            insertbackground="#ffffff",
            selectbackground="#264f78"
        )
        self.text_codigo.pack(fill=tk.BOTH, expand=True)
        
        # Frame de botones
        botones_frame = tk.Frame(self.root, bg="#2b2b2b", pady=10)
        botones_frame.pack(fill=tk.X)
        
        self.boton_verificar = tk.Button(
            botones_frame,
            text="✓ Verificar Código",
            font=("Arial", 12, "bold"),
            bg="#0e639c",
            fg="#ffffff",
            command=self.verificar_codigo,
            padx=20,
            pady=10,
            cursor="hand2"
        )
        self.boton_verificar.pack(side=tk.LEFT, padx=20)
        
        self.boton_solucion = tk.Button(
            botones_frame,
            text="💡 Ver Solución",
            font=("Arial", 12),
            bg="#6a6a6a",
            fg="#ffffff",
            command=self.mostrar_solucion,
            padx=20,
            pady=10,
            cursor="hand2"
        )
        self.boton_solucion.pack(side=tk.LEFT, padx=5)
    
    def mostrar_pregunta(self):
        if self.pregunta_actual < len(self.preguntas):
            pregunta = self.preguntas[self.pregunta_actual]
            self.label_pregunta.config(text=f"Pregunta {self.pregunta_actual + 1}: {pregunta['pregunta']}")
            self.label_pista.config(text=f"💡 Pista: {pregunta['pista']}")
            self.text_codigo.delete(1.0, tk.END)
            self.label_puntos.config(text=f"Puntos: {self.puntos}/10 | Pregunta: {self.pregunta_actual + 1}/10")
        else:
            self.mostrar_resultado_final()
    
    def verificar_codigo(self):
        codigo = self.text_codigo.get(1.0, tk.END).strip()
        
        if not codigo:
            messagebox.showwarning("Advertencia", "Por favor, escribe algo de código antes de verificar.")
            return
        
        # Capturar la salida del código
        old_stdout = sys.stdout
        sys.stdout = output_buffer = StringIO()
        
        try:
            # Ejecutar el código del usuario
            exec(codigo)
            output = output_buffer.getvalue()
            
            # Verificar si la salida es correcta
            pregunta = self.preguntas[self.pregunta_actual]
            if pregunta['verificar'](output):
                self.puntos += 1
                messagebox.showinfo(
                    "¡Correcto! ✓",
                    f"¡Excelente! Tu código es correcto.\n\nPuntos: {self.puntos}"
                )
                self.pregunta_actual += 1
                self.mostrar_pregunta()
            else:
                messagebox.showerror(
                    "Incorrecto ✗",
                    f"El código se ejecutó pero no produce el resultado esperado.\n\nSalida obtenida:\n{output}\n\nIntenta de nuevo o revisa la pista."
                )
        
        except Exception as e:
            messagebox.showerror(
                "Error en el código",
                f"Tu código tiene un error:\n\n{str(e)}\n\nRevisa la sintaxis y vuelve a intentar."
            )
        
        finally:
            sys.stdout = old_stdout
    
    def mostrar_solucion(self):
        pregunta = self.preguntas[self.pregunta_actual]
        respuesta = messagebox.askyesno(
            "Ver Solución",
            "¿Estás seguro de que quieres ver la solución?\n\nEsta pregunta no sumará puntos."
        )
        
        if respuesta:
            self.text_codigo.delete(1.0, tk.END)
            self.text_codigo.insert(1.0, pregunta['solucion'])
            messagebox.showinfo(
                "Solución",
                "La solución ha sido cargada en el editor.\n\nPuedes estudiarla y pasar a la siguiente pregunta."
            )
            self.pregunta_actual += 1
            self.mostrar_pregunta()
    
    def mostrar_resultado_final(self):
        porcentaje = (self.puntos / len(self.preguntas)) * 100
        
        if porcentaje == 100:
            mensaje = "¡PERFECTO! 🏆\n¡Eres un maestro de Python!"
        elif porcentaje >= 70:
            mensaje = "¡Muy bien! 🎉\n¡Tienes un buen dominio de Python!"
        elif porcentaje >= 50:
            mensaje = "¡Bien hecho! 👍\nSigue practicando para mejorar."
        else:
            mensaje = "Sigue intentándolo 💪\n¡La práctica hace al maestro!"
        
        resultado = messagebox.askyesno(
            "Juego Completado",
            f"{mensaje}\n\nPuntuación final: {self.puntos}/{len(self.preguntas)} ({porcentaje:.0f}%)\n\n¿Quieres jugar de nuevo?"
        )
        
        if resultado:
            self.reiniciar_juego()
        else:
            self.root.quit()
    
    def reiniciar_juego(self):
        self.puntos = 0
        self.pregunta_actual = 0
        self.mostrar_pregunta()

if __name__ == "__main__":
    root = tk.Tk()
    juego = PythonQuizGame(root)
    root.mainloop()