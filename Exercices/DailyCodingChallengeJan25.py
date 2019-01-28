# This problem was asked by Stripe.
# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.
# solution
# https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array/
# Variant
# https://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/
import math
import copy


#separate the negative numbers
#for each negative number encountered, keep a counter of the current index they should be moved to, place them there and increase the index
def separate(arr):
    current_negative_index = 0
    counter = 0
    while counter < len(arr):
        if arr[counter] < 0:
            temp = arr[current_negative_index]
            arr[current_negative_index] = arr[counter]
            arr[counter] = temp
            current_negative_index = current_negative_index + 1
        counter = counter + 1
    return current_negative_index

# idea use the offset taken from the previous method.
# For each value encountered while going through the array, set the value at that index to a negative value


def missing_integer(arr, negativeIndex):
    # 3 cases, all negative,  empty or 1 element
    if negativeIndex == len(arr) - 1 or not arr or negativeIndex == len(arr):  # most likely that
        print("invalid input")
        return
    ref = copy.copy(arr)
    for i in range(negativeIndex, len(arr)):
        valueAtIndex = min(ref[i],len(arr)-1) # use this as an index
        arr[valueAtIndex] = int(-1 * math.fabs(ref[valueAtIndex]))  # set the value to be negative, int was necessary
        # otherwise it would be transformed into a float
    # mid result should be the first half of the array be the segragated numbers followed by the value that have been flip
    # ped
    print(arr, negativeIndex, len(arr))
    #traverse the array again and take note of indices that have positive values
    #substrace the offset
    lowestInteger = -1
    for j in range(negativeIndex, len(arr)):
        if arr[j] > 0: #had -1 before but there is not such thing as  - 0
            lowestInteger = j - negativeIndex  # add structure here
            break  # break is necessary otherwise value is overwritten

    if lowestInteger == -1:
        lowestInteger = len(arr)

    print(lowestInteger)


# evenArray = [1,2,3,4,5,6]
# oddArray = [1,2,3,4,5]
typical = [3, 2, 1, 0, 4, 5, 6, 7]  # should be 8
given = [3, 4, -2, 5, 7, -1, 1]  # should be 0
given2 = [1, 2, 0]  # should be 3
testing = [-1, -3, -3, 4, 2, 1, 5, 8, 7, 6]  # should be 0
testing2 = [4, 4, 3, 2, 2, 6, 9, 9, 8, 1, 0]  # should be 5
invalid1 = [-1, -2, -3, -4, -5, -6, -7, -8]  # no positive integers
invalid2 = []
invalid3 = [1]

# flankTraversal(evenArray)
missing_integer(typical, separate(typical))
missing_integer(given, separate(given))
missing_integer(given2, separate(given2))
missing_integer(testing, separate(testing))
missing_integer(testing2, separate(testing2))
missing_integer(invalid1, separate(invalid1))
missing_integer(invalid2, separate(invalid2))
missing_integer(invalid3, separate(invalid3))
