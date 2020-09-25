color = ["Spade", "Heart", "Diamond", "Club"]
number = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
cords = []
for i in range(len(color)):
    for j in range(len(number)):
        cord = color[i] + "-" +number[j]
        cords.append(cord)
import random as r
play = r.sample(cords,5)
play.sort(reverse=True)
print(play)