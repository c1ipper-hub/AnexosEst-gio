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

n = 1000
# num of "spaces"
t_range = np.arange(0, t_max, dt)
step_end = len(t_range)
# initialize matrix whit "n" neurons and "step_end" time steps
v_n = el * np.ones([n, step_end])
# initialize all the values of i in a 50 by 149 matrix
i =  i_mean * (1 + 0.1 * (t_max/dt)**0.5 * (2 * np.random.random([n, step_end]) - 1))
n_bins = 50



for step, t in enumerate(t_range):
    # skip first iteration
    if step == 0:
        continue
    # compute v_n
    v_n[:, step] = v_n[:, step - 1] + (dt / tau) * (el - v_n[:, step - 1] + r * i[:, step])


# plot histrogram at time t = t_max
plt.figure()
plt.title('histogram')
plt.xlabel('$V_m$ (V)')
plt.ylabel('frequency')
plt.hist(v_n[:,-1], n_bins, label =f' t={t_max} s',
         histtype='stepfilled', linewidth=0)
plt.hist(v_n[:, int(step_end/10)], n_bins, label=f't= {t_max / 10} s',
         histtype='stepfilled', linewidth=0)
plt.legend()
plt.show()
