logins_and_passwords = []
try:
    #1. вход данных целого числа n
    number = int(input('Введите число пользователей: '))
except ValueError:
    print('Вы ввели строку, а надо ввести число, введите число:')
    number = int(input('Введите число вместо строки: '))

# 2. на строках n ввести данные пользователя
for i in range(number):
    log_passw = input('Введите логин и пароль: ').split()
    # случай когда пользователь вводит данные без пробела
    # ЭТО УСЛОВИЕ НУЖНО: Чтобы выяснить ввел ли пользователь данные слитно
    if len(log_passw) == 1:
        print('Вы написали слитно')
        log_passw = input('Введите логин и пароль: ').split()
    # случай когда пользователь вводит данные правильно
    logins_and_passwords.append(log_passw)

# 3. анализ паролей
for current_user in logins_and_passwords:
    # current_user = ['abc', '123456']
    if len(current_user[1]) < 6:
        # print('У пользователя', login_password[0], 'пароль короткий')
        print(f'У пользователя {current_user[0]} пароль короткий')