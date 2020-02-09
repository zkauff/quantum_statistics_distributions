import sys
import numpy as np
import pylatex
import matplotlib
from matplotlib import pyplot as plt


def fermi_dist(e, t):
    return 1 / (np.exp(e / (k * t)) + 1)


def bose_dist(e, t):
    return 1 / (np.exp(e / (k * t)) - 1)


matplotlib.use('TkAgg')

k = 8.617 * pow(10, -5)  # eV / degree Kelvin
particle = '   uninitialized'

while 1 > 0:
    print("please enter the type of particle: ")
    # Prompt user input for type of distribution
    for line in sys.stdin:
        if 'Fermion'.lower() == line.rstrip().lower():
            particle = 'Fermion'
            break
        if 'Boson'.lower() == line.rstrip().lower():
            particle = 'Boson'
            break
        print(f'Unknown particle type: {line} Supported particles are [Fermion][Boson]')
    print(f'Selected particle is \'{particle}\'')

    T = int(input("Enter the first temperature to plot: "))
    T2 = int(input("Enter the second temperature to plot: "))
    T3 = int(input("Enter the third temperature to plot: "))

    if particle == 'Boson':
        f = np.zeros(400)
        v = np.arange(.01, 4.01, 0.01)
        for i in np.arange(0, 400):
            f[i] = bose_dist(v[i], T)
        plt.plot(v, f, color='red')
        for i in np.arange(0, 400):
            f[i] = bose_dist(v[i], T2)
        plt.plot(v, f, color='blue')
        for i in np.arange(0, 400):
            f[i] = bose_dist(v[i], T3)
        plt.plot(v, f, color='green')
        plt.xlim([0, 4.01])
        plt.ylim([0, 2.5])
        plt.title('Bose(-Einstein) distribution')
        plt.show()

    if particle == 'Fermion':
        f = np.zeros(400)
        v = np.arange(.01, 4.01, 0.01)
        for i in np.arange(0, 400):
            f[i] = fermi_dist(v[i], T)
        plt.plot(v, f, color='red')
        for i in np.arange(0, 400):
            f[i] = fermi_dist(v[i], T2)
        plt.plot(v, f, color='blue')
        for i in np.arange(0, 400):
            f[i] = fermi_dist(v[i], T3)
        plt.plot(v, f, color='green')
        plt.xlim([0, 4.01])
        plt.ylim([0, 2.5])
        plt.title('Fermi(-Dirac) distribution')
        plt.show()
