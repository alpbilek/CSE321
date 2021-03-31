def knapSack(W, wts, vs, n):
    if n == 0 or W == 0:
        return 0
    if (wts[n - 1] > W):
        return knapSack(W, wts, vs, n - 1)
    else:
        return max(
            vs[n - 1] + knapSack(
                W - wts[n - 1], wts, vs, n - 1),
            knapSack(W, wts, vs, n - 1))


vs = [10, 4, 3]
wts = [5, 4, 2]
W = 9

print(knapSack(W, wts, vs, len(vs)))
