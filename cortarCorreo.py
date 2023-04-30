import re

# Pedir al usuario que ingrese su correo electrónico
correo_electronico = input("Ingrese su dirección de correo electrónico: ")
domain = re.search("@[\w.]+", correo_electronico).group()
domain = domain.replace(".com", "").replace("@", "")#remplaza el .com y el arroba


popular_domains = ["gmail", "yahoo", "hotmail", "aol", "outlook"]

if any(domain in popular for popular in popular_domains):
    print(f"Hey {correo_electronico.split('@')[0]},veo que su correo esta registrado en {domain.capitalize()}. ¡Eso es genial!")
else:
    print(f"Hey {correo_electronico.split('@')[0]}, parece que tiene tu propia configuracion personalizada en {domain.capitalize()}. ¡Impresionate!")




