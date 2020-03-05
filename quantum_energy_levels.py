

# arr - array to store the combination
# index - next location in array
# total_energy - the total number of energy levels to fill
# reducedNum - the number of energy levels left to fill
# num_particles - total number of energy levels to print
def find_macrostates_rec(arr, index, total_energy,
                         remaining_free_energy, num_particles):
    # Base condition
    if remaining_free_energy < 0:
        return

    # If combination is
    # found, print it
    if remaining_free_energy == 0:
        if index <= num_particles:
            if index < num_particles:
                # Print out zeroes to illustrate the particles in ground state
                for i in range(0, num_particles - index):
                    print(str(0), end=" ")
            # Print out excited state particles
            for i in range(index):
                print(arr[i], end=" ")
            print("")
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
                             remaining_free_energy - k, num_particles)


# Function to find out all
# combinations of positive numbers
# that add upto given number.
# It uses findCombinationsUtil()
def find_macrostates(total_energy, num_particles):
    # array to store the combinations
    # It can contain max n elements
    arr = [0] * total_energy

    print("Finding all macrostates for " + str(num_particles) + " particles with total energy " + str(total_energy))
    # find all combinations
    find_macrostates_rec(arr, 0, total_energy, total_energy, num_particles)


find_macrostates(9, 3)
