#1
a = int(input('Напишите цифру, обозначающую день недели: '))
if a < 6:
    print('Увы, сегодня нужно пойти на работу.')
elif a == 6 or a == 7:
    print('Ура, ВЫХОДНОЙ ДЕНЬ!')
else:
    print('Такого дня нет в календаре.')


#2
def inputNumbers(x):
    xyz = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f"Введите значение {xyz[i]}: "))
    return a

def checkPredicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result

statement = inputNumbers(3)

if checkPredicate(statement) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")


#3
x = int(input('Напишите X координату: '))
y = int(input('Напишите Y координату: '))
if  x>0 and y>0:
    print('Это 1-ая четверть.')
elif x<0 and y>0:
    print('Это 2-ая четверть.')
elif x<0 and y<0:
    print('Это 3-ая четверть.')
elif x>0 and y<0:
    print('Это 4-ая четверть.')
else:
    print('Эта точка лежит на оси координат')


#4
k = int(input('Напишите число обозначающееи четверть координату(1-4): '))
if  k==1:
    print('Диапазон точки(x>0; y>0)')
elif k==2:
    print('Диапазон точки(x<0; y>0)')
elif k==3:
    print('Диапазон точки(x<0; y<0)')
elif k==4:
    print('Диапазон точки(x>0; y<0)')
else:
    print('Такой четверти не существует')


#5
x1, y1 = map(int, input('Координаты первой точки (x, y): ').split())

x2, y2 = map(int, input('Координаты первой точки (x, y): ').split())

d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(round(d, 3))