a = (1, 2, 3, 4, 5, 6)
b = (7, 8, 9, 5, 3, 2)
c = a + b
print(c.count(2)) #Quantos dois tem
print(c.index(8)) #Em qual posição esta o 8
for co in enumerate(c):
    print(co)
del(c)