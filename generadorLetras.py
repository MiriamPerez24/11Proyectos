# Definir la lista de canciones con el nombre, artista y letra
canciones = [
    {"nombre": "EW", "artista": "Joji", "letra": "When it's lovely, I belive in anything..."},
    {"nombre": "Afterthougth", "artista": "Joji", "letra": "Lately, I'been slippin'away from you..."},
    {"nombre": "Ojitos lindos ", "artista": "Bad Bunny", "letra": "Hace mucho tiempo le hago caso al corazón..."},
    {"nombre": "Un coco ", "artista": "Bad Bunny", "letra": "A ver si me cae un coco en la cabeza y me borra mi vida entera..."},
    {"nombre": "TSQ", "artista": "Humbe", "letra": "Pero sigo creyendo. Que no somos amigos cercanos..."},
]

# Imprimir la lista de canciones para que el usuario pueda elegir
print("Lista de canciones:")
for i, cancion in enumerate(canciones):
    print(f"{i+1}. {cancion['nombre']} - {cancion['artista']}")

# Pedir al usuario que seleccione una canción
opcion = int(input("Ingrese el número de la canción que desea ver: "))
cancion_seleccionada = canciones[opcion-1]

# Imprimir la letra de la canción seleccionada
print(f"Letra de {cancion_seleccionada['nombre']} - {cancion_seleccionada['artista']}:")
print(cancion_seleccionada['letra'])

# Pedir al usuario que ingrese el nombre del artista para ver solo sus canciones
artista = input("Ingrese el nombre del artista para ver sus canciones: ")
canciones_artista = [cancion for cancion in canciones if cancion['artista'].lower() == artista.lower()]

# Imprimir la lista de canciones del artista seleccionado
print(f"Canciones de {artista}:")
for i, cancion in enumerate(canciones_artista):
    print(f"{i+1}. {cancion['nombre']}")

# Pedir al usuario que seleccione una canción del artista seleccionado
opcion = int(input("Ingrese el número de la canción que desea ver: "))
cancion_seleccionada = canciones_artista[opcion-1]

# Imprimir la letra de la canción seleccionada
print(f"Letra de {cancion_seleccionada['nombre']} - {cancion_seleccionada['artista']}:")
print(cancion_seleccionada['letra'])
