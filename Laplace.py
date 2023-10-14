import sympy
from sympy import pretty_print
t, s = sympy.symbols('t s')
# Get user input for the function
Sfunc = input("Enter the function in terms of t: ")
f1 = sympy.sympify(Sfunc)
Laplace_f1 = sympy.laplace_transform(f1, t, s, noconds=True)
pretty_print(Laplace_f1)
