arrNumber1 =  [0,1,1,1]
arrNumber2 =  [0,1,1,1]
#            1 1 1 1 0
def addBinaryNumber(arr1, arr2):
    if len(arr1) != len(arr2):
        raise Exception("Invalid Input")

    arrNumber1 = [0] + arr1
    arrNumber2 = [0] + arr2
    carry = 0
    for index in range(0 , len(arrNumber1)):
        iterator = (len(arrNumber1) -1) - index
        sum = arrNumber1[iterator] + arrNumber2[iterator] + carry

        result = 0 if (0 == sum % 2) else 1
        carry = 1 if  sum > 1 else 0

        if sum > 3:
            raise Exception("Brother what?")

        arrNumber1[iterator] = result
        print(result)

addBinaryNumber(arrNumber1,arrNumber2)