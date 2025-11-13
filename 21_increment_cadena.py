
def increment(s):
    """Incrementa el último número en una cadena o en una lista.
    
    Comportamiento:
    - Si `s` es una lista: modifica su último elemento o añade '1' si no hay número.
      - Si el último elemento es int -> lo incrementa (ej: 9 -> 10).
      - Si el último elemento es str y termina en dígitos -> incrementa el sufijo numérico.
      - Si no hay sufijo numérico se añade '1' como nuevo elemento.
    - Si `s` es una cadena: incrementa el sufijo numérico preservando ceros.
    """
    # --- Caso: lista ---
    if isinstance(s, list):
        arr = s.copy()
        if len(arr) == 0:
            return ['1']
        last = arr[-1]
        # si es entero
        if isinstance(last, int):
            arr[-1] = last + 1
            return arr
        # si es string
        if isinstance(last, str):
            # buscar sufijo numérico al final
            j = len(last) - 1
            while j >= 0 and last[j].isdigit():
                j -= 1
            suf = last[j+1:]
            if suf == '':
                # no hay número al final -> añadir '1' como nuevo elemento
                arr.append('1')
                return arr
            # hay sufijo numérico -> incrementarlo y preservar ceros
            ancho = len(suf)
            nuevo_suf = str(int(suf) + 1).zfill(ancho)
            arr[-1] = last[:j+1] + nuevo_suf
            return arr
        # otros tipos: convertir a str y tratar como no-numérico
        arr.append('1')
        return arr

    # --- Caso: string u otros tipos ---
    cadena = str(s)
    if len(cadena) == 0:
        return '1'
    
    # encontrar dónde empieza el sufijo numérico (si existe)
    i = len(cadena) - 1
    while i >= 0 and cadena[i].isdigit():
        i -= 1
    prefijo = cadena[:i+1]
    numero = cadena[i+1:]
    if numero == '': #no habia numero al final 
        return cadena + '1' 
    ancho_numero = len(numero)
    nuevo_numero = str(int(numero) + 1).zfill(ancho_numero) # mantener ceros a la izquierda
    return prefijo + nuevo_numero
    


print(increment(['a', 'b', 'c', 4]))  # Imprime: ['a', 'b', 'c', 5]
print(increment(['x', 'y', 'z']))     # Imprime: ['x', 'y', 'z', '1']
print(increment(['item1', 'item2', 9]))  # Imprime: ['item1', 'item2', 10]
print(increment([]))  # Imprime: ['1']
print(increment("foobar099"))  # Imprime: 'foobar100'
print(increment("test"))  # Imprime: 'test1'
print(increment("abc123"))  # Imprime: 'abc124'
print(increment(["ff002"]))  # Imprime: ['ff003']
print(increment(['item1', 'item2', '008']))  # Imprime: ['1']
