import sympy
t, s = sympy.symbols('t s')
Sfunc = input("Enter the frequency varying function: ")
f1 = sympy.sympify(Sfunc)
ILaplacef1 = sympy.inverse_laplace_transform(f1, t, s, noconds=True)
print("Laplace Transform of", Sfunc, "is", ILaplacef1)
