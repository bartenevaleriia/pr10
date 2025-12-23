biggest = 0
while True:
    num = int(input('Введите натуральное число: '))

    if num == 0:
        break

    if num > biggest:
        biggest = num

print('Максимальное число:', biggest)