def mergeSort(arr, size):
    temp = [0 for i in range(size)]
    return _mergeSort(arr, temp, 0, size - 1)
def _mergeSort(arr, temp, left, right):
    mid, count = 0, 0
    if right > left:
        mid = (right + left) // 2
        count = _mergeSort(arr, temp, left, mid)
        count += _mergeSort(arr, temp,mid + 1, right)
        count += mergeHelper(arr, temp, left,mid + 1, right)
    return count
def mergeHelper(arr, temp, left, mid, right):
    count = 0
    i = left
    j = mid
    k = left
    while i <= mid - 1 and j <= right:
        if arr[i] <= 2 * arr[j]:
            i += 1
        else:
            count += (mid - i)
            j += 1

    i = left
    j = mid
    k = left

    while i <= mid - 1 and j <= right:
        if arr[i] > arr[j]:
            temp[k] = arr[j]
            k += 1
            j += 1
        else:
            temp[k] = arr[i]
            k += 1
            i += 1
    while i <= mid - 1:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        j, k = j + 1, k + 1
    for i in range(left, right + 1):
        arr[i] = temp[i]
    return count




arr = [9,15,4,17,12,10,5,3]
print(mergeSort(arr, len(arr)))


