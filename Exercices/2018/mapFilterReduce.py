from functools import reduce
uncleanElements = [1,2,3,4,5,6,7,8,9,10]

cleanElements = list(filter(lambda x: 0==x%2,uncleanElements))
print(cleanElements)

mappedElements = list(map(lambda x,y: x*y,uncleanElements,cleanElements))
print(mappedElements)

reducedElements = reduce(lambda x,y: x*y, uncleanElements)
print(reducedElements)