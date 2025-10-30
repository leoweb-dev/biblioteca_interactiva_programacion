# Quiz de Programación en Python

Un juego educativo interactivo desarrollado con **Tkinter** para aprender y practicar conceptos de programación en Python mediante preguntas de opción múltiple.

## Descripción

Este quiz te presenta una serie de preguntas sobre programación en Python donde debes completar código o identificar la sintaxis correcta. Perfecto para:
- Estudiantes que están aprendiendo Python
- Profesores que quieren evaluar conocimientos básicos
- Personas que desean repasar conceptos fundamentales

## Características

- **Interfaz gráfica intuitiva** con diseño oscuro moderno
- **Sistema de preguntas personalizable** mediante archivo JSON
- **Seguimiento de progreso** en tiempo real
- **Sistema de puntaje** que muestra tu desempeño
- **Retroalimentación inmediata** después de cada respuesta
- **Pantalla de resultados final** con mensaje personalizado según tu puntaje

## Requisitos

- Python 3.x
- Tkinter (generalmente viene incluido con Python)

## Instalación

1. **Clona o descarga** este repositorio
2. Asegúrate de tener los siguientes archivos en la misma carpeta:
   - `quiz.py` (el script principal)
   - `preguntas.json` (archivo con las preguntas)

## Uso

1. **Ejecuta el programa:**
   ```bash
   main.py
   ```

2. **Responde las preguntas:**
   - Lee cada pregunta cuidadosamente
   - Selecciona la opción que consideres correcta 
   - Haz clic en "¡Comprobar!" para verificar tu respuesta

3. **Avanza por el quiz:**
   - El programa te mostrará si acertaste o no
   - Automáticamente pasará a la siguiente pregunta
   - Al final verás tu puntaje total

4. **Reinicia si quieres:**
   - Al terminar, puedes hacer clic en "Reiniciar Quiz" para volver a jugar

## Personalización de Preguntas

Puedes agregar, modificar o eliminar preguntas editando el archivo `preguntas.json`:

```json
{
    "preguntas": [
        {
            "pregunta": "Tu pregunta aquí\n\n(puedes usar saltos de línea)",
            "opciones": ["opción 1", "opción 2", "opción 3", "opción 4"],
            "respuesta_correcta": "opción 1"
        }
    ]
}
```

### Estructura de cada pregunta:

- **`pregunta`**: El texto de la pregunta (usa `\n` para saltos de línea)
- **`opciones`**: Array con 2 a 4 opciones de respuesta
- **`respuesta_correcta`**: Debe coincidir exactamente con una de las opciones

## Interfaz

