balance = 1000

while True:
    print('Чтобы узнать баланс, нажмите "1"')
    print('Чтобы снять 100 рублей, нажмите "2"')
    print('Чтобы положить 100 рублей, нажмите "3"')
    print('Для выхода, нажмите "4"')
    print('')

    command = int(input('Введите код команды: '))

    if 4 < command < 1:
        print('Неверная команда')
        print('')
        break

    if command == 1:
        print('Текущий баланс:', balance)
        print('')

    if command == 2:
        if balance >= 100:
            balance -= 100
            print('Снято')
            print('')
        else:
            print('Недостаточно средств')
            print('')

    if command == 3:
        balance += 100

    if command == 4:
        print('До свидания')
        print('')
        break

