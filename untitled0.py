import numpy as np
import matplotlib.pyplot as plt

a = np.array([[0.023392, 0.006976],
              [0.029888, 0.039104],
              [0.033328, 2.198592],
              [0.065632, 5.864992],
              [0.801120, 76.550461]])


xlabels = ['a', 'b', 'c', 'd', 'e', ]
plt.xticks([0,1,2,3,4], xlabels)


plt.plot(a[:,0])
plt.plot(a[:,1])
plt.show()