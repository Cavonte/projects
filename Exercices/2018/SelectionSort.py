# bootleg selection sort
# Time complexity O(n^2)
# Space complexity O(n)

arrToBeSorted = [5,1,3,7,4,8,2,0]

def selectionSort(arrToBeSorted):
    size = len(arrToBeSorted)
    if size == 1:
        return arrToBeSorted
    if size == 0:
        raise Exception("Please Fix")

    for index in range(0,size):
        value = arrToBeSorted[index]
        smallest = index
        iterator = index + 1
        while iterator < size:
            if arrToBeSorted[iterator] < arrToBeSorted[smallest]:
                smallest = iterator
            iterator += 1

        arrToBeSorted[index] = arrToBeSorted[smallest]
        arrToBeSorted[smallest] = value
    return arrToBeSorted

print(selectionSort(arrToBeSorted))
print(selectionSort([1]))
print(selectionSort([]))