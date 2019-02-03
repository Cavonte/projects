import math

fixPlease = [2, 20, 6, 4, 0, 17, 11, 5, 18, -1,1, 3, 14,14, 13, 9, 7, 16, 12, 15, 19, 10]

def combine(array, start, mid, end):
    left = array[start: mid]
    right = array[mid: end]

    leftSize = len(left)
    rightSize = len(right)

    iteratorLeft = 0
    iteratorRight = 0
    iteratorArray = start

    while iteratorArray < end:
        if left[iteratorLeft] < right[iteratorRight]:
            array[iteratorArray] = left[iteratorLeft]
            left[iteratorLeft] = float("inf")
            iteratorArray += 1
            iteratorLeft = iteratorLeft + 1 if iteratorLeft + 1 < leftSize else iteratorLeft
        elif right[iteratorRight] <= left[iteratorLeft]:
            array[iteratorArray] = right[iteratorRight]
            right[iteratorRight] = float("inf")
            iteratorArray += 1
            iteratorRight = iteratorRight + 1 if iteratorRight + 1 < rightSize else iteratorRight


def mergeSort(array, start, end):
    if end - start <= 1:
        return
    mid = math.floor((start + end) / 2)
    mergeSort(array, start, mid)
    mergeSort(array, mid, end)
    combine(array, start, mid, end)


arr = [1, 1, 1, 1, 1, 1, 1, 3, 5, 7, 9, 0, 2, 4, 6, 8, 1, 1, 1, 1, 1, 1, 1]
# print(combine(arr,6,11,16),arr)

print(mergeSort(fixPlease, 0, len(fixPlease)), fixPlease)
