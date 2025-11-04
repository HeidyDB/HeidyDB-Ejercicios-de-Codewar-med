def longest(a1, a2):
    combined = a1 + a2
    unique_chars = set(combined) # eliminar duplicados
    sorted_chars = sorted(unique_chars) # ordenar caracteres
    result = ''.join(sorted_chars)# unir en una cadena
    return result

print (longest("aretheyhere", "yestheyarehere"))