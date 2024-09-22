# Importing required libraries ====

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# Radar Chart ====

labels = np.array(["A", "B", "C", "D", "E"])
data = np.array([4, 5, 3, 4, 2])

angles = np.linspace(0, 2 * np.pi, len(labels), endpoint = False)
data = np.concatenate((data, [data[0]]))
angles = np.concatenate((angles, [angles[0]]))

plt.polar(angles, data, marker = "o")
plt.fill(angles, data, alpha = 0.25)
plt.title("Radar Chart")
plt.show()


# Heatmap ====

data_1 = np.random.rand(10, 10)

sns.heatmap(data_1)
plt.title("Heatmap", annot = True)
plt.show()


# Violin Plot ====

data_2 = [np.random.normal(0, std, 100) for std in range(1, 4)]

sns.boxplot(data = data_3)
plt.title("Box Plot")
plt.xlabel("Category")
plt.ylabel("Values")
plt.show()


# Bar Chart ====

country = ['USA', 'Canada', 'Australia', 'India']
cases = [4500, 4200, 5200, 49000]
colors = ['green', 'blue', 'purple', 'red']


plt.bar(country, cases, color = colors)
plt.title('cases')
plt.xlabel('Country')
plt.ylabel('Cases')
plt.show()
