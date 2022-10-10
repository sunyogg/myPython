# Using Recursion to perform Binary Search
def binary_search_recursion(arr, target, start, end):
    mid = int(start + ((end - start ) / 2))
    if (arr[mid] == target):
        return mid
    elif (target > arr[mid]):
        return binary_search_recursion(arr, target, mid + 1, end)
    else :
        return binary_search_recursion(arr, target, start, mid - 1)