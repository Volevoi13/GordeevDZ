import matplotlib.pyplot as plt
import numpy as np

glavniy = np.random.uniform(0, 10, (5, 2))

smech = [p + np.random.normal(0, 1, (10, 2)) for p in glavniy]

means = np.array([s.mean(axis=0) for s in smech])

plt.scatter(glavniy[:, 0], glavniy[:, 1], color='black', label='исходные',)
plt.scatter(means[:, 0], means[:, 1], color='red', marker='*', label='Центр')


for i in range(5):
    plt.scatter(smech[i][:, 0], smech[i][:, 1], color='gray')
    plt.errorbar(means[i, 0], means[i, 1], xerr=np.std(smech[i][:, 0]), yerr=np.std(smech[i][:, 1]), ecolor='red', capsize=3)

plt.legend()
plt.grid()
plt.show()