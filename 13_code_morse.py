
# Diccionario Morse normal
morse_table = {
    'A': '.-',    'B': '-...',  'C': '-.-.', 'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',  'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',  'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',  'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',  'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',  'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': '/'
}
def morse_to_text(morse_code):
    morse_to_char = {v: k for k, v in morse_table.items()} # diccionario inverso
    palabras = morse_code.strip().split("   ")  # separar palabras (3 espacios)
    texto_decodificado = []
    for palabra in palabras:
        letras = palabra.split()  # separar letras (1 espacio)
        palabra_decodificada = ''.join(morse_to_char.get(letra, '?') for letra in letras)
        texto_decodificado.append(palabra_decodificada)
    return ' '.join(texto_decodificado)


print(morse_to_text(".... . .-.. .-.. ---   .-- --- .-. .-.. -.."))