
def hamming(n):
    """Retorna el n-ésimo número de Hamming (n >= 1)"""
    if n <= 0:
        raise ValueError("n debe ser >= 1")
    
    # lista para almacenar números de Hamming
    h = [1]
    i2 = i3 = i5 = 0  # índices para multiplicadores 2, 3, 5
    
    while len(h) < n:
        # próximos candidatos
        next2 = h[i2] * 2
        next3 = h[i3] * 3
        next5 = h[i5] * 5
        
        # tomar el mínimo
        next_h = min(next2, next3, next5)
        h.append(next_h)
        
        # incrementar índices (puede haber empates)
        if next_h == next2:
            i2 += 1
        if next_h == next3:
            i3 += 1
        if next_h == next5:
            i5 += 1
    
    return h[n-1]

# Ejemplos
print(hamming(1))    # 1
print(hamming(10))   # 12
print(hamming(15))   # 24
print(hamming(20))   # 36