from scipy.special import comb
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
import matplotlib.gridspec as gridspec


class Macrostate:
    # An array of num_particles where each number is one particle at the energy level represented
    particle_energies = [0]
    # An array of size total_energy where each item is the number of particles at that energy level
    energy_levels = [0]
    # The number of particles in this macrostate
    num_particles = 0
    # The probability of this macrostate occuring. Must be set by calling determine_macrostate_probability
    microstates = 0
    # The total energy of the system
    total_energy = 0

    def __init__(self, num_particles, total_energy):
        self.particle_energies = []
        self.energy_levels = []
        self.num_particles = num_particles
        self.microstates = 0
        self.total_energy = total_energy


# arr - array to store the combination
# index - next location in array
# total_energy - the total number of energy levels to fill
# reducedNum - the number of energy levels left to fill
# num_particles - total number of energy levels to print
# macrostate_arr - array of Macrostates to update
def find_boson_macrostates_rec(arr, index, total_energy,
                               remaining_free_energy, num_particles, macrostate_arr):
    # Base condition
    if remaining_free_energy < 0:
        return

    # If combination is
    # found, print it
    if remaining_free_energy == 0:
        if index <= num_particles:
            state = Macrostate(num_particles, total_energy)
            if index < num_particles:
                # Print out zeroes to illustrate the particles in ground state
                for i in range(0, num_particles - index):
                    state.particle_energies.append(0)
            # Print out excited state particles
            for i in range(index):
                state.particle_energies.append(arr[i])
            macrostate_arr.append(state)
        return

    # Find the previous number stored in arr[].
    # It helps in maintaining increasing order
    prev = 1 if (index == 0) else arr[index - 1]

    # note loop starts from previous
    # number i.e. at array location
    # index - 1
    for k in range(prev, total_energy + 1):
        # next element of array is k
        arr[index] = k

        # call recursively with
        # reduced number
        find_boson_macrostates_rec(arr, index + 1, total_energy,
                                   remaining_free_energy - k, num_particles, macrostate_arr)


# Function to find out all
# combinations of positive numbers
# that add upto given number.
# It uses findCombinationsUtil()
def find_boson_macrostates(total_energy, num_particles, macrostate_arr):
    # array to store the combinations
    # It can contain max n elements
    arr = [0] * total_energy

    print("Finding all macrostates for " + str(num_particles) + " particles with total energy " + str(total_energy))
    # find all combinations
    find_boson_macrostates_rec(arr, 0, total_energy, total_energy, num_particles, macrostate_arr)

    # Convert array of particles into array of energy levels
    for k in range(0, len(macrostate_arr)):
        macrostate = macrostate_arr[k]
        macrostate.energy_levels = [0] * (macrostate.total_energy + 1)
        for i in range(0, len(macrostate.energy_levels)):
            for j in range(0, len(macrostate.particle_energies)):
                if macrostate.particle_energies[j] == i:
                    macrostate.energy_levels[i] = macrostate.energy_levels[i] + 1
    return


# arr - array to store the combination
# index - next location in array
# total_energy - the total number of energy levels to fill
# reducedNum - the number of energy levels left to fill
# num_particles - total number of energy levels to print
# macrostate_arr - array of Macrostates to update
def find_fermi_macrostates_rec(arr, index, total_energy,
                               remaining_free_energy, num_particles, macrostate_arr):
    # Base condition
    if remaining_free_energy < 0:
        return

    # If combination is
    # found, append it
    if remaining_free_energy == 0:
        if index <= num_particles:
            state = Macrostate(num_particles, total_energy)
            occupied_levels = [0] * (total_energy + 1)
            append = 1
            if index < num_particles:
                # Print out zeroes to illustrate the particles in ground state
                for i in range(0, num_particles - index):
                    state.particle_energies.append(0)
                    occupied_levels[0] = occupied_levels[0] + 1
                    if occupied_levels[0] > 2:
                        # Pauli exclusion principle is violated
                        append = 0
            # Print out excited state particles
            for i in range(index):
                state.particle_energies.append(arr[i])
                occupied_levels[arr[i]] = occupied_levels[arr[i]] + 1
                if occupied_levels[arr[i]] > 2:
                    # Pauli exclusion principle is violated
                    append = 0

            if append == 1:
                macrostate_arr.append(state)
        return

    # Find the previous number stored in arr[].
    # It helps in maintaining increasing order
    prev = 1 if (index == 0) else arr[index - 1]

    # note loop starts from previous
    # number i.e. at array location
    # index - 1
    for k in range(prev, total_energy + 1):
        # next element of array is k
        arr[index] = k

        # call recursively with
        # reduced number
        find_fermi_macrostates_rec(arr, index + 1, total_energy,
                                   remaining_free_energy - k, num_particles, macrostate_arr)


