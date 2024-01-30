texto_star_wars = """
Star Wars es una franquicia de películas de ciencia ficción concebida por el cineasta estadounidense George Lucas. 
La saga comenzó con una película que se estrenó el 25 de mayo de 1977 y rápidamente se convirtió en un fenómeno mundial. 
La historia se desarrolla en una galaxia ficticia en una época indefinida. Los personajes principales incluyen a Luke Skywalker, 
la princesa Leia, Han Solo, Darth Vader y el maestro Yoda, entre otros. La Fuerza es un concepto central en la saga, una energía mística que da poder a los Jedi y a los Sith.
"""

# Dividir el texto en palabras
palabras = texto_star_wars.split()

# Contador para contar la cantidad de veces que aparece la palabra "fuerza"
contador_fuerza = 0

for palabra in palabras:
    # Eliminar signos de puntuación para comparar correctamente
    palabra = palabra.strip(",.").lower()
    if palabra == "fuerza":
        contador_fuerza += 1

print("La palabra 'fuerza' aparece", contador_fuerza, "veces en el texto.")
