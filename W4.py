# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def mnogochlen(k):
    mnogochlen = "k = " + str(k) + " => "
    for i in range(k, -1, -1):
        # Так будет много отсутствуюших членов
        number = random.randrange(0, 4)
        if number != 0 or i == k: # Второе условие если нам всгеда нужен первый член
            number = random.randrange(1, 101)
        # Так будет мало отсутсвующих членов
        # number = random.randrange(0, 101)
        if number != 0 and i != 0:
            if random.randrange(0,4) == 0:
                curr_chlen = str(number) + "x^" + str(i) + " - "
            else:
                curr_chlen = str(number) + "x^" + str(i) + " + "
            mnogochlen += curr_chlen
        elif number != 0 and i == 0:
            mnogochlen += str(number)
        elif number == 0 and i == 0:
            mnogochlen = mnogochlen[:-3]
    mnogochlen += " = 0"
    f = open('mnogochlen.txt', 'w')
    f.write(mnogochlen + '\n')
    f.close()
    return mnogochlen

while True:
    k = -1
    while k < 0 or k > 100:
        k = int(input("Введите коэффициент: "))
        if k < 0 or k > 100:
            print ("Ошибка, введите снова!")
    print(mnogochlen(k))