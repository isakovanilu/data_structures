def char_count(string):
    # create an object to return at the end
    result = {}
    
    # loop through the string
    for i in string.lower():
        # if the char is in the result, add 1 to the result value
        if isinstance(i, str) and not (i.isspace()):
            if i in result:
                result[i] += 1
            else:
                result[i] = 1
    # return the result
    return result
            
print(char_count('Heh ll oo'))
        
    