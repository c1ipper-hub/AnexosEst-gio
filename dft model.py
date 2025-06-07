import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import *
import math

from fontTools.misc.cython import returns

""" !!! Sigmoid Function !!!"""
# initializing variables for the sigmoid function x, slope and thresh
def sigmoid_function(x, slope, tresh):
    sigmoid = 1 / (1 + np.exp(slope *(tresh - x)))
    return sigmoid
x = np.linspace(-10, 10, 100)
slope = 100
thresh = 0



""" !!! Gauss Function !!!"""
# initializing gaussian and variables mu, sigma
def gauss_function(x, mu, sigma):
    gauss = (np.pi*sigma) * np.exp(-0.5*((x-mu)/sigma)**2)
    return gauss
mu = 0
sigma = 3
# x is the same as before

""" !!! Dynamical field size !!!"""
# field size
L = 10
# step
dx = 0.1
# numb of neurons (odd)
N = int( L / dx)
# Field
x1 = np.linspace(-L, L, N)

print(len(x1))

""" !!!Temporal discretisation of the simulation!!!"""
# simulation final
T = 20
# time step
dt = 0.01
# number of time steps
M = int(T/dt)


#print(len(x1))

""" !!! Neural Field !!!"""
# time constant
tau = 1
# resting state
h = 0.01
# Dynamical field
u_field = -h * np.ones(N)

print(u_field.shape)
print(len(u_field))

"""!!! coupling Function !!!"""
###################################### isto é tipo o kernel #######################################################
ample = 1
width = 0.85
global_inhib = 0.5

w = ample * gauss_function(x1, mu, width) - global_inhib

w_hat = fft(w)

# stimulus s(t)
bump1 = 1 * gauss_function(x1, +5, 1)
bump2 = 1 * gauss_function(x1, -5, 1)

stimuli = np.zeros([N, M])
for step in range(int(M/2)):
    stimuli[:, step] = bump1 + bump2


plt.figure(figsize=(10, 5))

for i in range(M):
    # Firing rate
    f = sigmoid_function(u_field, slope, thresh)
    f_hat = np.fft.fft(f)

    # Convolution in frequency domain
    conv = dx * np.fft.ifftshift(np.real(np.fft.ifft(f_hat * w_hat)))

    # Field update
    u_field = u_field + (dt / tau) * (-u_field + conv + stimuli[:, i] - h)

    # Visualization every 5 steps
    if i % 5 == 0:
        plt.clf()
        plt.plot(x1, u_field, "k", linewidth=2.0, label="Campo Neuronal")
        plt.plot(x1, stimuli[:,i], "b", linewidth=2.0, label="Estímulo")
        plt.xlabel("Campo Dinâmico", fontsize=16)
        plt.ylabel("Ativação", fontsize=16)
        plt.title(f"Neural Field Simulation (Step {i})", fontsize=20)
        plt.legend()
        plt.pause(0.02)

# Close all plots
plt.close()

# Final Results
plt.figure(figsize=(10, 5))
plt.plot(x1, u_field, "k", linewidth=2.0, label="Campo Dinâmico Final")
plt.plot(x1, np.zeros(N), "--k", linewidth=2.0, label="Resting State")
plt.xlabel("Campo Dinâmico", fontsize=16)
plt.ylabel("Ativação", fontsize=16)
plt.title("Neural Field Simulation", fontsize=20)
plt.legend()
plt.show()