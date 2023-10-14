import sympy
x = sympy.symbols('x')
func_str = input("Enter the function in terms of 'x': ")
try:
    func = sympy.sympify(func_str)
    n = 20
    x0 = 0

    result = func.subs(x, x0)

    for i in range(1, n):
        result += sympy.diff(func, x, i).subs(x, x0) * (x - x0)**i / sympy.factorial(i)

    sympy.pretty_print(result)
except sympy.SympifyError:
    print("Invalid input. Please enter a valid mathematical expression.")

