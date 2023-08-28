def Palindrome(str):
    reverseStr = str[::-1]
    for si, ei in zip(str, reverseStr):
        if (si != ei):
            return 'not palindrome'
    return 'Palindrome'


def OptimizedPalindrom(str):
    length = len(str)
    for i in range(length // 2):
        if str[i] != str[length - i - 1]:
            return 'not palindrome'
    return 'Palindrome'
