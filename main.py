import itertools
import tuscan

def permutations(n, t=None):
    numbers = list(range(n))
    permutations = itertools.permutations(numbers, t)
    return permutations

n = int(input("Enter the number of tests: "))

print("Total Possible permutations of tests: ")
total_permutations = permutations(n)
for permutation in total_permutations:
    print(permutation)

t = int(input("Enter t value: "))

print("Total Possible permutations of length t: ")
total_permutations_t = permutations(n, t)
for permutation_t in total_permutations_t:
    print(permutation_t)

# Assuming 'generate_tuscan_permutations' is a function to generate the Tuscan permutations
# Replace this with the actual function name if it's different
print("Prioritized permutations of test orders: ")
prioritized_permutations = tuscan.generate_tuscan_permutations(n)
for permutation in prioritized_permutations:
    print(permutation)
