import math

def task1():
    number1 = 4
    number2 = 3
    num1 = number1 + number2
    print("Task 1:", num1)

#task1()

def task2():
    number3 = 4
    number4 = 2
    num2 = number3 / number4
    print("Task 2:", num2)

#task2()

def task3():
    number5 = int(16)
    number6 = int(2)
    num3 = number5 / number6
    print("Task 3:",num3)

#task3()

def task4():
    float_num1 = 3.43
    float_num2 = 5.34
    float_num3 = 4.23
    num4 = float_num1 * float_num2 / float_num3
    print("Task 4:",num4)

#task4()

def task5():
    num = 23.523
    num5 = round((num ** 3) / 2, 1)
    print("Task 5:",num5)

#task5()

def task6():
    number7 = float(16.76)
    number8 = float(2.12)
    num6 = math.floor(number7 - number8)
    print("Task 6:",num6)

#task6()

def task7():
    number9 = float(16.76)
    number10 = float(2.12)
    num7 = math.ceil(number9 - number10)
    print("Task 7:",num7)

#task7()

def task8():
    a = 12
    b = 16
    num8 = c = math.sqrt(a ** 2 + b ** 2)
    print("Task 8:",num8)

#task8()

def task9():
    pos_num = 5
    neg_num = -7
    num9 = pos_num + neg_num
    print("Task 9:",num9)

#task9()

def task10():
    temp = 90
    num10 = round(((temp - 32) / 1.8), 2)
    print("Task 10:",num10)

#task10()

def task11():
    num11 = (((6 + 7/12) - (3 + 17/36)) * 2.5 - (4 + 1/3) / 0.65) / (4 / (1/4) - 0.5)
    print("Task 11:", num11)

#task11()

def task12():
    first = (2 + 3 / 4) / 1.1 + (3 + 1 / 3) / (2.5 - 0.4 * (3 + 1 / 3))
    second = ((2 + 1 / 6) + 4.5) * 0.375 / (2.75 - (1 + 1 / 2))
    num12 = first / (5 / 7) - second
    print("Task 12:",num12)

#task12()

def task13():
    num13 = (11 + 2 / 5) + (7 + 1 / 2) * ((285.6 / 14 - (1 + 23 / 30) + 13 / 50) / (24.4 - 10.23))
    print("Task 13:",num13)

#task13()

def task14():
    top = (9 - (5 + 3 / 8)) * ((4 + 5 / 12) - (4 / (2 + 2 / 3))) + (3 / 10 - 0.5 / 4) * (4 / 7)
    bottom = (1 / 24) + 0.25 / (13 + 1 / 3)
    num14 = top / bottom
    print("Task 14:",num14)

#task14()

def task15():
    num15 = (5.75 * 100) / 2.5
    print("Task 15:",num15)

#task15()

def task16():
    top2 = 0.16 * (3.2 - 3 / 40) + (2 + 3 / 11) * 4.125 / 3 * (3 / 4)
    bottom2 = (5 + 1 / 6) * 0.3 - 0.3 * 4.5 + (1 / 3) * 0.3
    # значение выражения и 40% от него
    value = top2 / bottom2
    num16 = 0.4 * value

    print(num16)

task16()
