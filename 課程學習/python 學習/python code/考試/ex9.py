eat = ["牛肉麵", "餛飩麵", "蛋炒飯", "丼飯"]
eat_after = []
for i in range(len(eat)):
    for j in range(len(eat)):
        for k in range(len(eat)):
            for l in range(len(eat)):
                z = eat[i],eat[j],eat[k],eat[l]
                eat_after.append(z)  
for i in range