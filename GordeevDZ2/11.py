import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = x
y2 = x*2
y3 = x*3
y4 = x**2
y5 = 2 * x**2
plt.figure(figsize=(10, 5))
plt.plot(x, y1,  color ='blue')
plt.plot(x, y2,  color = 'red')
plt.plot(x, y3,  color = (1, 1, 0))
plt.plot(x, y4,  color = (0, 1, 1))
plt.plot(x, y5,  color = 'green')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
