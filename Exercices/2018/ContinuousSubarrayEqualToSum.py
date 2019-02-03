# find continuous subarray which
stuff = [1, 4, 0, 0, 3,10, 5]
stuff2 = [1,4,20,3,10,5]


def contSub(stuff, sum):
    currentSum = stuff[0]
    stuffSize = len(stuff)
    start = 0
    pointer = 1
    while start < stuffSize and pointer < stuffSize:

        print(currentSum)
        while currentSum + stuff[pointer] > sum and start < stuffSize-1:
            currentSum -= stuff[start]
            start += 1

        print(currentSum)
        currentSum += stuff[pointer]
        pointer += 1

        if currentSum == sum:
            print("Found", start, pointer)
            return

    print("Not Found")


contSub(stuff, 7)
contSub(stuff2, 33)
