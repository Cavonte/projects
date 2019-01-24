def minRow(listOfInt):
    min = 9999
    for num in listOfInt:
        if num < min:
            min = num
    return min
def minimumTotal(triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    sum = 0
    for lists in triangle:
        sum = sum + minRow(lists)

    return sum

major = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

major =    [
     [-1],
    [2,3],
   [1,-1,-3]
     ]

print(minimumTotal(major))
