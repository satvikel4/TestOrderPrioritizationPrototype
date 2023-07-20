import itertools
import tuscan

num_classes = int(input("Enter the number of classes (1 or 2): "))

def one_class():
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

    print("Prioritized permutations of test orders: ")
    prioritized_permutations = tuscan.generate_tuscan_permutations(n)
    for permutation in prioritized_permutations:
        print(permutation)

def multi_class():
    methods_per_class = []
    for i in range(2):
        methods = int(input("How many methods are in class " + str(i) + ": "))
        methods_per_class.append(methods)
    class_one_tuscan_permutations = tuscan.generate_tuscan_permutations(methods_per_class[0])
    class_two_tuscan_permutations = tuscan.generate_tuscan_permutations(methods_per_class[1])
    print("Prioritized permutations of test orders: ")
    for i in range(len(class_two_tuscan_permutations)):
        for j in range(len(class_one_tuscan_permutations)):
            print("Class 1: " + str(class_one_tuscan_permutations[j]) + "; Class 2: " + str(class_two_tuscan_permutations[i]))
    for i in range(len(class_one_tuscan_permutations)):
        for j in range(len(class_two_tuscan_permutations)):
            print("Class 2: " + str(class_two_tuscan_permutations[j]) + "; Class 1: " + str(class_one_tuscan_permutations[i]))      

if num_classes == 1:
    one_class()
else:
    multi_class()
