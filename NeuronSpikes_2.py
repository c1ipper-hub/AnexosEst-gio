import numpy as np
import matplotlib.pyplot as plt
from fontTools.varLib.models import nonNone
from numpy.ma.core import shape



def plot_all(t_range, v_n, spikes=None, spikes_mean=None):
    import numpy as np
    import matplotlib.pyplot as plt

    plt.figure()

    # Plot simulations and sample mean
    ax1 = plt.subplot(3, 1, 1)
    for j in range(n):
        plt.scatter(t_range, v_n[j], color="k", marker=".", alpha=0.01)
    plt.plot(t_range, v_mean, 'C1', alpha=0.8, linewidth=3)
    plt.ylabel('$V_m$ (V)')


    if spikes is not None:
        # Plot spikes
        plt.subplot(3, 1, 2, sharex=ax1)
        # for each neuron j: collect spike times and plot them at height j
        for j in range(n):
            # makes an array of times the neuron spiked for each neuron for better computation
            times = np.array(spikes[j])
            # plots the times the j neuron spiked (times) against the coresponding neuron (does this 500 times)
            plt.scatter(times, j * np.ones_like(times), color="C0", marker=".", alpha=0.2)
        plt.ylabel('neurónio')
    if spikes_mean is not None:
        # Plot firing rate
        plt.subplot(3, 1, 3, sharex=ax1)
        plt.plot(t_range, spikes_mean)
        plt.xlabel('Tempo (s)')
        plt.ylabel('Taxa (Hz)')

        plt.tight_layout()
    plt.show()

t_max = 150e-3  # second
dt = 1e-3  # second
tau = 20e-3  # second
el = -60e-3  # milivolt
vr = -70e-3  # milivolt
vth = -50e-3  # milivolt
r = 100e6  # ohm
i_mean = 25e-11  # ampere

# pseudorandom number generator
np.random.seed(2020)

n = 500

t_range = np.arange(0, t_max, dt)

step_end = len(t_range)

v_n = el * np.ones([n, step_end])

i = i_mean * (1 + 0.1 * (t_max / dt) ** (0.5) * (2 * np.random.random([n, step_end]) - 1))

spikes_dic = {x: [] for x in range(n)}
spikes_n = np.zeros(step_end)

for step, t in enumerate(t_range):
    if step == 0:
        continue
    v_n[:, step] = v_n[:, step - 1] + (dt / tau) * (el - v_n[:, step - 1] + r * i[:, step])

    # boolean with values where v_[step, step] > vth
    spiked = (v_n[:, step] > vth)

    # change values of v_n on the current step, that spiked, to the resting level.
    v_n[spiked, step] = vr

        # np.where gives the index where the boolean value is true. [0]: only rows e: [T, F, F, T] -> [1, 4]
    for j in np.where(spiked)[0]:
        # store the time that j neuron spiked
        spikes_dic[j] += [t]
        # add 1 for each neuron that spiked at a certain time(step)
        spikes_n[step] += 1

spikes_mean = spikes_n / n
v_mean = np.mean(v_n, axis=0)

plot_all(t_range, v_n, spikes=spikes_dic, spikes_mean=spikes_mean)

# print functions
# print(t_range, "\n", step_end, "\n",shape(v_n))
