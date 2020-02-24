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
    num_macrostates = total_energy + 1  # TODO: calculate number of macro-states
    macrostates = [[0 for x in range(num_macrostates)] for y in range(total_energy + 1)]
    macrostate_index = 0
    # Algorithm: pick a highest filled energy level (go in descending order).
    # Fill the rest accordingly
    # Throw out the macro-state if it doesn't meet requirements
    for i in range(total_energy, 0, -1):
        total_occupied_energy = 0
        macrostates[macrostate_index][i] = macrostates[macrostate_index][i] + 1
        total_occupied_energy = total_occupied_energy + i
        particles_placed = 1
        if total_occupied_energy == total_energy:
            for i in range(particles_placed, num_particles):
                particles_placed = particles_placed + 1
                macrostates[macrostate_index][0] = macrostates[macrostate_index][0] + 1
            print("Macrostate " + str(macrostate_index))
            for i in range(0, len(macrostates[macrostate_index])):
                print(str(i) + "dE: " + str(macrostates[macrostate_index][i]))
        elif total_occupied_energy > total_energy:
            # Throw out the state
            macrostate_index = macrostate_index - 1
        elif total_energy - i < i:
            macrostates[macrostate_index][total_energy - i] = macrostates[macrostate_index][total_energy - i] + 1
            total_occupied_energy = total_occupied_energy + (total_energy - i)
            particles_placed = particles_placed + 1
            if total_occupied_energy == total_energy:
                for i in range(particles_placed, num_particles):
                    particles_placed = particles_placed + 1
                    macrostates[macrostate_index][0] = macrostates[macrostate_index][0] + 1
                print("Macrostate " + str(macrostate_index))
                for i in range(0, len(macrostates[macrostate_index])):
                    print(str(i) + "dE: " + str(macrostates[macrostate_index][i]))
        macrostate_index = macrostate_index + 1


populate_boson(9, 3)
