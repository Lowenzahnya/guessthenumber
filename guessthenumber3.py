import random

while True:
    user_number = int(input('Введите загаданное число от 1 до 5: '))
    if random.randint(1, 5) == user_number:
        print('Вы угадали! Вау! Супер! Класс!')
        break
    else:
        print('Попробуйте снова')
print('gg')
