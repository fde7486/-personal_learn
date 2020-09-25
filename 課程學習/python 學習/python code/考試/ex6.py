def ab(x,y):
    x = list(x)
    y = list(y)
    a = 0
    b = 0
    for i in range(len(x)):
        if x[i] == y[i]:
            a +=1
        for j in range(len(x)):
            if x[i] == y[j]:
                b += 1
    b = b-a
    return (a,b)

ab1 = ab("12345", "82319")
ab2 = ab('12345', '12346')
ab3 = ab('12546', '64521')
print(ab1)
print(ab2)
print(ab3)