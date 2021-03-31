def insertionSort(arr):
    count = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            count=count+1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return count

counter=0
def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    global counter
    for j in range(low, high):


        if arr[j] < pivot:
            i = i + 1
            counter=counter+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    counter=counter+1
    return (i + 1)


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

arr = [12, 11, 13, 5, 6]
quickSort(arr,0,len(arr)-1)
arr2 = [12, 11, 13, 5, 6]
print("Insertion Sort Count:",insertionSort(arr2))
print("Quick Sort Count:",counter)
