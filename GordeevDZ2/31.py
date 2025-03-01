import matplotlib.pyplot as plt
import numpy as np

x = ['Матан', 'Физика', 'Начерталка', 'Введение в авиацию']
y = [3, 4, 4, 3]

plt.bar(x, y, color =['blue', 'red', 'green', (0, 1, 1)])

plt.xlabel("оценки")


plt.show()
