from sympy import *
from sympy.plotting import plot3d

x,y=symbols('x y')
f=2*x+3*y
plot3d(f)

x=symbols('x')
expr=x**2/x**5
print(expr)