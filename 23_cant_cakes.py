
def cakes(recipe, available):
    min_cakes=10000
    
    for clave in recipe:
        if clave in available:
            posibles_cakes= available[clave]//recipe[clave]
            if posibles_cakes >= 1: # si hay mas disponible de lo q lleva la receta 
                if min_cakes> posibles_cakes:
                    min_cakes= posibles_cakes
            else:
                return 0
        else:
            return 0
    return min_cakes
# Ejemplos de uso
print(cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}))  # Imprime: 2
print(cakes({'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}, {'sugar': 500, 'flour': 2000, 'milk': 2000}))  # Imprime: 0