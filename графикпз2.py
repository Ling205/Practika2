import numpy as np
import matplotlib.pyplot as plt
plt.title('График')
plt.xlabel('X1')
plt.ylabel('X2')
plt.xlim(0,10)
plt.ylim(0,10)
plt.plot([0, 4], [1, 0])
plt.plot([0, 6], [6, 0])
plt.plot([0, 9], [2, 2])
plt.plot([0, 10], [0,0])
plt.text(2, 0.6, 'X1 + 4X2 >= 4',fontsize=10)
plt.text(3, 3, 'X1 + X2 <= 6',fontsize=10)
plt.text(8, 2.1, 'X2 >= 2',fontsize=10)
plt.text(8, 0.3, 'X1 >= 0',fontsize=10)
plt.grid()
plt.show()
#Корешников Н. А.
#номер группы: 8