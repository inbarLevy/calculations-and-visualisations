import matplotlib.pyplot as plt
import numpy as np

bin_matrix = np.random.rand(100)
bin_matrix = [0 if i <= 0.5 else 1 for i in bin_matrix]
bin_matrix = np.array(bin_matrix)
bin_matrix = bin_matrix.reshape((10, 10))
np.savetxt('image.txt', bin_matrix, fmt='% 4f')

image = np.loadtxt('image.txt')
print(image.shape)


# Because the matrix includes only binary numbers, the average will necessarily be between 0 and 1, since it cannot be
# lesser than the minimum value-0, or greater than the maximum value -1.
image_avg = np.average(image)
if image_avg > 0.5:
    print('More ones than zeros')
else:
    print('More zeros than ones')


image = np.transpose(image)


amount_of_element = [image_avg * 100, (1 - image_avg) * 100]
if image_avg > 0.5:
    element = [1, 0]
else:
    element = [0, 1]
plt.xlabel('element')
plt.ylabel('amount of element')
plt.xticks(element)
plt.title('Ratio between number of zeros and number of ones')
plt.bar(element, amount_of_element, color='orange', width=0.4)
plt.show()
