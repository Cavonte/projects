# This problem was asked by Stripe.
# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.
# solution
# https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array/
# Varian
# https://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/
import math

# plan
def flankTraversal(arr):

    lookingFor = 0
    counter = 0
    while counter < len(arr):
        if arr[counter] == lookingFor:
            counter = 0
            lookingFor = lookingFor + 1
            continue
        counter = counter + 1
    print(lookingFor)



# evenArray = [1,2,3,4,5,6]
# oddArray = [1,2,3,4,5]
typical = [3,2,1,0,4,5,6,7]
given = [3, 4,-2,5,7,-1, 1]
given2 = [1, 2, 0]
testing = [-1,-3,-3,4,2,1,5,8,7,6]  #should be 0
testing2 = [4,4,3,2,2,6,9,9,8,1,0]  #should be 5
# flankTraversal(evenArray)
flankTraversal(typical)
flankTraversal(given)
flankTraversal(given2)
flankTraversal(testing)
flankTraversal(testing2)

# NO SOLUTION