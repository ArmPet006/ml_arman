import matplotlib.pyplot as plt

years = [2015,2016,2017,2018,2019,2020,2021,2023]
population = [8.5,8,7.5,7,6.5,6,5.5,5,4.5]

plt.plot(years, population, marker = 'o', linestyle = '--', color= 'red')
plt.xlabel("Year")
plt.ylabel("Population (in billions)")
plt.title("Population Growth Over Years")
plt.show()
