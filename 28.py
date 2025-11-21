def prox_ej(lst, n):
    """Devuelve el siguiente elemento en la lista después de n, o None si n es el último."""
    try:
        index = lst.index(n)
        if index + 1 < len(lst):
            return lst[index + 1]
        else:
            return None
    except ValueError:
        return None