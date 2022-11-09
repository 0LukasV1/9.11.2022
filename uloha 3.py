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

print('najvacacsi prvok je', max, 'kamo jeho pozicia je',pos)

a= 0
b= 0

for i in range(0, len(zoz)):
    if zoz[i] % 2==0 and i%2==0:
        a+=1
    else:
        b+=1

print('parnzch je', a , 'neparnzch je', b)





