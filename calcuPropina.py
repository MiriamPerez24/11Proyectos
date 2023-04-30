# Solicitar factura total y número de personas
factura_total = float(input("Ingrese la factura total: "))
num_personas = int(input("Ingrese el número de personas: "))

# Calcular la propina para 18%, 20% y 25%
propina_18 = round(factura_total * 0.18, 2)
propina_20 = round(factura_total * 0.20, 2)
propina_25 = round(factura_total * 0.25, 2)
# Mostrar las propinas
print(f"Propina del 18%: {propina_18}")
print(f"Propina del 20%: {propina_20}")
print(f"Propina del 25%: {propina_25}")

propina = int(input("Ingrese el porcentaje de propina: "))

#Costo total por persona 
costo_total = round(factura_total+(factura_total * (propina / 100)), 2)

# Pedir porcentajes de pago para cada persona
porcentajes_pago = []
for i in range(num_personas):
    porcentaje = float(input(f"Ingrese el porcentaje de pago para la persona {i+1}: "))
    porcentajes_pago.append(porcentaje)

# Calcular pago para cada persona según porcentajes de pago
pagos = []
for porcentaje in porcentajes_pago:
    pago = round(costo_total * (porcentaje / 100), 2)
    pagos.append(pago)

print(f"\nTotal a pagar:{costo_total}\nLos pagos de cada persona son: {pagos}")


