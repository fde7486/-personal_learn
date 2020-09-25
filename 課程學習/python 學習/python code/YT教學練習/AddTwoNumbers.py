def addTwoNumbers(num1,num2):
    list_1 = list(str(num1))
    list_2 = list(str(num2))
    list_1.reverse()
    list_2.reverse()
    ans_list = []
    for i in range(len(list_1)):
        ans = int(list_1[i]) + int(list_2[i])
        ans_list.append(ans)
    for i in range(len(ans_list)):
        if ans_list[i] > 9:
            ans_list[i] %= 10
            if i+1 in range(len(ans_list)):
                ans_list[i+1] += 1
            elif i+1 not in range(len(ans_list)):
                ans_list.append(1)
    for i in range(len(ans_list)):
        ans_list[i] = str(ans_list[i])
    ans_list.reverse()
    ans_num = "".join(ans_list)
    return int(ans_num)
n1, n2 = eval(input("請輸入2個三位數數字:"))
print(addTwoNumbers(n1,n2))