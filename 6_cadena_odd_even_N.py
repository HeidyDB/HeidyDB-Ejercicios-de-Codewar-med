
#You are given an array (which will have a length of at 
# least 3, but could be very large) containing integers. 
# The array is either entirely comprised of odd integers 
# or entirely comprised of even integers except for a
#  single integer N. Write a method that takes the array
#  as an argument and returns this "outlier" N.

#Examples
#[2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)

#[160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even 

def find_outlier(integers):
    # validar entrada mínima
    if not isinstance(integers, (list, tuple)):
        raise TypeError("Se espera una lista o tupla de enteros")
    if len(integers) < 3:
        return ("el arreglo debe tener al menos 3 elementos")

    # Determiimeros 3 elementosnar la paridad mayoritaria usando los pr
    first_three = integers[:3] # Obtener los primeros 3 elementos
    # Contar cuántos son pares
    evens = sum(1 for x in first_three if x % 2 == 0)
    # Si hay al menos 2 pares, la mayoría es par; si no, la mayoría es impar
    majority_is_even = evens >= 2

    # Buscar y devolver el outlier: el que no coincide con la paridad mayoritaria
    for x in integers:
        if (x % 2 == 0) != majority_is_even:
            return x

    # Si no se encontró outlier (teóricamente no debe pasar según el enunciado)
    return None


if __name__ == "__main__":
    examples = [
        [2, 4, 0, 100, 4, 11, 2602, 36],  # outlier 11 (impar)
        [160, 3, 1719, 19, 11, 13, -21],   # outlier 160 (par)
        [1, 2, 3],                         # outlier 2 (par)
        [2, 6, 8, 10, 3],                 # outlier 3 (impar)
        [4, 1],                         # outlier 1 (impar)
    ]

    for arr in examples:
        print(f"Entrada: {arr} -> Outlier: {find_outlier(arr)}")
            
   
    