import random

# Generar un número aleatorio entre 1 y 50
numMisterioso = random.randint(1, 50)

intentos = 0
continuar = True

# Ciclo principal del juego
while continuar:
    # Pedir al usuario que adivine un número
    adivin = input("Adivina un número entre 1 y 50: ")
    intentos += 1
    
    # Validar que la entrada del usuario sea un número
    if not adivin.isdigit():
        print("Ingresa un número válido.")
        continue
        
    # Convertir la entrada del usuario a un número entero
    adivin = int(adivin)
    
    # Validar que la adivinanza esté dentro del rango correcto
    if adivin < 1 or adivin > 50:
        print("El número debe estar entre 1 y 50.")
        continue
    
    # Comparar la adivinanza con el número secreto
    if adivin == numMisterioso:
        print(f"Felicidades, adivinaste el número en {intentos} intentos.")
        continuar = False
    else:
        # Si la adivinanza es incorrecta, preguntar al usuario si quiere seguir jugando
        respuesta = input("Lo siento, adivinaste el número equivocado. ¿Quieres seguir jugando? (s/n)")
        if respuesta.lower() == "n": #Lo convierte a minuscula
                continuar = False
                print(f"Suerte para la proxima, el numero era: {numMisterioso} ")
         
      
