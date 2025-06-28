from Stack import MyStack

sta=MyStack()
opr={'+':1,'-':1,'/':2,'*':2}

def postfix(formula):
    result=""
    for i in formula:
        if i.isdigit():
            result+=i
            continue
        if i==' ':
            continue
        if not sta.isEmpty() and opr[i]<opr[sta.peek()]:
            result+=sta.pop()
        else : 
            sta.push(i)
        result+=' '
    else : 
        while not sta.isEmpty():
            result+=sta.pop()
    print(result)
postfix("33 + 5 * 2")


            
