import random

def obtener_palabra_secreta():
    """Selecciona una palabra al azar de una lista predefinida."""
    palabras = ['python', 'programacion', 'desarrollo', 'inteligencia', 'artificial', 'tecnologia', 'ordenador']
    return random.choice(palabras).lower()

def mostrar_tablero(palabra_mostrada, intentos_restantes, letras_erroneas):
    """Muestra el estado actual del juego: la palabra, los intentos y las letras erróneas."""
    print("\n" + "="*30)
    print(f"Intentos restantes: {intentos_restantes}")
    print(f"Palabra: {' '.join(palabra_mostrada)}")
    if letras_erroneas:
        print(f"Letras incorrectas: {', '.join(sorted(letras_erroneas))}")
    print("="*30)

def jugar_ahorcado():
    """Función principal para ejecutar el juego del ahorcado."""
    palabra_secreta = obtener_palabra_secreta()
    palabra_mostrada = ['_'] * len(palabra_secreta)
    intentos_restantes = 10
    letras_adivinadas = set()
    letras_erroneas = set()

    print("¡Bienvenido al Juego del Ahorcado! 🤠")
    print(f"La palabra secreta tiene {len(palabra_secreta)} letras.")

    while intentos_restantes > 0:
        mostrar_tablero(palabra_mostrada, intentos_restantes, letras_erroneas)

        # Solicitar una letra al usuario
        letra = input("Introduce una letra: ").lower()

        # --- Validación de la entrada ---
        if not letra.isalpha() or len(letra) != 1:
            print("❌ Error: Por favor, introduce una sola letra.")
            continue
        
        if letra in letras_adivinadas or letra in letras_erroneas:
            print("⚠️ Ya intentaste con esa letra. ¡Prueba con otra!")
            continue

        # --- Comprobar si la letra está en la palabra ---
        if letra in palabra_secreta:
            letras_adivinadas.add(letra)
            print(f"✅ ¡Bien hecho! La letra '{letra}' está en la palabra.")
            # Actualizar la palabra mostrada
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i] == letra:
                    palabra_mostrada[i] = letra
        else:
            letras_erroneas.add(letra)
            intentos_restantes -= 1
            print(f"❌ ¡Incorrecto! La letra '{letra}' no está. Te quedan {intentos_restantes} intentos.")

        # --- Comprobar si el jugador ha ganado o perdido ---
        if '_' not in palabra_mostrada:
            print("\n🎉 ¡Felicidades! ¡Has adivinado la palabra! 🎉")
            print(f"La palabra era: {palabra_secreta.upper()}")
            break
    
    else: # Este 'else' se ejecuta solo si el bucle 'while' termina sin un 'break'
        mostrar_tablero(palabra_mostrada, intentos_restantes, letras_erroneas)
        print("\n😟 ¡Oh no! Te has quedado sin intentos.")
        print(f"La palabra secreta era: {palabra_secreta.upper()}")

if __name__ == "__main__":
    jugar_ahorcado()