import matplotlib.pyplot as plt

# 15.1
x_values = range(1, 6)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap='inferno', s=10)

ax.set_title("Cubes")
ax.set_xlabel("Value")
ax.set_ylabel("Cube of Value")

ax.axis([0, 5, 0, 70])

plt.show()

# 15.2
x_values = range(1, 1001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap='inferno', s=10)

ax.set_title("Cube of Values")
ax.set_xlabel("Value")
ax.set_ylabel("Cube of Values")

ax.axis([0, 1001, 0, 1_000_000_000])

plt.show()
