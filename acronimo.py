nombre = input("Por favor ingrese el significado completo de una organización o concepto: ")

# Dividimos la entrada del usuario en palabras
palabras = nombre.split()

# Recopilamos la primera letra de cada palabra y la convertimos en mayúscula
acr = "".join([palabra[0].upper() for palabra in palabras])

print(f"El acrónimo para '{nombre}' es: {acr}")