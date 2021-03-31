def sumsubsets(arr, n, target):
    x = [0] * len(arr)
    j = len(arr) - 1

    while n > 0:
        x[j] = n % 2
        n = n // 2
        j -= 1
    sum = 0
    for i in range(len(arr)):
        if (x[i] == 1):
            sum += arr[i]
    if (sum == target):
        for i in range(len(arr)):
            if x[i] == 1:
                print(arr[i], end=" ")
        print("\n")


def findSubsets(arr, K):
    x = pow(2, len(arr))
    for i in range(1, x):
        sumsubsets(arr, i, K)



arr = [2, 3, -5, -8, 6, -1]
findSubsets(arr, 0)
