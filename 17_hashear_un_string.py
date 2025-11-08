
def generate_hashtag(s):
    #your code here
    if len(s) == 0:
        return False
    else:
        primera_mayuscula= s.title()
        sin_espacio=primera_mayuscula.replace(" ", "")
        sin_esp_delante= sin_espacio.strip()
        resultado= "#" + sin_esp_delante
        if len(resultado) > 140 :
            return False
        return resultado
    
print(generate_hashtag("    Hello     world   "))  # Imprime: #Helloworld