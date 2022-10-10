arr = [5, 1, 2, 4, 3]

def cycle_sort_for(arr):
    for i in range(len(arr)-1):
        currentIndex = i
        correctIndex = arr[i] - 1
        if (arr[currentIndex] == arr[correctIndex]):
            continue
        else :
            arr[currentIndex], arr[correctIndex] = arr[correctIndex], arr[currentIndex]
            i -= 1
                        
def cycle_sort_while(arr):
    i = 0
    while (i < len(arr) - 1):
        currentIndex = i
        correctIndex = arr[i] - 1
        if (arr[currentIndex] == arr[correctIndex]):
            i+= 1
            continue
        else :
            arr[currentIndex], arr[correctIndex] = arr[correctIndex], arr[currentIndex]