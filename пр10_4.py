sum = 0

while True:
    price = int(input('Введите цену товара: '))

    if price == 0:
        break

    if price < 0:
        print('Ошибка цены')
        continue

    if price > 0:
        sum += price

if sum > 1000:
    sum = sum - (sum * 0.1)
    print(f"Применена скидка 10%. Итоговая сумма: {sum:.2f}")
else:
    print('Итоговая сумма: ')
