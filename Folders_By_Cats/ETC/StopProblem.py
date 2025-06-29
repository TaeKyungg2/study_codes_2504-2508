def P(input):
    return input,input

def H(P):
    if P[0](P[1])==False:
        return 'stuck'
    else : return 'not stuck'

def A(express):
    if type(express)==int:
        return express
    else : return False

def B(express):
    if type(express)==str:
        return express
    else : return False

def N(H):
    if H=='not stuck' : return 'smile'
    elif H =='stuck' : return False

def X(input):
    return N(H(P(input)))

print(X(X))