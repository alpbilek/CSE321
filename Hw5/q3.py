def minsumtriangle(arr):
    return dfs(arr, 0, 0, 0, 100000)


def dfs(arr, row, column, sum, minSum):
    sum += arr[row][column]
    if row == len(arr) - 1:
        if sum < minSum:
            return sum
    else:
        minSum = dfs(arr, row + 1, column, sum, minSum)
        minSum = dfs(arr, row + 1, column + 1, sum, minSum)
    return minSum


A = [[2],
     [5, 4],
     [1, 4, 7],
     [8, 6, 9, 6]]
print(minsumtriangle(A))