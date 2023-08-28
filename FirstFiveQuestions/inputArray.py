def inputArray(arr1):
    print("Enter elements for array (type 'done' when finished):")
    while True:
        element = input()
        if element.lower() == 'done':
            break
        arr1.append(element)
    return arr1
