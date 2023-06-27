import matplot.pyplot as plt

years = [2015, 2016,  2017, 2018, 2019, 2020, 2021, 2022, 2023]
population = [8.5, 9.1, 10.5, 5.3, 8.6, 6.8, 9.6, 5.1, 6]

plt.plot[years, population, marker = 'o', linestyle = '--', color = 'red')
plt.xlabel('Years')
plt.ylabel("Population (in billions)")
plt.title("Population Growth Over Years")
plt.show()
