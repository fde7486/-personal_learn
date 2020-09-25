# # 兩次和
# 給定一個整數數組nums 和一個整數target，返回兩個數字的索引，這樣它們的總和為target。
# 您可以假設每個輸入都只有一個解決方案，並且您可能不會兩次使用同一元素。
# 您可以按任何順序返回答案

def twoSum(nums,target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if target == (nums[i]+nums[j]) and i != j:
                return (i, j)        
x = [3,3,5,6,7,10]
y = 17
print(twoSum(x,y))
