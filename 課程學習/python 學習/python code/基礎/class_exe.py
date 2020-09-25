height = [160,174,194,167,137]
# max_height = 0
# for i in height:
#     if i > max_height:
#         max_height = i
# print(max_height)

tall = [171, 180, 165, 155]
s = len(tall)
for i in range(s-1):
    print ('Round', i)
    for j in range(s-1-i):
        print ('Compare tall{} and tall{}'.format(j,j+1))
        if tall[j] > tall[j+1]:
            print ('Switch {} and {}'.format(tall[i], tall[j]))
            temp = tall[j]
            tall[j] = tall[j+1]
            tall[j+1] = temp
    print (tall)       