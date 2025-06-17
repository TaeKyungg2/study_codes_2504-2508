from Stack import MyStack

st = MyStack()


def formulaMatch(formula):
    for i in formula:
        if i == "(":
            st.push(i)
        if i == ")":
            st.pop()
        if st.isEmpty() and formula[-1] != i:
            print("No Match")
            return
    if st.isEmpty():
        print("Match formula")
    else:
        print("no Match")