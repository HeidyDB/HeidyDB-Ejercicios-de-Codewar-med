#Complete the solution so 
# that it splits the string into pairs of two characters. 
# If the string contains an odd number of characters then it 
# should replace the missing second character of the final pair 
# with an underscore ('_').

#Examples:

# 'abc' =>  ['ab', 'c_']
# 'abcdef' => ['ab', 'cd', 'ef']


def solution(s):
    if len(s)%2!=0:
        s= s + "_"  # si es impar el str agregar _
    nuevo_arr = []
    for i in range(0, len(s), 2):
        nuevo_arr.append(str(s[i]+s[i+1]))
        
    return nuevo_arr

print (solution('abc'))
print (solution('abcddfghgdedd'))
print (solution(''))