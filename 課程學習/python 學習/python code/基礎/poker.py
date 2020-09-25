def poker():
    a = ["D","d","R","r"]
    porker = ['2', '3', '4', '5', '6', '7', '8',
            '9', '10', 'J', 'Q', 'K', 'A']
    cards = []
    for i in a:
        for j in porker:
            b = i+'-'+str(j)
            cards.append(b)
    return cards
    

import random
def getPoker13():
    p = poker()
    random.shuffle(p)
    players = []
    players.append(p[0:13])
    players.append(p[13:26])
    players.append(p[26:39])
    players.append(p[39:])
    
    return players

def showPlayers(players):
    for i, p in enumerate(players):
       print ('\n Players '+str(i))
       print (p)

'''
import random as r
# play1 = r.sample(cards,13)
# cards1 = list(set(cards)-set(play1))
# print(cards1)

for i in range(4):
    i = r.sample(cards,13)
    cards = list(set(cards)-set(i))
    play = sorted(i)
    
'''