import random

random_number = random.randint(1, 5)
user_number = int(input('Введите загаданное число от 1 до 5: '))
if random_number == user_number:
    print('Вы угадали! Вау! Супер! Класс!')
else:
    print(f'Не верно, было загадано {random_number}')
