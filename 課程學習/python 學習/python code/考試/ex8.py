player1 = ["張三", 12, 10, 3]
player2 = ["李四", 4, 8, 2]
player3 = ["王五", 20, 1, 10]
player = [player1, player2, player3]
hit = 0
theft = []
home_run = 0
for i in range(len(player)):
    for j in range(len(player1)):
        print(player[i][j],end=" ")
    print()
    hit +=player[i][1]

hit /=len(player)
print("平均安打數是{}".format(hit))
for i in range(len(player)):
    theft.append(player[i][2])
    if player[i][2] == max(theft):
        print("{}是盜壘王".format(player[i][0]))
    home_run += player[i][3]
print("他們三個共有{}支全壘打".format(home_run))
home_rumlist = sorted(player,key=lambda x:x[-1],reverse=True)
print("全壘打排序：", end=" ")
for i in range(len(home_rumlist)):
    print(home_rumlist[i][0],end=" ")