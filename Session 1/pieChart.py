import matplotlib.pyplot as plt

categories = ['Category A', 'category B', 'Category C', 'Category D', 'Category E']

percentages = [25, 50,8, 12,5]
explode = [0.1, 0.1, 0.1, 0.1, 0.1]
colors = ['lightgreen', 'aqua', 'red', 'lime','yellow']

plt.pie(percentages, explode = explode, labels = categories, colors = colors, shadow = True)
plt.title("Percentage Distribution")
plt.legend(categories)
plt.show()
