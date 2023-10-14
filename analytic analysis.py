import sympy as sp

# Define a complex variable
z = sp.symbols('z')
a=int(input(" enter the secound order co efficient"))
b=int(input(" enter the first order co efficient"))
c=int(input(" enter the constant co efficient"))
h=int(input(" enter the real part of z"))
k=int(input(" enter the imaginary part if z"))


# Define a complex function, for example, f(z) = z^2 + 2z + 1
f = a*z**2 + b*2*z + c

# Compute the derivative of the function
f_prime = sp.diff(f, z)

# Compute the integral of the function
f_integral = sp.integrate(f, z)

# Simplify the results
f_prime_simplified = sp.simplify(f_prime)
f_integral_simplified = sp.simplify(f_integral)

# Display the results
print("Original Function: f(z) =", f)
print("Derivative: f'(z) =", f_prime_simplified)
print("Integral: ∫f(z)dz =", f_integral_simplified)

# Evaluate the function at a specific complex point, e.g., z = 2 + 3i
z_value = h + 5j
f_at_z_value = f.subs(z, z_value)
print(f"f({z_value}) =", f_at_z_value)
