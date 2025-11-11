
#Write a program that will calculate the number of trailing zeros in a factorial of a given number.
def zeros(n):
    factorial=1
    for i in range(1,n+1):
        factorial*=i
    contador = 0 
    
    for c in  str(factorial)[::-1]: # recorrer el str del factorial al reves
        if c == '0':
            contador +=1
        else:
            break
    return contador 

print(zeros(5))  # Imprime: 1
print(zeros(100))  # Imprime: 24