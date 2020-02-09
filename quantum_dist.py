import sys
from scipy.stats import boltzmann
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

matplotlib.use('TkAgg')

k = 8.617 * pow(10, -5) # eV / degree Kelvin
particle = 'uninitialized'

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

    T = int(input("Enter the temperature: "))

    if particle == 'Boson':
        f = np.zeros(400)
        v = np.arange(0, 4, 0.01)
        for i in np.arange(0, 400):
            f[i] = 1 / (np.exp(v[i] / (k * T)) - 1)
        plt.plot(v, f)
        plt.show()