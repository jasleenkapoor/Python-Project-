# -*- coding: utf-8 -*-
#Emlyn Davies 08/11/22
#TDSE alpha v0.10
import numpy as np
import matplotlib.pyplot as plt
from findiff import FinDiff
from scipy.sparse.linalg import inv
from scipy.sparse import eye, diags
import matplotlib.animation as animation
import math
from scipy import signal

plt.rcParams["axes.labelsize"] = 16


#0=SHO 1=INF SQ WELL


def make_animation(demox,choiceS_W, var1,var2,var3):
    Nx = 500
    xmin = -5
    xmax = 5
    k = 1 
    
    x_array = demox
    if choiceS_W == 0:
        v_x = k * x_array ** 2
    if choiceS_W ==1:
        v_x = 1*(signal.square(0.7*x_array-1.6))

    
    
    
    ############
    # Input parameters


    Nt = 250
    tmin = 0
    tmax = 20


    # Calculate grid, potential, and initial wave function

    t_array = np.linspace(tmin, tmax, Nt)
    
    #psi = np.exp(-(x_array+2)**2)
    psi = np.exp(-(x_array+1)**2)

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
    fig, ax = plt.subplots()

    ax.set_xlabel("x [arb units]")
    ax.set_ylabel("$|\Psi(x, t)|$", color="C0")

    ax_twin = ax.twinx()
    ax_twin.plot(x_array, v_x, color="C1")
    ax_twin.set_ylabel("V(x) [arb units]", color="C1")

    line, = ax.plot([], [], color="C0", lw=2)
    ax.grid()
    xdata, ydata = [], []

    def run(psi):
        line.set_data(x_array, np.abs(psi)**2)
        return line,

    ax.set_xlim(x_array[0], x_array[-1])
    ax.set_ylim(0, 1)

    ani = animation.FuncAnimation(fig, run, psi_list, interval=10)
    ani.save("particle_in_a_well.gif", fps=30, dpi=300)


import subprocess
import time
#import vlc
Nx = 500
xmin = -5
xmax = 5
    
choice=1
var1=123
var2=123
var3=123
    
make_animation(np.linspace(xmin, xmax, Nx), choice, var1, var2, var3)




def play_movie():
    subprocess.call(["cmd", "/c", "start", "/max", "particle_in_a_well.gif."])
    time.sleep(5)
    #startfile(r"particle_in_a_well.mp4")
    #subprocess.call("TASKKILL /F /IM VLC.exe", shell=True)

play_movie()




