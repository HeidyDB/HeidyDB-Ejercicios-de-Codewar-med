def solution(text, ending):
    if len(ending)>=2:
       if text[-1].lower() == ending[1].lower():
          return True
       else:
         return False
    else:
       return  False
    
resultado= solution("abcd", "a")
print(resultado)


#Complete the solution so that it returns true 
#if the first argument(string) passed in ends
#with the 2nd argument (also a string).