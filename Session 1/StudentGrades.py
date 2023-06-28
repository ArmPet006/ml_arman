import matplotlib.pyplot as plt

subject = ['Math', 'Science', 'History', 'English', 'Physics', 'Biology', 'Geography', 'Chemistry']
grade = [80,90,75,85,92,88,82,78]

plt.bar(subject, grade, color = ['red', 'blue', 'green', 'aqua', 'orange', 'pink', 'yellow', 'skyblue'])

plt.xlabel('subject')
plt.ylabel('grade')
plt.title('Student Grades')
plt.show()

summ = 0
for i in range(len(grade)):
    summ += grade[i]

print('The Average is', summ/len(grade))

countt = 0

for i in grade:
    if i >= 80:
        countt += 1

print((countt * 100)/len(grade))
