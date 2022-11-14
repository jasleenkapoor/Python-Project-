# -*- coding: utf-8 -*-
#Emlyn Davies 08/11/22
#TDSE alpha v0.01
import numpy as np
import matplotlib.pyplot as plt
from findiff import FinDiff
from scipy.sparse.linalg import inv
from scipy.sparse import eye, diags
import matplotlib.animation as animation


plt.rcParams["axes.labelsize"] = 16

############
# Input parameters
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
























######################################
#fig, ax = plt.subplots()

#ax.set_xlabel("x [arb units]")
#ax.set_ylabel("$|\Psi(x, t)|$", color="C0")

#ax_twin = ax.twinx()
#ax_twin.plot(x_array, v_x, color="C1")
#ax_twin.set_ylabel("V(x) [arb units]", color="C1")

#line, = ax.plot([], [], color="C0", lw=2)
#ax.grid()
#xdata, ydata = [], []

#def run(psi):
    #line.set_data(x_array, np.abs(psi)**2)
    #return line,

#ax.set_xlim(x_array[0], x_array[-1])
#ax.set_ylim(0, 1)

#ani = animation.FuncAnimation(fig, run, psi_list, interval=10)
#ani.save("particle_in_a_well.mp4", fps=120, dpi=300)
















#np.argsmax np.where

#use txt file Jamie uses
#each frame is 10ms, so find number of rows/columns between two numerically similar peaks, times by 10ms
#this gives an estimate for the time, 1/estimated time = estimated frequency
########################################################
#data = open(Jamie.txt, mode='r')

#def freq(x_array, psi_list):
    #peak = max(psi_list)
    #pos = x_array(np.where(psi_list == peak))
    #print(pos)

#freq()

#print(psi_list)
#print(type(psi_list))
#print(psi_list[0])

#print (max(psi_list[0]))
#print(len(psi_list))

#for i in range(len(psi_list)):
    #peak = max(psi_list[i])
    #print(x_array[np.where(psi_list[i] == peak)])
    #for j in range(len(psi_list)):
        #peak2 = max(psi_list[j])
        #plow = peak2 + 0.001
        #phigh = peak2 - 0.001
        #print(np.where(peak <= plow))
        
yf = np.fft.rfft(psi_list)
#d = psi_list[1] - psi_list[0]
fs = np.fft.rfftfreq(499, d=1)
plt.plot(fs, yf)
plt.show()

#np.ndarray.shape(yf)