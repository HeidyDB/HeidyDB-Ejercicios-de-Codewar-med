
#Implement a function that adds two numbers together 
# and returns their sum in binary. The conversion can
#  be done before, or after the addition.

#The binary number returned should be a string.

#xamples:(Input1, Input2 --> Output (explanation)))

def suma_en_binario(a,b):
    suma=a+b
    return bin(int(abs(suma))).replace("0b","") #replace para quitar el prefijo 0b que indica que es binario

print(suma_en_binario(1.8,1))
print(suma_en_binario(5,-9))