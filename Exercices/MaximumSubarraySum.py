# Given an array of integer(positive and negative) find the subarray with the maximum sum

# Kadanes algorithm


def findMaximumSubarraySum(inputArray):
    maxSoFar = 0
    maxAthisIndex = 0
    start = 0
    end = 0

    for i in range(0, len(inputArray)):
        # Add the current element to the max so far
        maxAthisIndex = maxAthisIndex + inputArray[i]

        # if you encouter an element that set the max so far below 0 then reset
        if maxAthisIndex < 0:
            maxAthisIndex = 0
            start = i + 1

        # if the current maxAthisIndex then replace the current maximum
        elif maxSoFar < maxAthisIndex:
            maxSoFar = maxAthisIndex
            end = i

    print(start,end)
    return maxSoFar


input = [-1, 2, 4, -3, 5, 2, -5, 2]

print(findMaximumSubarraySum(input))

a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
print(findMaximumSubarraySum(a))

b = a = [-2, -3, 4, -1, -2, 1, 5, -3]
print(findMaximumSubarraySum(b))







# divide and conquer


