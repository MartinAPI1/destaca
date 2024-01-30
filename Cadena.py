cadena = "pedro pepe pica papas"
contador_vocales = 0

for caracter in cadena:
    if caracter.lower() in "aeiou":
        contador_vocales += 1

print("El número de vocales en la cadena es:", contador_vocales)
