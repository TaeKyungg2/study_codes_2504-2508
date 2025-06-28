n=int(input())
Fib=[0]*(n+1)
def fib(n):
    if n==0 or n==1:
        Fib[n]=1
    elif Fib[n]!=0:
        return Fib[n]
    else:
        Fib[n]=fib(n-1)+fib(n-2)
    return Fib[n]

print(fib(n))