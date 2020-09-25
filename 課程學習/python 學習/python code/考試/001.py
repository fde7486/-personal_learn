dict={}
for i in range(3):
    name=input('name? ')
    dict.setdefault(name)
    x=int(input('安打數? '))
    y=int(input('盜壘數? '))
    z=int(input('全壘打數? '))
    num=[x, y, z]
    dict[name]=num
print(dict)