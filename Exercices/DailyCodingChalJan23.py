# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?
import copy

# Plan
# Start with an initial array filled with ones
# Iterate through the array and multiply the current number by the number at the index that we are at.
# Unless its the index
def multiplier(initialArray):
    if len(initialArray)<2:
        print("Invalid Input")

    output = []
    # inefficient but I dt not have to import numpy
    for number in initialArray:
        output.append(1)
    # print(output, "Array filled with ones")

    initialArrayCounter = 0
    for outerNumber in initialArray:
        multipLierCounter = 0
        for innerNumber in output:
            if initialArrayCounter != multipLierCounter:
                output[multipLierCounter] = outerNumber * innerNumber
            multipLierCounter = multipLierCounter + 1
        initialArrayCounter = initialArrayCounter + 1
    return output


set1 = [3,2,1]
set2 = [1, 2, 3, 4, 5]
set3 = []
set4 = [1]

# print("result",multiplier(set1))
# print("result",multiplier(set2))
# print("result",multiplier(set3))
# print("result",multiplier(set4))

# Consider a solution with a division
print('--------------------------------------------------------')
def solutionWithDivision(initialArray):
    if len(initialArray) < 2:
        print("Invalid Input")

    product = []
    # inefficient but I dt not have to import numpy
    for number in initialArray:
        product.append(1)

    totalProduct = 1
    for number in initialArray:
        totalProduct = totalProduct * number

    divisionCounter = 0
    while divisionCounter < len(initialArray):
        product[divisionCounter] = totalProduct / initialArray[divisionCounter]
        divisionCounter = divisionCounter + 1

    return product

print("result",solutionWithDivision(set3))
print("result",solutionWithDivision(set4))
print("result",solutionWithDivision(set1))
print("result",solutionWithDivision(set2))


print('--------------------------------------------------------')
# Big brain solution
# This solution uses the fact 2 loops multiply each number. The final product put both of them together.
def MultipliserV2(initialArray):
    if len(initialArray)<2:
        print("Invalid Input")

    left = []
    right = []

    product = []
    # inefficient but I dt not have to import numpy
    for number in initialArray:
        right.append(1)
        left.append(1)
        product.append(1)
    # print(output, "Array filled with ones")

    # Start after the first index filled with 1
    # Left
    counterLeft = 1
    while counterLeft < len(initialArray):
        left[counterLeft] = left[counterLeft - 1] * initialArray[counterLeft - 1]
        counterLeft = counterLeft + 1

    print("Left", left)

    # start from the 2 from the end because the last element is supposed to be a 1
    counterRight = len(initialArray) - 2
    while counterRight >= 0:
        right[counterRight] = right[counterRight + 1] * initialArray[counterRight + 1]
        counterRight = counterRight - 1

    print("Right", right)

    counterProd = 0
    while counterProd < len(initialArray):
        product[counterProd] = left[counterProd] * right[counterProd]
        counterProd = counterProd + 1

    return product

# print("result",MultipliserV2(set3))
# print("result",MultipliserV2(set4))
# print("result",MultipliserV2(set1))
# print("result",MultipliserV2(set2))



