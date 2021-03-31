def segtree(tree, a, n):
    for i in range(n):
        tree[n + i] = a[i]
    for i in range(n - 1, 0, -1):
        tree[i] = min(tree[2 * i],tree[2 * i + 1])
def range_query(tree, l, r, n):
    l += n
    r += n
    mi = 1e9
    while l < r:
        if l & 1:
            mi = min(mi, tree[l])
            l = l + 1
        if r & 1:
            r -= 1
            mi = min(mi, tree[r])
        l = l // 2
        r = r // 2
    return mi
a = [99,3,5,14,9,2,11]
tree = [0 for i in range(2 * len(a))]
segtree(tree, a, len(a))
print(range_query(tree, 1, 6 + 1, len(a)))
