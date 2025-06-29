import numpy as np
# from sympy.plotting import plot3d
from sympy import integrate,symbols,lambdify
from math import sin



# a=[1,2,3,4,5]
# print(sum(a))
x,y=symbols('x y')
# plot3d((x-y)**2)
print(integrate(x**-5,x))
f = lambdify(x, x**7)
print(sin(3.14))