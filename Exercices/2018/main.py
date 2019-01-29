import math
fixPlease = [2, 20, 6, 4, 0, 17, 11, 5, 18, -1,1, 3, 14,14, 13, 9, 7, 16, 12, 15, 19, 10]

def maximumInMiddle(arr,start,mid,end):
    maxLeft = -float("inf")
    currentSum = 0
    indexLeft = mid
    for index in range(mid, start, -1):
        currentSum += arr[index]
        if currentSum > maxLeft:
            maxLeft = currentSum
            indexLeft = index

    currentSum = 0
    maxRight = -float("inf")
    indexRight = mid
    for index in range(mid, end):
        currentSum += arr[index]
        if currentSum > maxRight:
            maxRight = currentSum
            indexRight = indexRight

    combined = maxRight + maxLeft - arr[mid]
    return {indexLeft,indexRight,combined}


def maximumSubArray(arr,start, mid,end):

    left = maximumSubArray(arr,start,mid)
    right = maximumSubArray(arr,mid+1,end)
    current = maximumInMiddle(arr,start,mid,end)

    if left > right:
        return left
    elif right > left:
        return right
    else:
        return current


exemple = [-1,1,1,2,1,1,-1]
# expected max middle total 6 from index 1 to 7
mid = floor(len(exemple)/2)
print(mid)
print(maximumInMiddle(exemple,0, len(exemple)-1))