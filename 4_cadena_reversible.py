
def cadena_reversible(walk):
    #determinar si una cadena es reversible
    if len(walk) % 2 != 0:
        return "cadena impar. No es reversible"

    n = len(walk) - 1
    for i in range(0, len(walk)//2):
        if walk[i] != walk[n]:
            return "cadena no reversible"
        n -= 1
    
    return "esta cadena es reversible"

print(cadena_reversible(['n','s','n','s','n','n','s','n','s','n']))
print(cadena_reversible(['n','s','n','s','n','s','n','s']))
print(cadena_reversible(['n']))