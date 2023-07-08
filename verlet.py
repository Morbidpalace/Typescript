# verlet.py

#--------------------------------------------------------------------------

#Verlet's numerical method to solve a MAS simple harmonic motion system.

#--------------------------------------------------------------------------

import numpy as np
from scipy.special import logsumexp

k, m, = 0.5, 3.2
x_0 = 0.01
v_0 = 0.01
x = x_0
v = v_0
a = -0.0015625
for h in np.arange(0, 7, 0.001):
	a = (-k/m)*x
	x = x+(h*v)+(0.5*(h**2)*((-k/m)*x))
	v = v + ((a + ((-k/m)*x))*(0.5)*h)
	print("x= {:.3f}, v= {:.3f}, h= {:.3f}, a= {:.3f} " .format(x, v, h, a))


