# Pedir al usuario que ingrese cinco palabras
palabras = []
for i in range(5):
    palabra = input("Ingrese una palabra: ")
    palabras.append(palabra)

# Verificar si alguna de las palabras es un palíndromo
for palabra in palabras:
    if palabra == palabra[::-1]:
        print(f"{palabra} es un palíndromo.")
        
    elif palabra != palabra[::-1]:
        print(f"{palabra} no es un palíndromo.")
        