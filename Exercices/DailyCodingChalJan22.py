# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Execute this in one pass.
# This is executed in linear time.
# And Should take O(N) in regards to space as the worst possible case is to store all the number and not find anything.

def findSum(givenlist,k):
    if len(givenlist) < 2:
        print("Invalid input. Given:", givenlist)
        return
    localMap = {}
    counter = 0
    print("Starting list")
    for number in givenlist:
        #     check if the the second number exist already
        if number in localMap:
            print("Found",givenlist,"index",counter, "plus", localMap[number])
            return
        # key = sum to be found - number encoutered,  value = currentIndex
        localMap[k - number] = counter
        print("adding",k - number)
        counter = counter + 1

    print("could not find the number in", givenlist)

expected = [10,9,4,1,15,3,7]
expectedK = 22
findSum(expected,expectedK)

small = [10]
smallK = 0
findSum(small,smallK)

medium = [3,2,1,4,10,2,3]
mediumk = 6
findSum(medium,mediumk)

emptyList = []
emptyNumber = 0
findSum(emptyList,emptyNumber)

# Number is not in the list
notpresnet = [10,22,30,12,11]
notPresentNumber = 4
findSum(notpresnet,notPresentNumber)
