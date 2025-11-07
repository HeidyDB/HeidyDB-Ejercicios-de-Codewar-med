def count_smileys(arr):
    contador_smiles = 0
    # Unir todos los caracteres en una sola cadena
    cadena = ''.join(arr)
    # Revisar todas las posiciones posibles para caritas de 2 o 3 caracteres
    for i in range(len(cadena)):
        # Carita de 2 caracteres
        if i+1 < len(cadena):
            if (cadena[i] == ':' or cadena[i] == ';') and (cadena[i+1] == ')' or cadena[i+1] == 'D'):
                contador_smiles += 1
        # Carita de 3 caracteres
        if i+2 < len(cadena):
            if (cadena[i] == ':' or cadena[i] == ';') and (cadena[i+1] == '-' or cadena[i+1] == '~') and (cadena[i+2] == ')' or cadena[i+2] == 'D'):
                contador_smiles += 1
    return contador_smiles

print(count_smileys([':', ')', ';', '(', ';', '}', ':', '-', 'D']))  # Imprime: 2
            
