from l4s import *

while True:
    try:
        n = int(input('Введите количество сотрудников'))
        break

    except ValueError:
        print('ВВОДИТЕ ЧИСЛО!!!!!')


person = {}                                                               # создание списков и словарей для промежуточного хранения номеров такси и п.
taxi = {}
sort = {}
person_n = []
summa = int()

flag = 0                                                                           # ввод расстояния до дома кажд. сотрудника
for i in range(n):
    while flag < n:
        try:
            x = int(input(f'сколько км ехать до дома {i + 1} сотруднику: '))
            person[i + 1] = x
            flag += 1
            break
        except ValueError:
            print('ВВОДИТЕ ЧИСЛО!!!!!')

flag1 = 0                                                                            # ввод  цены у каждого такси
for i in range(n):
    while flag1 < n:
        try:
            y = int(input(f'цена такси {i + 1}: '))
            taxi[i + 1] = y
            flag1 += 1
            break
        except ValueError:
            print('ВВОДИТЕ ЧИСЛО!!!!!')


taxi1 = sorted(taxi.values(), reverse=True)                                          # сопоставление 1эл. с большей ценой 1эл. с меньшим расстоянием
person1 = sorted(person.values())


for i in range(n):
    q1 = person1[i]                                      # сопоставление номера такси и номера сотрудника
    s1 = taxi1[i]

    q = keys1(person, q1)
    s = keys1(taxi, s1)

    sort[s] = q

    del person[q]
    del taxi[s]


sort1 = sorted(sort.values())                             # список номеров такси в верном порядке

for i in range(n):
    s2 = sort1[i]
    s3 = keys1(sort, s2)

    person_n.append(s3)

for i in range(n):                                       # рассчет стоимоcти
    sum = taxi1[i] * person1[i]
    summa += sum



#print(person)
#print(taxi)

#print(person1)
#print(taxi1)

#print(sort)
#print(sort1)

print(person_n)

print(summa)
symma(summa)



























































