def palindrome(str):
    n = len(str)
    arr = [[0 for x in range(n)] for y in range(n)]
    max = 1
    i = 0
    while i < n:
        arr[i][i] = True
        i = i + 1
    head = 0
    i = 0
    while i < n - 1:
        if str[i] == str[i + 1]:
            arr[i][i + 1] = True
            head = i
            max = 2
        i = i + 1
    k = 3
    while k <= n:
        i = 0
        while i < n - k + 1:
            j = i + k - 1
            if arr[i + 1][j - 1] and str[i] == str[j]:
                arr[i][j] = True
                if k > max:
                    head = i
                    max = k
            i = i + 1
        k = k + 1
    print("Longest palindrome substring is: ",)
    for i in range(head,head+max):
        print(str[i])
    print("\nLength is :", max)


palindrome("alpplaemirrimebilekkelib")