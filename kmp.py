#This library contains the function "fa" for calculating the failure 
#array of the KMP algorithm, as well as the KMP matching algorithm in 
#the function "match".

def fa(S): #calculate the  kmp failure array for string S

    F = [0] #the initialized failure array
    m = len(S)
    i = 1; j = 0

    while i < m:
        if S[i] == S[j]:
            F.append(j+1)
            i+=1; j+=1
        elif j > 0:
            j = F[j-1]
        else:
            F.append(0)
            i+=1

    return F


#KMP algorithm for matching string S in text T using failure array F
def match(S,T,F):

    if T == "": return False
    if S == "": return False

    m = len(S); n = len(T)
    i = 0; j = 0

    while i < n:
        if T[i] == S[j]:
            if j == m-1:
                return True
            else:
                i+=1; j+=1
        else:
            if j > 0:
                j = F[j-1]
            else:
                i+=1

    return False
