def statistic(x):
    ans = (min(x), max(x), round(sum(x)/len(x),3))
    return ans
x1 = [12, 34, 24, 75, 36, 97]
print(statistic(x1))