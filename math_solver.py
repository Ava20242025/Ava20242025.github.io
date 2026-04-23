import matplotlib.pyplot as plt

# Solve a simple problem: y = x^2
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

plt.plot(x, y)
plt.title("My Math Result")
plt.savefig('diagram.png') # This creates the photo
print("Math solved and diagram saved!")
