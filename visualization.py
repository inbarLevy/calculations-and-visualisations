from math_functions import *
import matplotlib.pyplot as plt
import numpy as np

# 1
y = create_exp_values(-1, 5)
x = np.linspace(-1, 5, 100)
plt.xlabel('x')
plt.ylabel('y')
plt.title('exp')
plt.xticks(np.arange(-1, 6))
plt.yticks()
plt.xlim(-1, 5)
plt.plot(x, y, 'm--', linewidth=3)
plt.grid()
plt.show()

# 2
y1 = np.cos(np.linspace(-5, 5, 100))
y2 = create_sin_values(-5, 5)
x = np.linspace(-5, 5, 100)
plt.xlabel('x')
plt.ylabel('y')
plt.title('sin & cos')
plt.xticks(np.arange(-5, 6))
plt.yticks()
plt.xlim(-5, 5)
plt.plot(x, y1, 'green')
plt.plot(x, y2, 'blue')
plt.grid()
plt.show()

# 3
y1 = create_x_power(-5, 5, 1)
y2 = create_x_power(-5, 5, 2)
y3 = create_x_power(-5, 5, 3)
x = np.linspace(-5, 5, 100)
plt.xlabel('x')
plt.ylabel('y')
plt.title('1st, 2nd and 3rd degree Polynomials')
plt.xticks(np.arange(-5, 6))
plt.yticks()
plt.xlim(-5, 5)
plt.plot(x, y1, 'gs', markersize=3.5)
plt.plot(x, y2, 'b--', linewidth=2.5)
plt.plot(x, y3, 'ro', markersize=3.5)
plt.grid()
plt.show()

# 4
student, grade = create_students_grades(15)
plt.xlabel('student')
plt.ylabel('grade')
plt.xticks(student)
plt.title('Student grades')
plt.bar(student, grade, color='c', width=0.6)
plt.show()

# 5
student, grade = create_students_grades(12)
plt.xlabel('grade')
plt.yticks(student)
plt.title('Student grades')
plt.barh(student, grade, color='pink')
plt.show()

# 6
y = np.random.poisson(4, size=150)
x = np.linspace(0, 7, 150)
plt.xlabel('x')
plt.ylabel('y')
plt.title('poisson')
plt.xticks(np.arange(0, 8))
plt.xlim(0, 7)
plt.plot(x, y, 'gray', linewidth=3)
plt.grid()
plt.show()
