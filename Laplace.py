import sympy
from sympy import pretty_print
t, s = sympy.symbols('t s')
Tfunc = input("Enter the time varying function: ")
f1 = sympy.sympify(Tfunc)
Laplacef1 = sympy.laplace_transform(f1, t, s, noconds=True)
pretty_print(Laplacef1)