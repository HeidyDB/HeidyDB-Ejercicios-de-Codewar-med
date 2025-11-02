#our task is to convert strings to how they would be written by 
# Jaden Smith. The strings are actual quotes from Jaden Smith, 
# but they are not capitalized in the same way he originally typed
#  them.

#Example:

#Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
#Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Ar

def to_jaden_case(texto):
    word= texto.split() # dividir en palabras
    word_capitalized= [w.capitalize() for w in word] # capitalizar cada palabra
    texto= " ".join(word_capitalized) # unir las palabras capitalizadas
    return texto

print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
