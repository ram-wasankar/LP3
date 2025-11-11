# Gradient Descent to find local minima of y = (x + 3)^2 starting from x = 2

# Import required library
import matplotlib.pyplot as plt

# Define the function and its derivative
def f(x):
    return (x + 3)**2

def df(x):
    return 2 * (x + 3)

# Initialize parameters
x = 2           # starting point
alpha = 0.1     # learning rate
iterations = 50 # number of iterations

# Store values for plotting
x_values = [x]
y_values = [f(x)]

# Gradient Descent Iteration
for i in range(iterations):
    grad = df(x)
    x = x - alpha * grad
    x_values.append(x)
    y_values.append(f(x))

# Display final result
print("Local minima occurs at x =", round(x, 4))
print("Minimum value of function y =", round(f(x), 4))

# Plot the function and the descent path
plt.figure(figsize=(8,5))
X = [i for i in range(-6, 3)]
Y = [(val + 3)**2 for val in X]
plt.plot(X, Y, label="y = (x + 3)^2", color='blue')
plt.scatter(x_values, y_values, color='red', label='Gradient descent path')
plt.title("Gradient Descent to find local minima of y = (x + 3)^2")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
