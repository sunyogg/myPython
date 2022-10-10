# Select the maximum element/number from the array and move it to the right
# Hand side.
# So the biggest number will be moved at the last index, second biggest
# element will be moved at the second last index and so on.

# So first we need to find the biggest number in the array and then 
# swap the biggest number with right most number. 
# We also need to make sure that we are not checking the max numbers that are
# already swapped.

# 1) Check the biggest element in the array.
# 2) swap the biggest element with the right most element
# 3) again check the next big element but don't check the sorted element(last).


nums = [7, 2, 10, 6, 4, 5, 3, 0]



def selection_sort_1(arr):
    for i in range(len(arr) - 1):
        max = arr[0]
        index_of_max = 0
        for j in range(len(arr) - i):
            if (arr[j] > max):
                max = arr[j]
                index_of_max = j
        last_index_to_swap = len(arr) - 1 - i
        arr[index_of_max], arr[last_index_to_swap] = arr[last_index_to_swap], arr[index_of_max]



def findMaxIndex(arr, start_index, end_index):
    max = 0
    for i in range(start_index, end_index+1):
        if (arr[i] > arr[max]):
            max = i
    return max

def swap(arr, first, second):
    arr[first], arr[second] =  arr[second], arr[first]

def selection_sort_2(arr):
    for i in range(len(arr) - 1):
        last_index = len(arr) - 1 - i
        max_index = findMaxIndex(arr, 0, last_index)
        swap(arr, max_index, last_index)


selection_sort_2(nums)
print(nums)