# Function to find out all
# combinations of positive numbers
# that add upto given number.
# It uses findCombinationsUtil()
def find_fermi_macrostates(total_energy, num_particles, macrostate_arr):
    # array to store the combinations
    # It can contain max n elements
    arr = [0] * total_energy

    print("Finding all macrostates for " + str(num_particles) + " particles with total energy " + str(total_energy))
    # find all combinations
    find_fermi_macrostates_rec(arr, 0, total_energy, total_energy, num_particles, macrostate_arr)

    # Convert array of particles into array of energy levels
    for k in range(0, len(macrostate_arr)):
        macrostate = macrostate_arr[k]
        macrostate.energy_levels = [0] * (macrostate.total_energy + 1)
        for i in range(0, len(macrostate.energy_levels)):
            for j in range(0, len(macrostate.particle_energies)):
                if macrostate.particle_energies[j] == i:
                    macrostate.energy_levels[i] = macrostate.energy_levels[i] + 1
    return


# Determines the probability of particles appearing in each state.
# macrostate_arr - an array of macrostates, where each state must have the same total energy and number of particles
def average_per_energy_level(macrostate_arr):
    total_energy = macrostate_arr[0].total_energy
    num_microstates = total_microstates(macrostate_arr)
    particle_counts = []
    for i in range(0, total_energy + 1):
        particle_counts.append(0)
        for j in range(0, len(macrostate_arr)):
            particle_counts[i] = particle_counts[i] + macrostate_arr[j].energy_levels[i] * microstates_of_macrostate(
                macrostate_arr[j])
    # average number of particles in each state
    for i in range(len(particle_counts)):
        print("Average number of particles at " + str(i) + " dE: " + str(particle_counts[i] / num_microstates))
    return


# Finds the number of microstates for the given macrostate
def microstates_of_macrostate(macrostate):
    num_microstates = 1
    remaining_particles = macrostate.num_particles
    for i in range(macrostate.total_energy, -1, -1):
        num_microstates = num_microstates * (comb(remaining_particles, macrostate.energy_levels[i]))
        remaining_particles -= macrostate.energy_levels[i]
    macrostate.microstates = num_microstates
    return num_microstates


# Finds the number of microstates for a given array of macrostates by summing the number of microstates for each
# macrostate. Please note that running this for a macrostate_arr with large numbers of particles and total energy will
# be quite slow as the number of macrostates depends upon computation of factorials.
def total_microstates(macrostate_arr):
    num_microstates = 0
    for i in range(len(macrostate_arr)):
        num_microstates = num_microstates + microstates_of_macrostate(macrostate_arr[i])
    return num_microstates


def display_macrostate_text_vertical(macrostate):
    for i in range(macrostate.total_energy, -1, -1):
        print("% 4d dE: " % i, end=" ")
        for j in range(0, macrostate.num_particles - macrostate.energy_levels[i]):
            print("-", end=" ")
        for j in range(0, macrostate.energy_levels[i]):
            print("\033[0;31mX\033[0;34m", end=" ")
        print(" ")
    return


def display_macrostate_arr_text_vertical(macrostates):
    for x in range(0, len(macrostates)):
        print("\033[0;34mMacrostate " + str(x) + " (microstates: "
              + str(microstates_of_macrostate(macrostates[x])) + ")")
        display_macrostate_text_vertical(macrostates[x])


def display_macrostate_arr_text_horizontal(macrostates):
    print("          ", end="")  # offsets the fact that lower rows have '0dE: ' before each level
    # print each title
    for x in range(0, len(macrostates)):
        print("{:<45}".format("\033[0;34mMacrostate " + str(x) + " (microstates: "
                              + str(microstates_of_macrostate(macrostates[x])) + ")"), end="")
    print()
    for i in range(macrostates[0].total_energy, -1, -1):
        # print energy level descriptor
        print("% 4d dE: " % i, end=" ")
        for x in range(0, len(macrostates)):
            count = 38
            # print dashes for each empty slot
            for j in range(0, macrostates[x].num_particles - macrostates[x].energy_levels[i]):
                print("-", end=" ")
                count = count - 2
            # print X's for each occupied slot
            for j in range(0, macrostates[x].energy_levels[i]):
                print("\033[0;31mX\033[0;34m", end=" ")
                count = count - 2
            # pad the rest of the space with spaces to line up with macrostate titles
            for j in range(0, count):
                print(" ", end="")
        # print newline
        print("")
    return


def display_macrostate_arr_graphics(macrostates):
    fig, axs = plt.subplots(3, int(len(macrostates) / 3))
    for n in range(0, len(macrostates)):
        for i in range(macrostates[n].total_energy, -1, -1):
            for j in range(0, macrostates[n].energy_levels[i]):
                axs[n%3][int(n/3)].plot(j, i, marker='o', color="red")
                axs[n%3][int(n/3)].set_xlim([-1, macrostates[n].num_particles])
                axs[n%3][int(n/3)].set_ylim([-1, macrostates[n].total_energy])
                axs[n%3][int(n/3)].set_title('Macrostate ' + str(n) + ' (' + str(macrostates[n].microstates) + ' microstates)')
                axs[n%3][int(n/3)].axes.get_xaxis().set_visible(False)
                axs[n%3][int(n/3)].yaxis.set_major_locator(MultipleLocator(1))
                axs[n%3][int(n/3)].grid(which='major', axis='y', color='#CCCCCC', linestyle='--')
    plt.show()
    return


def demo():
    macrostates = []
    find_fermi_macrostates(6, 4, macrostates)
    display_macrostate_arr_text_horizontal(macrostates)
    average_per_energy_level(macrostates)
    display_macrostate_arr_graphics(macrostates)


demo()
