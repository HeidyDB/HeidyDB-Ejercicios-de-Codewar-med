def find_outlier(integers):
    resultado=[]
    for persona in integers: # par [edad, handicap] in integers
        
        if persona[0] >= 55 and persona[1] > 7:
            resultado.append("Senior")
        else:
            resultado.append("Open")

    return resultado


print(find_outlier([[45, 12],[55,21],[19, -2],[104, 20]]))



#be a senior, a member must be at least 55 years old and have a 
# handicap greater than 7. In this croquet club, handicaps range 
# from -2 to +26; the better the player the lower the handicap.

#Input
#Input will consist of a list of pairs. Each pair contains information
#  for a single potential member. Information consists of an integer 
# for the person's age and an integer for the person's handicap.

#Output
#Output will consist of a list of string values (in Haskell and C: 
# Open or Senior) stating whether the respective member is to be
#  placed in the senior or open category.
