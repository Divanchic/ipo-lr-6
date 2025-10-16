import random
mas = [tuple(sorted(random.randint(-10, 10) for i in range(4))) for j in range(20)] # Генерируем массив
print(mas)
comb = list(set(mas)) # Создаем список уникальных комбинаций, засчет перевода в множество
for combo in comb:#задаем цикл, в котором перебираем каждый элемент
    print(combo)
num = int(input("Введите число: "))
count = 0
for i in range(len(combo)): # Подсчитываем кол-во пар, сумма которых меньше числа
    for j in range(i + 1, len(combo)):
        if combo[i] + combo[j] < num:
            count += 1
print(count)
