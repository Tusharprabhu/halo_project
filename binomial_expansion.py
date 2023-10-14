import sympy as sp
from sympy import pretty_print
# Define the symbolic variables
x, n = sp.symbols('x n')

# Get user input for the function
user_function = input("Enter a function in terms of 'x' and 'n' (e.g., (1+x)**n): ")

try:
    # Convert the user input into a SymPy expression
    user_expr = sp.sympify(user_function)

    # Calculate the binomial expansion
    binomial_expansion = sp.expand(user_expr, power_base=True)

    # Print the binomial expansion
    print("Binomial Expansion of", user_function, "is:")
    pretty_print(binomial_expansion)

except sp.SympifyError:
    print("Invalid input. Please enter a valid mathematical expression.")