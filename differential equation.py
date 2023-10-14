import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Function that defines the differential equation
def user_ode(t, y, equation):
    try:
        # Define the variables for evaluating the user-provided equation
        variables = {'t': t, 'y': y}
        result = eval(equation, variables)
        return result
    except:
        return 0  # Return 0 in case of an error

# Prompt the user for the differential equation
equation = input("Enter the differential equation (e.g., 't - y'): ")

# Prompt the user for initial conditions
initial_t = float(input("Enter the initial t: "))
initial_y = float(input("Enter the initial y: "))

# Set the time span
t_span = (initial_t, initial_t + 10)

# Solve the ODE using solve_ivp
sol = solve_ivp(user_ode, t_span, [initial_y], args=(equation,), t_eval=np.linspace(initial_t, initial_t + 10, 100))

# Extract the solution
t = sol.t
y = sol.y[0]

# Plot the solution
plt.figure(figsize=(8, 6))
plt.plot(t, y, label='Solution y(t)')
plt.xlabel('Time (t)')
plt.ylabel('y(t)')
plt.title('Solution of the ODE')
plt.legend()
plt.grid(True)
plt.show()
