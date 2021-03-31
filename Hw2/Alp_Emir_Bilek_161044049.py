def binary_search(arr, x):
    bot = 0
    top = len(arr) - 1
    middle = 0
    while bot <= top:
        middle = (top + bot) // 2
        if arr[middle] < x:
            bot = middle + 1
        elif arr[middle] > x:
            top = middle - 1
        else:
            return middle
    return -1

def pair(array,x):
    for i in array:
        temp=x/i
        if binary_search(array,temp) !=-1:
            print("pair (",i,array[binary_search(array,temp)],")")

def main():
    array=[1,2,3,6,5,4]
    array.sort()
    pair(array,6)

main()

