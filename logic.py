import random

def play_game(min_number, max_number, attempts, initial_capital):
    print("Добро пожаловать в игру 'Угадай число'!")
    print(f"У вас есть {attempts} попыток и {initial_capital} капитала.")
    secret_number = random.randint(min_number, max_number)
    capital = initial_capital

    for attempt in range(1, attempts + 1):
        print(f"\nПопытка {attempt}/{attempts}")
        print(f"Ваш текущий капитал: {capital}")
        bet = int(input("Введите ставку: "))
        guess = int(input(f"Угадайте число ({min_number}-{max_number}): "))

        if guess == secret_number:
            print("Поздравляем! Вы угадали число!")
            capital += bet  # Удвоение ставки
        else:
            print("Не угадали.")
            capital -= bet  # Потеря ставки
        if capital <= 0:
            print("Ваш капитал исчерпан. Игра окончена.")

    print("\nИгра завершена!")
    print(f"Загаданное число было: {secret_number}")
    print(f"Ваш итоговый капитал: {capital}")