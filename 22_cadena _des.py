
def pig_it(text):
    return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())

print(pig_it('Hello world !'))  # Imprime: 'elloHay orldway !'
print(pig_it('Pig latin is cool'))  # Imprime: 'igPay atinlay siay oolcay'
print(pig_it('This is my string'))  # Imprime: 'hisTay siay ymay tringsay'

#Verifica si el "string" x contiene solo letras y números (sin símbolos ni espacios)