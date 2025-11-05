
def duplicate_encode(word):
    nuevo_str= ""
    for char in word:
        if word.lower().count(char.lower())>1:
            nuevo_str += ")"
        else:
            nuevo_str += "("
    return nuevo_str

print(duplicate_encode("Success"))    

#The goal of this exercise is to convert a string to a new string
# where each character in the new string is "(" if that character   
# appears only once in the original string, or ")" if that character
# appears more than once in the original string. Ignore capitalization
 