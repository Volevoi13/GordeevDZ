import matplotlib.pyplot as plt
import numpy as np

x = ["5 созыв", "6 созыв", "7 созыв", "8 созыв"]

ay = [300, 250, 340, 320]
by = [50, 90, 40, 60]
cy = [40, 55, 39, 20]
dy = [40, 65, 25, 30]

plt.stackplot(x, ay, by, cy, dy, labels=["Единая Россия", "КПРФ", "ЛДПР", "Справедливая Россия"])

plt.ylabel("Места в Думе")
plt.title("Распределение партий")

plt.show()