from array import *


def populate_boson(total_energy, num_particles):
    # set up energy level array
    energy_levels = array('i', [0])
    # total number of energy levels = total_energy + 1
    for i in range(1, total_energy + 1):
        energy_levels.append(0)

    # Iterate through all energy levels in descending order,
    # filling the 'i'th energy level
    total_occupied_energy = 0
    particles_placed = 0
    num_macrostates = total_energy + 1 # TODO: calculate number of macrostates
    macrostates = [[0 for x in range(num_macrostates)] for y in range(total_energy + 1)]
    # for i in range(total_energy - 1, 0, -1):
    # TODO: add loop
    macrostates[0][total_energy] = macrostates[0][total_energy] + 1
    total_occupied_energy = total_occupied_energy + total_energy
    particles_placed = 1
    if total_occupied_energy == total_energy:
        for i in range(particles_placed, num_particles):
            particles_placed = particles_placed + 1
            macrostates[0][0] = macrostates[0][0] + 1
    for i in range(0, len(macrostates[0])):
        print( str(i) + " dE: " + str(macrostates[0][i]))


populate_boson(8, 2)
