
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
    return det