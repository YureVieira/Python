import matplotlib.pylab as plt
import numpy as np

#-inicio,-fim,-quantidade
x = np.linspace(-np.pi, np.pi, 20)
plt.plot(x, np.sin(x))
print x

plt.xlabel('Angle [rad]')
plt.ylabel('sin(x)')
plt.axis('tight')
plt.show()
