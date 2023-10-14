import sympy as sp
from sympy import pretty_print
s, t = sp.symbols('s t')
Laplace_transform_str = input("Enter the Laplace-transformed function in terms of 's': ")
try:
    Laplace_transform = sp.sympify(Laplace_transform_str)
    inverse_transform = sp.inverse_laplace_transform(Laplace_transform, s, t)
    pretty_print(inverse_transform)
except sp.SympifyError:
    print("Invalid input. Please enter a valid Laplace-transformed function.")
