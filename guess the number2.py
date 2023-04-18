import random

random_number = random.randint(1, 5)
running = True

while running:
    user_number = int(input('Введите загаданное число от 1 до 5: '))
    if random_number == user_number:
        print('Вы угадали! Вау! Супер! Класс!')
        running = False
    else:
        print('Попробуйте снова')
print('gg')