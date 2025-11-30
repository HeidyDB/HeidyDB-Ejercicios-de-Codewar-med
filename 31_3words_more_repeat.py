def top_3_words(text):
    """Devuelve las tres palabras más comunes en el texto, ignorando mayúsculas y puntuación."""
    import re
    from collections import Counter

    # Convertir a minúsculas y encontrar palabras
    words = re.findall(r"\b[a-zA-Z']+\b", text.lower())

    # Contar la frecuencia de cada palabra
    word_counts = Counter(words)

    # Obtener las tres palabras más comunes
    most_common = word_counts.most_common(3)

    # Devolver solo las palabras, no sus conteos
    return [word for word, count in most_common]
