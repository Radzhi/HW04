"""Программа для обучения английскому с использованием словарей"""

# Уровни сложности со своими словарями
easy = {
    'cat': 'кошка',
    'dog': 'собака',
    'bird': 'птица',
    'monkey': 'обезьяна',
    'fox': 'лиса'
}
medium = {
    'car': 'машина',
    'skate': 'скейт',
    'bus': 'автобус',
    'tram': 'трамвай',
    'train': 'поезд'
}
hard = {
    'mirror': 'зеркало',
    'shower': 'душ',
    'teapot': 'чайник',
    'glass': 'стакан',
    'lamp': 'лампа'
}

# Словарь уровней знания игрока
levels = {
   0: "Нулевой",
   1: "Так себе",
   2: "Можно лучше",
   3: "Норм",
   4: "Хорошо",
   5: "Отлично",
}

# Словарь Ответы. Здесь будут храниться правильные и неправильные слова.
correct_answers = []
incorrect_answers = []

# Программа приветствует и предлагает выбрать уровень сложности
print('Привет! Выбери уровень сложности, равный твоему интеллекту и нажми "ENTER"')
print('*ЛЕГКИЙ*', '*СРЕДНИЙ*', '*СЛОЖНЫЙ*')

# Пользователь выбирает уровень сложности
user_input = input().lower()
if user_input == 'легкий':
    words = easy
    print('Ты выбрал легкий уровень сложности')
elif user_input == 'средний':
    words = medium
    print('Ты выбрал средний уровень сложности')
elif user_input == 'сложный':
    words = hard
    print('Ты выбрал сложный уровень сложности')
else:
    print('Иди учи английский! Тебе еще рано сынок')

# Программа показывает английское слово и подсказку
for eng_word, ru_word in words.items():
    print(f'{eng_word}, {len(ru_word)} букв, начинается на {ru_word[0]}...')
    user_input = input('Ваш ответ: ')
    if user_input == ru_word:
        print(f'Верно, {eng_word} это {ru_word}')
        print('-' * 20)
        correct_answers.append(eng_word)
    elif user_input != ru_word:
        print(f'Неверно, {eng_word} это {ru_word}')
        incorrect_answers.append(eng_word)
        print('-' * 20)

# Вывод статистики
print('Вот и все')
print(f'Правильно отвеченные слова: ')
for word in correct_answers:
    print(word)
print(f'Неправильно отвеченные слова: ')
for word in incorrect_answers:
    print(word)

# Вывод рейтинга
score = len(correct_answers)
print(f'\nВаш рейтинг: = {levels[score]} =')
