import scipy.integrate as integrate
import scipy.special as special
import numpy as np

x = np.linspace(0, 4.5, 50)
y = special.jv(2.5, x)
result1 = integrate.trapz(y, x)
result2 = integrate.simps(y, x)
## resultado
# quad:  1.1178179380783249
# trapz: 1.11767339787
# simps: 1.11781225777