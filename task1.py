from matplotlib import pyplot as plt

x = [1, 1, 3, 5, 5, 6, 6, 6, 7, 7, 9, 9, 7, 7, 7, 10, 10, 10, 12, 12]
y = [0, 5, 5, 5, 0, 0, 5, 3, 3, 5, 5, 0, 0, 3, 0, 0, 5, 0, 5, 0]

plt.plot(x, y)
plt.xlabel("x - axis")
plt.ylabel("y - axis")
plt.ylim(0)
plt.title("my first graph!")
plt.show()
