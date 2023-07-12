import itertools
import tuscan

def permutations(n):
    numbers = list(range(n))
    permutations = itertools.permutations(numbers)
    return permutations

n = int(input("Enter the number of test orders: "))

print("Total permutations of test orders: ")
total_permutations = permutations(n)
for permutation in total_permutations:
    print(permutation)

print("Prioritized permutations of test orders: ")
prioritized_permutations = tuscan.generate_tuscan_permutations(n)
for permutation in prioritized_permutations:
    print(permutation)