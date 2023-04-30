import random

opciones = ["piedra", "papel", "tijera"]

while True:
    jugador = input("Piedra, papel o tijera? (o 'q' para salir): ").lower()

    if jugador == "q":
        break
    
    if jugador not in opciones:
        print("Opción no válida. Por favor intenta de nuevo.")
        continue
    
    computadora = random.choice(opciones)

    print(f"Jugador: {jugador}")
    print(f"Computadora: {computadora}")

    if jugador == computadora:
        print("Empate!")
    elif (jugador == "piedra" and computadora == "tijera") or (jugador == "papel" and computadora == "piedra") or (jugador == "tijera" and computadora == "papel"):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")