toBeSorted  = [1,4,5,5,2,6,3]

def insertionSort(unsortedArray):
    for index in range(1, len(unsortedArray)):
        value = unsortedArray[index]
        iterator = index - 1
        while iterator > -1 and unsortedArray[iterator] > value:
            unsortedArray[iterator + 1] = unsortedArray[iterator]
            iterator -= 1
        unsortedArray[iterator + 1] = value
    return unsortedArray

print(insertionSort(toBeSorted))