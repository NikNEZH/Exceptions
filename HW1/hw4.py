def divide_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        raise ValueError("Array lengths are not equal")

    result = []
    for i in range(len(arr1)):
        try:
            result.append(arr1[i] / arr2[i])
        except ValueError as e:
            print(e)
    
    return result

try:
    arr1 = [6, 9, 12]
    arr2 = [2, 3, 0]
    result = divide_arrays(arr1, arr2)
    print(result)
except ValueError as e:
    print(e)
