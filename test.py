import sys
from PyQt4 import QtGui

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

objects = ('Python', 'Bs', 'C', 'D', 'E', 'F')
y_pos = np.arange(len(objects))
performance = [10, 3, 15, 8, 4, 2]
# error = np.random.rand(len(objects)) xerr=error,

ax.barh(y_pos, performance, align='center', alpha=0.5, color='green')
ax.set_yticks(y_pos)
ax.set_yticklabels(objects)
ax.set_ylabel('Objects')
ax.invert_yaxis()
ax.set_xlabel('Performance')
ax.set_title('Test')

plt.show()
# pic = QtGui.QLabel()
# pic.setPixmap(QtGui.QPixmap('piechart.png'))
# pic.show()