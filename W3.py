#  Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

while True:
    lst = list(map(int, input('Введите числа через пробел:\n').split()))
    new_lst = []
    [new_lst.append(i) for i in lst if i not in new_lst]
    print(f'Список оставшихся элементов: {new_lst}')