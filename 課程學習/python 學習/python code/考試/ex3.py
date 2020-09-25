number = []
for i in range(10,10001):
    i_list = list(str(i))
    one = list(str(i))
    i_list.reverse()
    two = i_list
    if one == two:
        number.append(i)
print(number)
