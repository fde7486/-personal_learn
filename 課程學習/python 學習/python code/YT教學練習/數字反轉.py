# 將數字反轉(ex : 123:321, 130:31, -56:-65)
def reverse(x):
    x_list = list(str(x))
    x_list.reverse()
    if x_list[0] == "0" and x_list[-1] == "-":
        del x_list[0]
        x_list = list(x_list[-1]) + x_list[:-1]
    elif x_list[0] == '0' :
        del x_list[0]
    elif x_list[-1] == "-":
        x_list = list(x_list[-1]) + x_list[:-1]    
    y = ''.join(x_list)
    return y
x = eval(input('輸入數字'))
print(reverse(x))