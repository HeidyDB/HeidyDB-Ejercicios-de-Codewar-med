def tower_builder(n_floors):
    result = []
    for i in range(n_floors):
        estrellas = '*' * (2 * i + 1)
        espacios = ' ' * (n_floors - i - 1)
        result.append(espacios + estrellas + espacios)
    return result
pisos = tower_builder(5)
for piso in pisos:
    print(piso) 