
# Newton's Method – Math 201 Root Finder

This project uses Newton’s Method to approximate the **negative root** of the equation:

**e^x = 4 - x²**

---

## Function Setup

We rewrote the equation in the form:

f(x) = e^x + x² - 4  
f'(x) = e^x + 2x

Newton’s Method formula used:

xₙ₊₁ = xₙ - f(xₙ) / f'(xₙ)

This formula helps refine the guess until we reach a root value that's accurate to six decimal places.

---

##  What This Code Does

- Starts with an initial guess (x₀ = -1)
- Applies Newton's Method in a loop
- Stops when the change is very small (less than 0.000001)
- Displays all iterations and final root
- Plots the function with the root highlighted on the graph

---

## How to Run This

1. Make sure Python is installed  
2. Install the required libraries:

