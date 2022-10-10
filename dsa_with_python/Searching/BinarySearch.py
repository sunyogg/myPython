

# divide the sorted array into 2 parts from middle.
# then access the element in the middle.
# compare it with the target.

# if the target is less than that number.
# repeat the above step between the first element and middle element.

# if it's larger than the middle element
# then repeat the above step between the middle element and the last element.


def binary_search(arr, target):
    start_index = 0
    end_index = len(arr) - 1
    while (start_index <= end_index):
        middle_index = int(start_index + ((end_index - start_index) / 2))
        if (target == arr[middle_index]):
            return middle_index
        elif (target < arr[middle_index]):
            end_index = middle_index - 1
        elif (target > arr[middle_index]):
            start_index = middle_index + 1
    return -1


array = [1, 2, 4, 5, 7, 9, 10, 12, 14]
print(binary_search(array, 15))















# while (middle > -1):
#     if (target < array[middle]):
#         # search in left
#         end = middle - 1
#         middle = int((start + end) / 2)
#         continue

#     elif (target > array[middle]):
#         # search in right
#         start = middle + 1
#         middle = int((start + end) / 2)
#         continue

#     elif (target == array[middle]) :
#         # target is middle
#         print(f"Found {array[middle]} at index position {middle}.")
#         break

#     else :
#         print(f"{target} not found in the array.")
