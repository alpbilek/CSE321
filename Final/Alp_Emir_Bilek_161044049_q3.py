def rev(m, x, revenue, n, t):
    maxr = [0] * (m + 1)
    nth = 0
    for i in range(1, m + 1):
        if nth < n:
            if x[nth] == i:
                if i > t:
                    maxr[i] = max(maxr[i - t - 1] + revenue[nth], maxr[i - 1])
                else:
                    maxr[i] = max(maxr[i - 1], revenue[nth])
                nth += 1
            else:
                maxr[i] = maxr[i - 1]
        else:
            maxr[i] = maxr[i - 1]
    return maxr[m]

m = 20
x = [7, 11, 13, 15]
r = [4, 2, 5, 6]
t = 4
print(rev(m, x, r, len(x), t))