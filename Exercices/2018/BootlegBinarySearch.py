values = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def regularSearch (arrayOfValues,needle):
    count = 0;
    for elem in arrayOfValues:
        count += 1
        if needle == elem:
            print ('count', count)
            return needle
    print('count', count)
    return False


def bootlegBinarySearch(arrayOfValues,needle):
    count = 0
    size = len(arrayOfValues) -1
    midIndex = round(size/2)
    found = False
    output = -1
    midArray = arrayOfValues
    while found == False and len(midArray) > 1:
        count += 1
        if midArray[midIndex] == needle:
            found = True
            output = midArray[midIndex]
        if needle > midIndex:
            midArray =  midArray[midIndex:]
        else:
            midArray =  midArray[0:midIndex]

        midIndex = round(len(midArray)/2)
    print ("Result", output)
    print ("Count",   count)
    return output
print (regularSearch(values,17))
print (regularSearch(values,21))
bootlegBinarySearch(values,30)
bootlegBinarySearch(values,2)
