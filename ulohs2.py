import random
zoz= []
for i in range(10):
    zoz.append(random.randrange(0,21))

print(zoz)
max = zoz[0]

for i in range(1,len(zoz)):
    if max < zoz[i]:
        max= zoz[i]
        pos = i

print('najvacsi prvok je', max, 'kamo jeho pozicia je',pos)