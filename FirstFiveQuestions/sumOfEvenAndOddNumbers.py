def SumOfEven(arr1):
    sum = 0
    for ele in arr1:
        if int(ele) % 2 == 0:
            sum = sum + int(ele)
    return sum


def SumOfOdd(arr1):
    sum = 0
    for ele in arr1:
        if int(ele) % 2 != 0:
            sum = sum + int(ele)
    return sum
