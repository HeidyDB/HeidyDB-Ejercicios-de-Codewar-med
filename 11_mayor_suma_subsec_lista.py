def max_sequence(arr):
    suma_max = 0
    suma_actual = 0 
    for numero in arr:
        suma_actual += numero
        if suma_actual <0:
            suma_actual=0
        if suma_actual > suma_max:
            suma_max = suma_actual
    return suma_max

print (max_sequence([-2,1,-3,4,-1,2,1,-5,4]))