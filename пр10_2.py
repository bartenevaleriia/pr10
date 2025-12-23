num1 = int(input('Введите первое число '))

while True:
    num2 = int(input('Введите второе число '))
    if num2 <= num1:
        print('Ошибка. Второе число должно быть больше первого. Попробуйте еще раз')
        continue
    break

while True:
    num3 = int(input('Введите третье число '))
    if num3 <= num2:
        print('Ошибка. Третье число должно быть больше второго. Попробуйте еще раз')
        continue
    break

print('Последовательность принята')