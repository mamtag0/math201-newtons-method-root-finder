import numpy as np
import matplotlib.pyplot as plt

# Define the function and its derivative
def f(x):
    return np.exp(x) + x**2 - 4

def f_prime(x):
    return np.exp(x) + 2*x

# Newton's Method
def newton_method(x0, tolerance=1e-6, max_iter=100):
    x = x0
    steps = []
    for i in range(max_iter):
        fx = f(x)
        fpx = f_prime(x)
        if abs(fpx) < 1e-10:
            print("Derivative too small, stopping.")
            break
        x_new = x - fx / fpx
        steps.append((i+1, round(x, 6)))
        if abs(x_new - x) < tolerance:
            break
        x = x_new
    return round(x, 6), steps

# Initial guess
root, steps = newton_method(-1)

# Output results
print("Root (approx):", root)
print("Iterations:")
for step in steps:
    print(f"Step {step[0]}: x = {step[1]}")

# Plotting the function
x_vals = np.linspace(-4, 2, 500)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label="f(x) = e^x + x^2 - 4")
plt.axhline(0, color='black', linestyle='--')
plt.axvline(root, color='red', linestyle='--', label=f"Root ≈ {root}")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Graph of f(x) with Root Highlighted")
plt.legend()
plt.grid(True)
plt.show()