
def det_gauss(matrix):
    # copia para no modificar la original
    n = len(matrix)
    if n == 0:
        raise ValueError("La matriz no puede estar vacía")
    if any(len(row) != n for row in matrix):
        raise ValueError("La matriz debe ser cuadrada")
    # trabajar con floats
    A = [list(map(float, row)) for row in matrix]
    det = 1.0
    for i in range(n):
        # pivoteo parcial: buscar fila con max |A[row][i]|
        pivot_row = max(range(i, n), key=lambda r: abs(A[r][i]))
        if abs(A[pivot_row][i]) < 1e-12:
            return 0.0
        if pivot_row != i:
            A[i], A[pivot_row] = A[pivot_row], A[i]
            det *= -1  # permutar filas cambia signo
        pivot = A[i][i]
        det *= pivot
        # normalizar y eliminar hacia abajo
        for j in range(i+1, n):
            factor = A[j][i] / pivot
            # restar factor * fila i de fila j
            for k in range(i+1, n):
                A[j][k] -= factor * A[i][k]
            # opcional: establecer A[j][i] = 0
    return round(det)


# Ejemplos de prueba
if __name__ == "__main__":
    # matriz 2x2: det = 1*4 - 2*3 = -2
    m1 = [[1, 2], [3, 4]]
    print(f"det({m1}) = {det_gauss(m1)}")  # -2
    
    # matriz 3x3
    m2 = [[2, 0, 1], [3, 4, -1], [1, 2, 0]]
    print(f"det({m2}) = {det_gauss(m2)}")  # 11
    
    # matriz identidad: det = 1
    m3 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    print(f"det({m3}) = {det_gauss(m3)}")  # 1
    
    # matriz singular (det = 0)
    m4 = [[1, 2], [2, 4]]
    print(f"det({m4}) = {det_gauss(m4)}")  # 0