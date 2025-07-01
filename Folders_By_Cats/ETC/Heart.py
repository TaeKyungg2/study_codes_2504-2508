from sympy import symbols,plot_implicit
x,y=symbols('x y')
f=(x**2+y**2-1)**3-x**2*y**3
plot_implicit(f,(x,-2,2),(y,-2,2),line_color='#EE82EE')