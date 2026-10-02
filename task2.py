from matplotlib import pyplot as plt

for y in range(0,6):
    x = [1, 6] 
    plt.plot(x, [y, y])
    
plt.xlabel("x - axis")
plt.ylabel("y - axis")
plt.ylim(0)
plt.title("my first graph!")
plt.show()