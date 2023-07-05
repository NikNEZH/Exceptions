def diff_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        raise ValueError("Array lengths are not equal")
    
    return [arr1[i] - arr2[i] for i in range(len(arr1))]

try:
    arr1 = [1, 3, 5]
    arr2 = [2, 2, 2, 4]
    result = diff_arrays(arr1, arr2)
    print(result)
except ValueError as e:
    print(e)