class Macrostate:
    particle_energies = [0]
    num_particles = 0
    probability = 0
    total_energy = 0

    def __init__(self, num_particles, total_energy):
        self.particle_energies = []
        self.num_particles = num_particles
        self.probability = 0.00
        self.total_energy = total_energy


# arr - array to store the combination
# index - next location in array
# total_energy - the total number of energy levels to fill
# reducedNum - the number of energy levels left to fill
# num_particles - total number of energy levels to print
# macrostate_arr - array of Macrostates to update
def find_macrostates_rec(arr, index, total_energy,
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
        find_macrostates_rec(arr, index + 1, total_energy,
                             remaining_free_energy - k, num_particles, macrostate_arr)


# Function to find out all
# combinations of positive numbers
# that add upto given number.
# It uses findCombinationsUtil()
def find_macrostates(total_energy, num_particles, macrostate_arr):
    # array to store the combinations
    # It can contain max n elements
    arr = [0] * total_energy

    print("Finding all macrostates for " + str(num_particles) + " particles with total energy " + str(total_energy))
    # find all combinations
    find_macrostates_rec(arr, 0, total_energy, total_energy, num_particles, macrostate_arr)


def determine_macrostate_probability(macrostate_arr):
    return


def display_macrostate(macrostate):
    # Convert array of particles into array of energy levels
    num_per_energy_level = [0] * (macrostate.total_energy + 1)
    for i in range(0, len(num_per_energy_level)):
        for j in range(0, len(macrostate.particle_energies)):
            if macrostate.particle_energies[j] == i:
                num_per_energy_level[i] = num_per_energy_level[i] + 1

    for i in range(macrostate.total_energy, -1, -1):
        print(str(i) + "dE: ", end=" ")
        for j in range(0, macrostate.num_particles - num_per_energy_level[i]):
            print("-", end=" ")
        for j in range(0, num_per_energy_level[i]):
            print("x", end=" ")
        print(" ")
    return


macrostates = []
find_macrostates(9, 5, macrostates)
for i in range(0, len(macrostates)):
    print("Macrostate " + str(i))
    display_macrostate(macrostates[i])
