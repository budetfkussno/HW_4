#Задайте натуральное число N Напишите программу, которая составит список простых множителей числа N.
while True:
    n = int(input('Введите натуральное число: '))
    lst = [n]

    def natur(lst):
        fl = 0
        for i in range(lst[-1] // 2, 1, -1):
            if lst[len(lst)-1] % i == 0:
                lst.append(i)
                lst[-2] = lst[-2] // i              
                fl += 1
        if fl != 0:
            natur(lst)

    natur(lst)
    print(lst)