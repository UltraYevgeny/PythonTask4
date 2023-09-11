"""
Задача 22: Даны два неупорядоченных набора целых чисел 
(может быть, с повторениями). Выдать без повторений в порядке 
возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
m — кол-во элементов второго множества. Затем пользователь вводит 
сами элементы множеств.
"""
"""
n = int(input("Введите кол-во элементов первого множества: "))
m = int(input("Введите кол-во элементов второго множества: "))

setN = input(f"Веведите элементы первого множества(в количестве {n}), через пробел: \n").split()
if len(setN) != n:
    while len(setN) != n:
        setN = input(f"Веведите элементы именно в количестве {n}: \n").split()

setM = input(f"Веведите элементы второго множества(в количестве {m}), через пробел: \n").split()
if len(setM) != m:
    while len(setM) != m:
        setM = input(f"Веведите элементы именно в количестве {m}: \n").split()

resultSet = sorted(set(setN).intersection(set(setM)), reverse=False)

print("Числа удовлетворяющие условиям:",*resultSet)
"""

"""
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
Она растёт на круглой грядке, причём кусты высажены только по окружности. 
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке 
растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них 
выросло различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым 
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может 
собрать за один заход собирающий модуль, находясь перед некоторым кустом 
заданной во входном файле грядки.
"""

numberBush = 0
while numberBush < 4:
    numberBush = int(input("Введите количество кустов (не менее 4): "))

berry = 0
for i in range(numberBush - 2):
    a = i+1 + i+2 + i+3
    if a > berry:
        berry = a

print(berry)


