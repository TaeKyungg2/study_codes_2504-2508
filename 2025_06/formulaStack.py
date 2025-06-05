class MyStack:
    def __init__(self, size=10):
        if size < 10:
            self.size = 10
        self.stack = []
        for i in range(0, size):
            self.stack.append(0)
        self.top = -1
        self.size = size

    def isFull(self):
        if self.size - 1 == self.top:
            return True
        else:
            return False

    def push(self, data):
        if self.isFull():
            print(f"stack can't eat {data}")
            return
        self.top += 1
        self.stack[self.top] = data

    def print(self):
        for i in range(0, self.size):
            print(self.stack[i], end=" ")
        print()

    def pop(self):
        if self.isEmpty():
            return "Stack empty"
        temp = self.stack[self.top]
        self.stack[self.top] = 0
        self.top -= 1
        return temp

    def isEmpty(self):
        if self.top == -1:
            return True
        return False

    def peek(self):
        if self.isEmpty():
            print("can't peek")
            return
        return self.stack[self.top]


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


