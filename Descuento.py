valor = float(input('Valor del producto: '))

# Procso
if valor >100:
    descuento = 0.10
else:
    descuento = 0
pagar = valor*(1-descuento)

# Salida
print(pagar)
