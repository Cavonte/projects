# Given an array of integers, return a new array such that each element at index i of the new array is the product of
# all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was
# [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?

# Plan
# Start with an initial array filled with ones
# Iterate through the array and multiply the current number by the number at the index that we are at.
# Unless its the index


def multiplier(initial_array):
    if len(initial_array)<2:
        print("Invalid Input")

    output = []
    # inefficient but I dt not have to import numpy
    for number in initial_array:
        output.append(1)
    # print(output, "Array filled with ones")

    initial_array_counter = 0
    for outerNumber in initial_array:
        multiplier_counter = 0
        for innerNumber in output:
            if initial_array_counter != multiplier_counter:
                output[multiplier_counter] = outerNumber * innerNumber
            multiplier_counter = multiplier_counter + 1
        initial_array_counter = initial_array_counter + 1
    return output


set1 = [3, 2, 1]
set2 = [1, 2, 3, 4, 5]
set3 = []
set4 = [1]

print("result", multiplier(set3))
print("result", multiplier(set4))
print("result", multiplier(set1))
print("result", multiplier(set2))

# Consider a solution with a division
print('--------------------------------------------------------')


def solution_with_division(initial_array):
    if len(initial_array) < 2:
        print("Invalid Input")

    product = []
    # inefficient but I dt not have to import numpy
    for number in initial_array:
        product.append(1)

    total_product = 1
    for number in initial_array:
        total_product = total_product * number

    division_counter = 0
    while division_counter < len(initial_array):
        product[division_counter] = total_product / initial_array[division_counter]
        division_counter = division_counter + 1

    return product


print("result", solution_with_division(set3))
print("result", solution_with_division(set4))
print("result", solution_with_division(set1))
print("result", solution_with_division(set2))


print('--------------------------------------------------------')
# Big brain solution
# This solution uses the fact 2 loops multiply each number. The final product put both of them together.


def MultipliserV2(initial_array):
    if len(initial_array) < 2:
        print("Invalid Input")

    left = []
    right = []

    product = []
    # inefficient but I dt not have to import numpy
    for number in initial_array:
        right.append(1)
        left.append(1)
        product.append(1)
    # print(output, "Array filled with ones")

    # Start after the first index filled with 1
    # Left
    counter_left = 1
    while counter_left < len(initial_array):
        left[counter_left] = left[counter_left - 1] * initial_array[counter_left - 1]
        counter_left = counter_left + 1

    print("Left", left)

    # start from the 2 from the end because the last element is supposed to be a 1
    counter_right = len(initial_array) - 2
    while counter_right >= 0:
        right[counter_right] = right[counter_right + 1] * initial_array[counter_right + 1]
        counter_right = counter_right - 1

    print("Right", right)

    counter_prod = 0
    while counter_prod < len(initial_array):
        product[counter_prod] = left[counter_prod] * right[counter_prod]
        counter_prod = counter_prod + 1

    return product


print("result", MultipliserV2(set3))
print("result", MultipliserV2(set4))
print("result", MultipliserV2(set1))
print("result", MultipliserV2(set2))



