from cProfile import label

import numpy as np
import matplotlib.pyplot as plt
from pyparsing import alphas

t_max = 150e-3   #second
dt = 1e-3        #second
tau = 20e-3      #second
el = -60e-3      #milivolt
vr = -70e-3      #milivolt
vth = -50e-3     #milivolt
r = 100e6        #ohm
i_mean = 25e-11  #ampere

# set random number generator
np.random.seed(2020)

# initialize step_end, t_range, v
step_end = int(t_max/dt) - 1
n = 50
t_range = np.linspace(0, t_max, num=step_end, endpoint=False)
# initialize matrix whit "n" neurons and "step_end" time steps
v_n = el * np.ones([n, step_end])
# initialize all the values of i in a 50 by 149 matrix
i =  i_mean * (1 + 0.1 * (t_max/dt)**0.5 * (2 * np.random.random([n, step_end]) - 1))


# loop for step_end times
for step in range(1, step_end):

    v_n[:, step] = v_n[:, step - 1] + (dt / tau) * (el - v_n[:, step - 1] + r * i[:, step])

# compute mean for each neuron across time
mean_neuron = np.mean(v_n, axis = 1)
# compute mean for each time step for all neurons
mean_timeStep = np.mean(v_n, axis = 0)
# std_d
std_d = (np.var(v_n, axis = 0))**.5

# Plot membrane potential
plt.figure()
plt.title('Multiple realizations of $V_m$')
plt.xlabel('time (s)')
plt.ylabel('$V_m$ (V)')

plt.plot(t_range, v_n.T,'k', alpha=.3)

plt.plot(t_range, v_n[-1],'k', alpha=.3, label='V(t)')
plt.plot(t_range, mean_timeStep,'C0', alpha=.8, label='Mean')
plt.plot(t_range, mean_timeStep + std_d,'C3', alpha=.8, label='Std')
plt.plot(t_range, mean_timeStep + (- std_d),'C3', alpha=.8)
plt.legend()
plt.show()
print(n)
print(len(t_range))
print(v_n)
print(i)