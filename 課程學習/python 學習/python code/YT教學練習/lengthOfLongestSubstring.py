# def lengthOfLongestSubstring(string):
a = ""
a_list = []
string = "dkskedkhdd"
for i in range(len(string)):
    for j in range(len(string)-(i+1)):
        if string[i+j] in string:
            a += string[i+j] 
        else :
            a_list.append(a)
            a = ""  
print(a_list)