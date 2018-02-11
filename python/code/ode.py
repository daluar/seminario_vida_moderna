from scipy.special import gamma, airy
from scipy.integrate import odeint, ode
import numpy as np

import matplotlib.pyplot as plt

y0 = np.empty((2,))

y0[0] = 1.0 / 3 ** (2. / 3) / gamma(2. / 3)
y0[1] = - 1.0 / 3 ** (1. / 3) / gamma(1. / 3)

def func(y, z):
    return np.array([y[1], z * y[0]])

z = np.arange(0, 4., 0.01)

y_ana = airy(z)[0]
y_odeint = odeint(func, y0, z)[:,0]

def func2(z, y):
    return np.array([y[1], z * y[0]])

y_ode = []
z_ode = []

edo = ode(func2)
edo.set_integrator('dopri5')
edo.set_initial_value(y0, t=0)
dt = 0.01
while edo.successful() and edo.t < 4.:
    z_ode.append(edo.t + dt)
    y_ode.append(edo.integrate(edo.t + dt))

y_ode = np.array(y_ode)
z_ode = np.array(z_ode)

plt.figure()
plt.plot(z, y_ana, label=r"$\mathrm{Ai}(z)$")
plt.plot(z, y_odeint, label=r"$\mathtt{odeint}$", ls="--")
plt.plot(z_ode, y_ode[:,0], label=r"$\mathtt{ode}$", ls=":")
plt.legend(loc="best")
plt.grid(True)

plt.figure()
plt.semilogy(z, np.abs(y_odeint - y_ana))
plt.semilogy(z_ode, np.abs(y_ode[:,0] - airy(z_ode)[0]))
plt.grid(True)

plt.show()
plt.close('all')