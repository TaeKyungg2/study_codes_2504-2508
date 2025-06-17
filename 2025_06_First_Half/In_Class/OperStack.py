"""
피연산자(숫자)는 스택에 넣는다. 그럼, 스택의 상태는 [3, 5, 2]이다.
연산자를 만나면 스택에서 피연산자 두 개를 꺼내서 계산한다.
연산자 *를 만났으므로 스택에서 2와 5를 꺼내서 곱한다. 5 * 2 = 10
결괏값을 스택에 저장한다. 이제 스택의 상태는 [3, 10]다.
그다음에 연산자 +가 있으므로 스택에서 10과 3을 꺼내서 더한다. 답은 13이다.
"""
from Stack import MyStack
from formulaStack import formulaMatch
def postorder(string):
    #if not formulaMatch(str):return
    st=MyStack()
    for i in string :
        if i.isdigit():st.push(i)
        elif i!=' ':
            right=st.pop()
            left=st.pop()
            sic=str(left)+str(i)+str(right)
            v=eval(sic)
            st.push(v)
    return st.pop()

print(postorder('3 5 2 * +'))