from Stack import MyStack

sta=MyStack()
opr={'+':1,'-':1,'/':2,'*':2}
def postfix(formula):
    for i in formula:
        if i.isdigit():
            print(i,end=' ')
            continue
        if i==' ':continue
        if not sta.isEmpty() and opr[i]<opr[sta.peek()]:
            print(sta.pop())
        else : sta.push(i)
    else : 
        while not sta.isEmpty():
            print(sta.pop())
postfix("3 + 5 * 2")


            
