# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
# Follow-up: Can you do this in O(N) time and constant space?

test1 = [2 ,4 ,6 ,2 , 5]
test2 = [5, 1, 1, 5]
test3 = [1,3,2,1,5,4,1]
test4 = [2, 4, -1, 0, -3, 2]


# Plan
def getmaxsum(arr, startindex):
    currentmax = max(0,arr[startindex])
    iterator = startindex + 2

    while iterator < len(arr):
        value1 = arr[iterator]

        value2 = iterator + 1 < len(arr) and arr[iterator + 1]
        if value1 >= value2 and value1 > -1:
            currentmax = currentmax + value1
        elif value2 > value1 and value2  > -1:
            currentmax = currentmax + value2
            iterator = iterator + 1

        iterator = iterator + 2

    return currentmax

print(max(getmaxsum(test1,0),getmaxsum(test1,1)))
print(max(getmaxsum(test2,0),getmaxsum(test2,1)))
print(max(getmaxsum(test3,0),getmaxsum(test3,1)))
print(max(getmaxsum(test4,0),getmaxsum(test4,1)))

