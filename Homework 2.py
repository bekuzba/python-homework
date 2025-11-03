
def task1():
    number = 3
    if number > 0:
         print(True)
    else:
        print(False)

#task1()

def task2():
    mark = int(input())
    if mark >= 90:
        print("Отлично, Ваша оценка 5!")
    elif mark >= 80:
        print("Здорово, Ваша оценка 4!")
    elif mark >= 70:
        print("Хорошо, Ваша оценка 3!")
    elif mark >= 60:
        print("Вам стоит подучить материал")
    else:
        print("Вы не сдали экзамен")

#task2()

def task3():
    x = 45
    y = 76
    z = 87
    if x < y and x < z:
        print(x)
    elif y < x and y < z:
        print(y)
    elif z < x and z < y:
        print(z)
#task3()

def task4():
    x, y = int(input()), int(input())
    if x % y == 0:
        print(x / y)
    else:
        print(x + y)
#task4()

def task5():
    a = 4
    b = 9
    c = 6
    if a + b > c and a + c > b and b + c > a:
        print("yes")
    else:
        print("no")
#task5()

def task6():
    a = 58
    b = 5
    c = 63
    if c == a + b:
        print(True)
    else:
        print(False)

#task6()

def task7():
    x = int(input())
    if x >= 2 and x < 10:
        print(True)
    else:
        print(False)

#task7()

def task8():
    x = float(input())
    print(x < -4 or x >= 5)

#task8()

def task9():
    x = int(input())
    print(x in (2, 4, 6, 8, 10))

#task9()

def task10():
