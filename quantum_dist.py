import sys
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

k = 7.617 * pow(10, -5)  # eV / degree Kelvin


def fermi_dist(e, t):
    return 1 / (np.exp(e / (k * t)) + 1)


def bose_dist(e, t):
    return 1 / (np.exp(e / (k * t)) - 1)


def plot_by_temp():
    print("Plotting population dependence on temperature.")
    matplotlib.use('TkAgg')

    particle = '   uninitialized'

    print("please enter the type of particle: ")
    # Prompt user input for type of distribution
    for line in sys.stdin:
        if 'Fermion'.lower() == line.rstrip().lower():
            particle = 'Fermion'
            break
        if 'Boson'.lower() == line.rstrip().lower():
            particle = 'Boson'
            break
        print("Unknown particle type: " + line + "Supported particles are Fermion, Boson")
    print("Selected particle is \"" + particle + "\"")

    T = int(input("Enter the first temperature to plot: "))
    T2 = int(input("Enter the second temperature to plot: "))
    T3 = int(input("Enter the third temperature to plot: "))

    f = np.zeros(400)
    v = np.arange(.01, 4.01, 0.01)
    for i in np.arange(0, 400):
        if particle == 'Fermion':
            f[i] = fermi_dist(v[i], T)
        else:
            f[i] = bose_dist(v[i], T)
    plt.plot(v, f, color='red')
    for i in np.arange(0, 400):
        if particle == 'Fermion':
            f[i] = fermi_dist(v[i], T2)
        else:
            f[i] = bose_dist(v[i], T2)
    plt.plot(v, f, color='blue')
    for i in np.arange(0, 400):
        if particle == 'Fermion':
            f[i] = fermi_dist(v[i], T3)
        else:
            f[i] = bose_dist(v[i], T3)
    plt.plot(v, f, color='green')
    plt.xlim([0, 4.01])
    plt.ylim([0, 2.5])
    if particle == 'Fermion':
        plt.title('Fermi(-Dirac) distribution')
        plt.ylim([0, .5])
    else:
        plt.title('Bose(-Einstein) distribution')
    plt.xlabel('Energy (in eV)')
    plt.ylabel('n(E)')
    plt.show()


plot_by_temp()
