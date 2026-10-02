from matplotlib import pyplot as plt

x = [1, 1, 1, 2, 1, 2, 4, 4, 3, 4, 5, 4, 4, 6, 7, 6.6, 6]
y = [0, 5, 3, 5, 3, 0, -1, 5, 4, 3, 4, 5, -1, 0, 5, 3, 5]

plt.plot(x, y)
plt.xlabel("x - axis")
plt.ylabel("y - axis")
plt.ylim(0)
plt.title("my first graph!")
plt.show()