import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

subject = [1,2,3,4,5,6,7,8]
grade = [80,90,75,85,92,88,82,78]
students = [10,12,24,16,13,18,20,11]
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
xs = subject
ys = grade
zs = students
ax.scatter(xs, ys, zs, marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
