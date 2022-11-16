# -*- coding: utf-8 -*-
#Emlyn Davies 08/11/22
#TDSE alpha v0.01
import numpy as np
import matplotlib.pyplot as plt
from findiff import FinDiff
from scipy.sparse.linalg import inv
from scipy.sparse import eye, diags
import matplotlib.animation as animation


def freq(psi_list):
    yf = np.fft.rfft(psi_list)
    fs = np.fft.rfftfreq(499, d=1)
    plt.plot(fs, yf)
    plt.show()
    