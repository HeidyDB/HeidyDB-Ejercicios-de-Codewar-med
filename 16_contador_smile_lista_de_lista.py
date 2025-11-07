def count_smileys(arr):
    contador_smiles = 0
    for cara in arr:
        # Carita de 2 caracteres
        if len(cara) <= 2:
            if (cara[0] == ':' or cara[0] == ';') and (cara[1] == ')' or cara[1] == 'D'):
                contador_smiles += 1
        # Carita de 3 caracteres
        if len(cara) <= 3:
            if (cara[0] == ':' or cara[0] == ';') and (cara[1] == '-' or cara[1] == '~') and (cara[2] == ')' or cara[2] == 'D'):
                contador_smiles += 1
    return contador_smiles


print(count_smileys([':D',':~)',';~D',':)']) ) # Imprime: 4)