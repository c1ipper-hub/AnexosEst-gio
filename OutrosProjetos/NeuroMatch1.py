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


print(t_max, dt, tau, el, vr, vth, r, i_mean)

np.random.seed(2020)

# initialize step_end
stepEnd = int(t_max/dt)
n = 50
# initialize list with v0 in every position
v_list = [el] * n
# initializing the figure

plt.figure()
plt.title('Multiple realizations of $V_m$')
plt.xlabel('time (s)')
plt.ylabel('$V_m$ (V)')


for step in range(stepEnd):
    # compute value of t
    t = step * dt
    for j in range(0, n):
        # compute value of i at this time step
        #i = i_mean * (1 + np.sin((2 * np.pi / 0.01) * tau))
        i = i_mean * (1 + 0.1 * (t_max/dt)**0.5 * (2 * np.random.rand() - 1))

        # integration of dv/dt. In other words We want the function of V(t).
        v_list[j] = v_list[j] + (dt/tau) * (el - v_list[j] + r*i)

    v_mean = sum(v_list) / n

    v_var_n = [(x - v_mean)**2 for x in v_list]

    v_var = sum(v_var_n)/(n-1)

    v_std = np.sqrt(v_var)

    # plot the simulation
    plt.plot([t] * n, v_list, 'k.', alpha=0.1)
    plt.plot(t, v_mean, 'C0.', alpha=0.8)
    plt.plot(t, v_std + v_mean, 'C2.', alpha=0.8)
    plt.plot(t, v_mean - v_std, 'C2.', alpha=0.8)


plt.show()