El quiz cuenta con:
- **Tema oscuro** (#242424 de fondo) para reducir fatiga visual
- **Tipografía clara** (Arial para texto, Cascadia Code para botones)
- **Colores distintivos:**
  - Verde (#4CAF50) para elementos interactivos
  - Blanco para texto principal
  - Gris (#888888) para información secundaria

## Sistema de Calificación

Al finalizar el quiz, recibirás:
- Tu puntaje (ej: 4/5)
- Porcentaje de aciertos
- Un mensaje personalizado:
  - **100%**: "¡Perfecto!"
  - **70-99%**: "¡Muy bien!"
  - **50-69%**: "¡Buen intento!"
  - **Menos de 50%**: "Sigue practicando"

## Estructura del Proyecto

```
biblioteca_interactiva_programacion/
│
├── main.py             # Script principal del juego
├── preguntas.json      # Archivo con las preguntas del quiz
├── .gitignore          # Su función principal es indicar qué archivos o carpetas deben ser ignorados por Git
├── LICENSE             # Licencia MIT (De uso abierto)
└── README.md           # Este archivo

```
## Justificación del Uso de Librerías

Tkinter: Tk es la librería de interfaz gráfica estándar de Python y la elegimos por las siguientes razones:

1. Integración nativa: Viene incluida con Python, lo que elimina dependencias externas y facilita la distribución del proyecto.

2. Documentación abundante: Existe una gran cantidad de recursos y ejemplos de Tkinter, lo que facilita el aprendizaje y la resolución de problemas.

3. Multiplataforma: Funcionan en Windows, macOS y Linux sin modificaciones, garantizando que el quiz sea accesible para todos los estudiantes.

4. Componentes suficientes: Proporciona todos los widgets necesarios para nuestro proyecto:
   - Label: para mostrar texto e instrucciones
   - Radiobutton: para las opciones múltiples
   - Button: para interacciones
   - Frame: para organizar elementos
   - messagebox: para retroalimentación inmediata

 JSON: lo seleccionamos como formato de almacenamiento de datos por múltiples ventajas:

1. Legibilidad humana: Es fácil de leer y editar manualmente, permitiendo que profesores y estudiantes modifiquen las preguntas sin conocimientos técnicos avanzados.

2. Estructura jerárquica clara: Permite organizar las preguntas con sus opciones y respuestas correctas de manera intuitiva:
   ```json
   {
       "pregunta": "texto",
       "opciones": ["opción1", "opción2"],
       "respuesta_correcta": "opción1"
   }
   ```

3. Separación de datos y lógica: Mantener las preguntas en un archivo separado permite:
   - Actualizar contenido sin tocar el código
   - Facilitar el trabajo colaborativo 

4. Librería nativa: Viene incluido en Python, sin necesidad de instalaciones adicionales.


## Fundamento Didáctico

1. Programación Orientada a Eventos

Este proyecto introduce el concepto de programación basada en eventos, importante en el desarrollo de interfaces gráficas:

- Los botones responden a eventos -command- cuando son presionados
- La interfaz permanece en un loop (`mainloop()`) esperando interacciones del usuario
- Las funciones callback (`comprobar_respuesta`, `cargar_pregunta`) se ejecutan en respuesta a acciones

Este paradigma difiere de la programación secuencial tradicional y prepara para el desarrollo de aplicaciones interactivas modernas.

 2. Manejo de Estado

El proyecto requiere gestionar múltiples estados:

```python
pregunta_actual = 0  # Posición en el quiz
puntaje = 0          # Contador de aciertos
respuesta_seleccionada = tk.StringVar()  # Selección actual
```

prendizaje: Comprender cómo mantener y actualizar el estado de una aplicación es crucial para cualquier proyecto de software.

 3. Separación de Responsabilidades

El código está organizado en funciones con propósitos específicos:
- `cargar_pregunta()`: Actualiza la interfaz
- `comprobar_respuesta()`: Valida la lógica del juego
- `mostrar_resultado_final()`: Maneja la pantalla de resultados

Valor didáctico: Esta estructura facilita el mantenimiento y demuestra buenas prácticas de programación.

 4. Manipulación de Archivos y Datos Estructurados

## Desafíos encontrados y soluciones

Desafío 1: Radiobuttons preseleccionados

Problema: Al inicializar `respuesta_seleccionada = tk.StringVar()` con cadena vacía, los radiobuttons con `value=""` aparecían seleccionados.

Solución: Cambiar la inicialización a `respuesta_seleccionada.set(None)` para indicar explícitamente que no hay selección.

Aprendizaje: Los valores por defecto en widgets GUI requieren atención especial para evitar comportamientos inesperados.


Desafío 2: Gestión dinámica de opciones

Problema: Diferentes preguntas pueden tener diferente número de opciones (2, 3 o 4).

Solución: Crear una lista fija de radiobuttons y activar/desactivar según sea necesario:

```python
for i, opcion in enumerate(opciones_radiobuttons):
    if i < len(p["opciones"]):
        opcion.config(text=p["opciones"][i], value=p["opciones"][i], state='normal')
    else:
        opcion.config(text="", value="", state='disabled')
```

Aprendizaje: La reutilización de componentes es más eficiente que crear/destruir widgets constantemente.


Desafío 3: Codificación de caracteres

Problema: Los acentos y caracteres especiales en español no se mostraban correctamente al leer el JSON.

Solución: Especificar explícitamente `encoding='utf-8'` al abrir el archivo:

```python
with open(ruta_json, 'r', encoding='utf-8') as archivo:
```

Aprendizaje: Siempre considerar la internacionalización desde el inicio del proyecto.


Desafío 4: Navegación entre preguntas

Problema: ¿Cómo avanzar automáticamente después de verificar una respuesta sin confundir al usuario?

Solución: Mostrar un `messagebox` modal que:
1. Informa si acertó o falló
2. Muestra la respuesta correcta (si falló)
3. Pausa la ejecución hasta que el usuario cierre el mensaje
4. Luego carga automáticamente la siguiente pregunta

Aprendizaje: La retroalimentación inmediata y clara mejora significativamente la experiencia de usuario.


## Reflexiones del Proceso de Desarrollo

Sobre el Diseño:

Elegir un tema oscuro (#242424)

Justificación: 
- Reduce la fatiga visual durante sesiones largas de estudio
- Es la preferencia actual en muchos entornos de programación

## Sobre la Arquitectura

Decisión: 
Usar variables globales para `pregunta_actual` y `puntaje`

Ventajas:
- Simplicidad para un proyecto educativo
- Fácil de entender para principiantes

Desventajas reconocidas:
- No es escalable para proyectos grandes
- Puede causar problemas en aplicaciones concurrentes

Reflexión: En un contexto educativo, la simplicidad prima sobre la perfección arquitectónica. El proyecto introduce conceptos progresivamente.

## Sobre la Gestión de Errores

El código incluye múltiples bloques -try-except-:

```python
try:
    with open(ruta_json, 'r', encoding='utf-8') as archivo:
        datos = json.load(archivo)
except FileNotFoundError:
    messagebox.showerror("Error", "No se encontró el archivo...")
```

Valor educativo: Enseña que las aplicaciones robustas deben anticipar y manejar errores de manera elegante, proporcionando mensajes útiles al usuario.

## Licencia

Este proyecto es de código abierto y está disponible para uso educativo.

---

**¡Diviértete aprendiendo Python!** 🐍✨
