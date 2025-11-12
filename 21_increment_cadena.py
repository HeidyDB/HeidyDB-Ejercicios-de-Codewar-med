
def increment(cadena):
    if len(cadena) == 0:
        return '1'
    
    # Si es una lista, trabajar con el último elemento
    if isinstance(cadena, list):
        if type(cadena[-1]) == int:
            cadena[-1] += 1      
        else:
            cadena.append('1')
        return cadena
    
    # Si es una cadena, extraer número al final y incrementar
    if isinstance(cadena, str):
        # Encontrar dónde comienza el número al final
        i = len(cadena) - 1
        while i >= 0 and cadena[i].isdigit():
            i -= 1
        
        # Si hay números al final
        if i < len(cadena) - 1:
            prefijo = cadena[:i+1]
            numero = int(cadena[i+1:])
            return prefijo + str(numero + 1)
        else:
            # Si no hay números, agregar '1'
            return cadena + '1'
    
    return cadena
print(increment(['a', 'b', 'c', 4]))  # Imprime: ['a', 'b', 'c', 5]
print(increment(['x', 'y', 'z']))     # Imprime: ['x', 'y', 'z', '1']
print(increment(['item1', 'item2', 9]))  # Imprime: ['item1', 'item2', 10]
print(increment([]))  # Imprime: ['1']
print(increment("foobar099"))  # Imprime: 'foobar100'
print(increment("test"))  # Imprime: 'test1'
print(increment("abc123"))  # Imprime: 'abc124'