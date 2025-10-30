# biblioteca_interactiva_programacion
# 🎮 Quiz de Programación en Python

Un juego educativo interactivo desarrollado con **Tkinter** para aprender y practicar conceptos de programación en Python mediante preguntas de opción múltiple.

## 📋 Descripción

Este quiz te presenta una serie de preguntas sobre programación en Python donde debes completar código o identificar la sintaxis correcta. Perfecto para:
- Estudiantes que están aprendiendo Python
- Profesores que quieren evaluar conocimientos básicos
- Personas que desean repasar conceptos fundamentales

## ✨ Características

- **Interfaz gráfica intuitiva** con diseño oscuro moderno
- **Sistema de preguntas personalizable** mediante archivo JSON
- **Seguimiento de progreso** en tiempo real
- **Sistema de puntaje** que muestra tu desempeño
- **Retroalimentación inmediata** después de cada respuesta
- **Pantalla de resultados final** con mensaje personalizado según tu puntaje
- **Opción de reiniciar** el quiz para practicar nuevamente

## 🚀 Requisitos

- Python 3.x
- Tkinter (generalmente viene incluido con Python)

## 📦 Instalación

1. **Clona o descarga** este repositorio
2. Asegúrate de tener los siguientes archivos en la misma carpeta:
   - `quiz.py` (el script principal)
   - `preguntas.json` (archivo con las preguntas)

## 🎯 Uso

1. **Ejecuta el programa:**
   ```bash
   python quiz.py
   ```

2. **Responde las preguntas:**
   - Lee cada pregunta cuidadosamente
   - Selecciona una de las opciones con los botones de radio
   - Haz clic en "¡Comprobar!" para verificar tu respuesta

3. **Avanza por el quiz:**
   - El programa te mostrará si acertaste o no
   - Automáticamente pasará a la siguiente pregunta
   - Al final verás tu puntaje total

4. **Reinicia si quieres:**
   - Al terminar, puedes hacer clic en "Reiniciar Quiz" para volver a jugar

## 📝 Personalización de Preguntas

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

## 🎨 Interfaz

El quiz cuenta con:
- **Tema oscuro** (#242424 de fondo) para reducir fatiga visual
- **Tipografía clara** (Arial para texto, Cascadia Code para botones)
- **Colores distintivos:**
  - Verde (#4CAF50) para elementos interactivos
  - Blanco para texto principal
  - Gris (#888888) para información secundaria

## 🏆 Sistema de Calificación

Al finalizar el quiz, recibirás:
- Tu puntaje (ej: 4/5)
- Porcentaje de aciertos
- Un mensaje personalizado:
  - 🎉 **100%**: "¡Perfecto!"
  - 👏 **70-99%**: "¡Muy bien!"
  - 💪 **50-69%**: "¡Buen intento!"
  - 📚 **Menos de 50%**: "Sigue practicando"

## 🛠️ Estructura del Proyecto

```
proyecto-quiz/
│
├── quiz.py              # Script principal del juego
├── preguntas.json       # Archivo con las preguntas del quiz
└── README.md           # Este archivo
```

## 🐛 Solución de Problemas

### Error: "No se encontró el archivo 'preguntas.json'"
- Verifica que el archivo `preguntas.json` esté en la misma carpeta que `quiz.py`

### Error: "El archivo 'preguntas.json' tiene un formato inválido"
- Revisa que el JSON esté bien formateado (usa un validador JSON online)
- Verifica que todas las llaves y comas estén correctas

### Los radiobuttons no se deseleccionan
- Asegúrate de tener la versión actualizada del código

## 💡 Ideas para Extender el Proyecto

- Agregar diferentes niveles de dificultad
- Implementar un temporizador para cada pregunta
- Guardar el historial de puntajes
- Añadir categorías de preguntas (variables, funciones, bucles, etc.)
- Modo multijugador con ranking
- Sonidos de retroalimentación

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso educativo.

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar el quiz o quieres agregar más preguntas, siéntete libre de hacerlo.

---

**¡Diviértete aprendiendo Python!** 🐍✨
