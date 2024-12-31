def maxmin(x):
    x.sort()
    max = x[-1]
    min = x[0]
    return [min, max]


print(maxmin([20, 50, 12, 6, 14, 8]))
