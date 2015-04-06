#Writing functions to modify strings to find potential matches 
#recorded in different formats

def repSpace(S): #in case a space in the model name appears hyphenated

    Sd = ""
    for char in S:
        if char == " ": Sd+="-"
        else: Sd+=char

    return Sd

def rmSpace(S): #in case the model name appears contracted

    Sd = ""
    for char in S:
        if char == " ": continue
        else: Sd+=char

    return Sd

    
