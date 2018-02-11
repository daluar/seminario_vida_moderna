import function
import numpy as np
from scipy.linalg import inv as hazme_inversa
import matplotlib.pyplot as plt
from math import *

e = function.mi_funcion(5, z=3)
z = np.linspace(0, 1, 3)
i = hazme_inversa(np.eye(3))
plt.plot(z)
e = sqrt(e)
