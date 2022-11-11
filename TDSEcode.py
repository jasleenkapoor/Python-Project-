#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 11:56:33 2022

@author: jasleen
"""

import numpy as np
import matplotlib.pyplot as plt
from findiff import FinDiff
from scipy.sparse.linalg import inv
from scipy.sparse import eye, diags
import matplotlib.animation as animation

x_array = np.linspace(-7, 7, 500)

k = 10 
v_x = k * x_array ** 2
psi = np.exp(-(x_array)**2)

fig, ax = plt.subplots()

ax.plot(x_array, np.abs(psi)**2)
ax.set_xlabel("x [arb units]")
ax.set_ylabel("$|\Psi(x, t=0)|^2$", color="C0")

ax_twin = ax.twinx()
ax_twin.plot(x_array, v_x, color='C1')
ax_twin.set_ylabel("$V(x)$", color="C1")


def f(x):
    return np.sin(x)

# Define a grid in x
N = 100
x_array = np.linspace(0, 2 * np.pi, N)

# Loop over the grid and calculate the second order derivative at each point
ypp_method1 = []
h = 1.0
for x in x_array:
    second_order_derivative = (f(x - h) - 2 * f(x) + f(x + h)) / h ** 2
    ypp_method1.append(second_order_derivative)
   
# Plot the results
fig, ax = plt.subplots()
ax.plot(x_array, f(x_array), label="f(x)")
ax.plot(x_array, -np.sin(x_array), label="$y''$ calculated exactly")
ax.plot(x_array, ypp_method1, "--", label="$y''$ calculated numerically")
ax.set(xlabel="x")
ax.legend()

h = 1
N = 8
order = 2
d2_dx2 = FinDiff(0, h, order)
d2_dx2.matrix((N,)).toarray()


N = 100
x_array = np.linspace(0, 2 * np.pi, N)

h = x_array[1] - x_array[0]
fx_array = f(x_array)
ypp_method2 = FinDiff(0, h, 2).matrix((N,)) * fx_array

# Plot the results
fig, ax = plt.subplots()
ax.plot(x_array, f(x_array), label="f(x)")
ax.plot(x_array, -np.sin(x_array), label="$y''$ calculated exactly")
ax.plot(x_array, ypp_method2, "--", label="$y''$ calculated numerically")
ax.set(xlabel="x")
ax.legend()
plt.show()

Nx = 500
xmin = -5
xmax = 5

Nt = 250
tmin = 0
tmax = 20
k = 1 

# Calculate grid, potential, and initial wave function
x_array = np.linspace(xmin, xmax, Nx)
t_array = np.linspace(tmin, tmax, Nt)
v_x = k * x_array ** 2
psi = np.exp(-(x_array+2)**2)

# Calculate finite difference elements
dt = t_array[1] - t_array[0]
dx = x_array[1] - x_array[0]

# Convert to a diagonal matrix
v_x_matrix = diags(v_x)

# Calculate the Hamiltonian matrix
H = -0.5 * FinDiff(0, dx, 2).matrix(x_array.shape) + v_x_matrix

# Apply boundary conditions to the Hamiltonian
H[0, :] = H[-1, :] = 0
H[0, 0] = H[-1, -1] = 1

# Calculate U
I_plus = eye(Nx) + 1j * dt / 2. * H
I_minus = eye(Nx) - 1j * dt / 2. * H
U = inv(I_minus).dot(I_plus)

# Iterate over each time, appending each calculation of psi to a list
psi_list = []
for t in t_array:
    psi = U.dot(psi)
    psi[0] = psi[-1] = 0
    psi_list.append(np.abs(psi))