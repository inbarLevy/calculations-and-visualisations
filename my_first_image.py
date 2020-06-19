import matplotlib.pyplot as plt
import numpy as np

rand_matrix = np.arange(0, 256)
rand_matrix.resize((16, 16))
transpose_rand_matrix = np.transpose(rand_matrix)
plt.imshow(rand_matrix, cmap='gray')
plt.show()
plt.imshow(transpose_rand_matrix, cmap='gray')
plt.show()

# cmap- map scalar data to RGBA (red, green, blue, alpha) colors, in this case to alpha=grey.
# In the first time, the numbers increased along the lines, so the black color started from the top.
# The second time, after transposing the matrix, the numbers increased along the columns,
# so the black color started from the left.



