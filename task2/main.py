import random
sumnum = 0
rows = random.randint(4,8)
col = random.randint(4,8)
mat = [-3, -5, -2, -12, 0, 15, 4, 7, 2]
matr = [[random.choice(mat) for i in range(col)] for j in range(rows)]
for i in matr:
    print(*[f"{x:>5}" for x in i])
    for a in i:
        if a%3==0:
            sumnum += a
print(sumnum)

   