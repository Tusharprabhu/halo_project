import matplotlib.pyplot as plt
import numpy as np


def plot_user_function():
    """
    Takes user input for a function and generates a graph for that function.
    """
    try:
        # Get user input for the function
        function_str = input("Enter a function (e.g., 'x**2 + 2*x + 1'): ")

        # Parse and create a callable function
        x = np.linspace(-10, 10, 400)
        user_function = lambda x: eval(function_str)

        # Generate y values
        y = user_function(x)

        # Plot the user-defined function
        plt.figure(figsize=(8, 6))
        plt.plot(x, y, label=function_str)
        plt.xlabel('x')
        plt.ylabel(f'{function_str}(x)')
        plt.title("User-Defined Function Plot")
        plt.grid(True)
        plt.legend()
        plt.show()

    except Exception as e:
        print("An error occurred:", e)


# Call the function to plot the user-defined function
plot_user_function()
