def hybrid_quick_sort(arr, R, L):
    while R < L:
        if L - R + 1 < 10:
            insertion_sort(arr, R, L)
            break

        else:
            pivot = partition(arr, R, L)

            if pivot - R < L - pivot:
                hybrid_quick_sort(arr, R, pivot - 1)
                R = pivot + 1
            else:
                hybrid_quick_sort(arr, pivot + 1, L)
                L = pivot - 1

def insertion_sort(arr, low, n):
    for i in range(low + 1, n + 1):
        val = arr[i]
        j = i
        while j > low and arr[j - 1] > val:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = val

def partition(arr, low, high):
    pivot = arr[high]
    i = j = low
    for i in range(low, high):
        if arr[i] < pivot:
            array[i], array[j] = array[j], array[i]
            j += 1
    array[j], array[high] = array[high], array[j]
    return j

array=[3 ,5 ,1,17,16,14,18,25,79,0,1,4]
hybrid_quick_sort(array,0,len(array)-1)
print(array)