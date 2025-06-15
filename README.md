# 🤠 Juego del Ahorcado en Python 🐍

¡Bienvenido al clásico juego del Ahorcado, desarrollado completamente en Python! Este es un proyecto simple y divertido, ideal para demostrar habilidades básicas de programación en Python de una manera interactiva y entretenida.

## 📜 Descripción del Juego

El objetivo es adivinar una palabra secreta seleccionada al azar de una lista predefinida. Tienes un total de **6 oportunidades** para adivinar la palabra letra por letra. Si fallas 6 veces, ¡el juego termina!

## ✨ Características

-   **Palabra Aleatoria**: En cada partida, se elige una nueva palabra secreta al azar.
-   **Interfaz de Consola Clara**: El estado del juego se muestra de forma organizada, indicando:
    -   Intentos restantes.
    -   La palabra con las letras adivinadas y espacios en blanco.
    -   Las letras incorrectas que ya has utilizado.
-   **Límite de 6 Intentos**: Tienes 6 vidas para resolver el misterio.
-   **Validación de Entrada**: El programa se asegura de que solo introduzcas una letra válida en cada turno.
-   **Sin Dependencias Externas**: Solo necesitas tener Python instalado. ¡No requiere librerías adicionales más allá de las estándar!

## 🚀 ¿Cómo Jugar?

Para ejecutar el juego, solo necesitas tener **Python 3** instalado en tu sistema.

1.  **Clona o descarga este repositorio:**
    ```bash
    git clone [https://github.com/TU_USUARIO/TU_REPOSITORIO.git](https://github.com/TU_USUARIO/TU_REPOSITORIO.git)
    cd TU_REPOSITORIO
    ```
    > Reemplaza `TU_USUARIO` y `TU_REPOSITORIO` con tu nombre de usuario y el nombre de tu repositorio.

2.  **Ejecuta el script desde tu terminal:**
    ```bash
    python ahorcado.py
    ```

3.  **¡Adivina la palabra!** Sigue las instrucciones en la pantalla, introduce una letra y presiona `Enter`.

## 🛠️ Estructura del Código

El código está organizado en funciones para una mejor legibilidad y mantenimiento:

-   `obtener_palabra_secreta()`: Selecciona y devuelve una palabra al azar de la lista interna.
-   `mostrar_tablero()`: Dibuja la interfaz del juego en la consola.
-   `jugar_ahorcado()`: Contiene la lógica principal del juego, gestionando los turnos, las entradas del usuario y las condiciones de victoria o derrota.

### Personalización

¿Quieres añadir más palabras o cambiar las existentes? ¡Es muy fácil! Simplemente edita la lista `palabras` dentro de la función `obtener_palabra_secreta()` en el archivo `ahorcado.py`:

```python
def obtener_palabra_secreta():
    """Selecciona una palabra al azar de una lista predefinida."""
    # ¡Añade tus propias palabras aquí!
    palabras = ['python', 'programacion', 'github', 'repositorio', 'codigo']
    return random.choice(palabras).lower()
```

## 💻 Tecnologías Utilizadas

-   **Lenguaje**: ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
-   **Librerías**:
    -   `random` (para la selección de palabras).

---

¡Gracias por visitar este proyecto! Si tienes alguna sugerencia o encuentras un error, no dudes en abrir un *issue*.
