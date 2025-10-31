def alphabet_position(text):
    diccionario= "abcdefghijklmnñopqrstuvwxyz"
    texto = text.lower()
    resultado= []
    
    for letra in texto:
        if letra in diccionario:
            resultado.append(diccionario.index(letra)+1)
    return resultado

numero_de_letra= alphabet_position("Hola Mundo")
print(numero_de_letra)