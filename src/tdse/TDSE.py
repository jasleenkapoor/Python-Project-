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
from scipy import signal # 
from tdse.Alex_GUI_code import firstq as gui
import tdse.save_psi
import tdse.Frequency
    #export0 == choice 0=owndata 1=SHO 2=SQ WELL
    #export1 == save yes/no 0=n 1=y
    #export2 == springK VALUE
    #export3 == filetype 0=NA 1= mp4 2=gif
    #export4 == filename to save
    #export5 == file name to read V(x)





"""def TDSE_gui():
    try:
        run=gui(0, 0, 0, 0, 0, 0)
        run.main()
    
        Nx = 500
        xmin = -5
        xmax = 5
        k=run.export()[2]
    
        x_array = np.linspace(xmin, xmax, Nx)
        offset=1
        global filename
        if run.export()[0] == 1:
            v_x = k * x_array ** 2
        if run.export()[0] == 2:
            v_x = 1*(signal.square(0.7*x_array-1.6))
        if run.export()[0] == 0:
            v_x = run.export()[5]
            print(run.export()[5])

        if run.export()[3] == 0:
            print("DONT SAVE")
        if run.export()[3] == 1:
            filename = run.export()[4] + ".mp4"
        if run.export()[3] == 2:
            filename = run.export()[4] + ".gif"
    
        make_animation(offset, v_x)
    except:
        print("An unexpected error has occurred, re-try:")"""
        
def TDSE_gui():
    
    run=gui(0, 0, 0, 0, 0, 0)
    run.main()
    
    Nx = 500
    xmin = -5
    xmax = 5
    k=run.export()[2]
    
    x_array = np.linspace(xmin, xmax, Nx)
    offset=1
    global filename
    if run.export()[0] == 1:
        v_x = k * x_array ** 2
    if run.export()[0] == 2:
        v_x = 1*(signal.square(0.7*x_array-1.6))
    if run.export()[0] == 0:
        v_x = np.array(run.export()[5])
        v_x = v_x.astype(np.float)

    if run.export()[3] == 0:
        print("DONT SAVE")
    if run.export()[3] == 1:
        filename = run.export()[4] + ".mp4"
    if run.export()[3] == 2:
        filename = run.export()[4] + ".gif"
    
    make_animation(offset, v_x)









plt.rcParams["axes.labelsize"] = 16


#0=SHO 1=INF SQ WELL 2=CUSTOM


def make_animation(OFFSET,v_x):
    '''  
    Generates the wavefunction for the selected or given potential data
    Parameters
    - - - - - - - 
    demox : str
        name of textfile
        
    choiceS_W : Boolean
        Decides if Square well or Simple Harmonic Oscillator
        
    SpringK : float
        Value of Spring Constant
    
    OFFSET: float
        Initial position of wave packet in x direction
        
    '''
    Nx = 500
    xmin = -5
    xmax = 5
    
    x_array=np.linspace(xmin, xmax, Nx)
    
    ############
    # Input parameters


    Nt = 250
    tmin = 0
    tmax = 20


    # Calculate grid, potential, and initial wave function

    t_array = np.linspace(tmin, tmax, Nt)
    
    #psi = np.exp(-(x_array+2)**2)
    psi = np.exp(-(x_array+OFFSET)**2)

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
        '''  Returns the wavefunction for every unit time increment 
        
        Parameters
        - - - - - - - 
        psi : object with array attributes
        
        '''
        line.set_data(x_array, np.abs(psi)**2)
        return line,

    ax.set_xlim(x_array[0], x_array[-1])
    ax.set_ylim(0, 1)
    
    ani = animation.FuncAnimation(fig, run, psi_list, interval=10)
    try:
        ani.save(filename, fps=30, dpi=300)

    except:
        print("ffmpeg not installed, using pillow (.mp4 not possible)")
        writergif = animation.PillowWriter(fps=30)
        ani.save(filename,writer=writergif)
    
    #save_psi.writetxt(np.square(np.abs(psi_list)),"saved_data_psi"," ",True)
    
    
    
    
    
    
    
    


import subprocess
import time
#import vlc

#TDSE_gui()





def play_movie(filename):
    '''  Plays selected TDSE animation '''
    subprocess.call(["cmd", "/c", "start", "/max", filename+"."]) #
    time.sleep(5)
    #startfile(r"particle_in_a_well.mp4")
    #subprocess.call("TASKKILL /F /IM VLC.exe", shell=True)

#play_movie()




