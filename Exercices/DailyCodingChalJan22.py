# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Execute this in one pass.
# This is executed in linear time.
# And Should take O(N) in regards to space as the worst possible case is to store all the number and not find anything.


def find_sum(given_list, k):
    if len(given_list) < 2:
        print("Invalid input. Given:", given_list)
        return
    localmap = {}
    counter = 0
    print("Starting list")
    for number in given_list:
        #     check if the the second number exist already
        if number in localmap:
            print("Found", given_list, "index", counter, "plus", localmap[number])
            return
            # key = sum to be found - number encountered,  value = currentIndex
        localmap[k - number] = counter
        print("adding", k - number)
        counter = counter + 1

    print("could not find the number in", given_list)


expected = [10, 9, 4, 1, 15, 3, 7]
expected_k = 22
find_sum(expected, expected_k)

small = [10]
small_k = 0
find_sum(small, small_k)

medium = [3, 2, 1, 4, 10, 2, 3]
medium_k = 6
find_sum(medium, medium_k)

# invalid number
empty_list = []
empty_number = 0
find_sum(empty_list, empty_number)

# Number is not in the list
not_present = [10, 22, 30, 12, 11]
not_present_number = 4
find_sum(not_present, not_present_number)
