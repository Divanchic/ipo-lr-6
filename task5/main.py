import random
a = [random.randint(-50, 50) for i in range(1,26)]
zero = 0
plus = 0
minus = 0
for i in a:
    if i < 0:
        minus += 1
    if i>0:
        plus+=1
    if i==0:
        zero +=1
print("отрицательный",minus/25*100)
for i in a:
    if i < 0:
        print(i)
print("положиьельный",plus/25*100)
for i in a:
    if i > 0:
        print(i)
print("нуль",zero/25*100)
for i in a:
    if i == 0:
        print(i)
print("максимальное значение")
print(max(a))
print("минимальное значение")
print(min(a))
print(a)