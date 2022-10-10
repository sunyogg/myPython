def insertion_sort_using_for(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, 0, -1):
            if (arr[j] < arr[j-1]):
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else :
                break


def insertion_sort_using_while(arr):
    i = 0
    j = i+1
    while (i < (len(arr) - 1)):
        while (j > 0):
            if (arr[j] < arr[j-1]):
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j -= 1
            else :
                break
        i += 1
        j = i + 1