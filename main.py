from random import randint

secret_number = randint(1, 100)
print('Отгадай число от 1 до 100')

user_number = 0
try_count = 0

while user_number != secret_number:
    try_count += 1
    user_number = int(input(f'{try_count}-я попытка: '))
    if user_number > secret_number:
        print('Много')
    elif user_number < secret_number:
        print('Мало')
    else:
        print(f'Правильно. Я загадал {secret_number}')
