# pedimos un texto 

texto = input("Ingrese un texto: ")

"""metodo split() sirve para dividir la 
cadena de texto en palabras, utilizando 
el espacio como separador"""

# El metodo len() se utiliza para contar las palabras

resultado = len(texto.split())

print("Contiene "+str(resultado) + " palabras")

#str significa que lo convertimos en una cadena de texto