"""Программа тест для инженера заправщика картриджей"""

# Необходимые переменные
hp = {'Q2612A': '2500 стр',
      'CE285A': '1500 стр',
      'CF280X': '6000 стр'
      }
canon = {'Canon 728': '1500 стр',
         'Canon 718': '3000 стр',
         'Canon E16': '3000 стр'
         }
kyocera = {'TK-1140': '7200 стр',
           'TK-3130': '12000 стр',
           'TK-130': '3000 стр'}
levels = {
   0: "Нулевой",
   1: "Так себе",
   2: "Можно лучше",
   3: "Норм",
   4: "Хорошо",
   5: "Отлично",
}

# Программа приветствует пользователя. Спрашивает имя и предлагает выбрать бренд компании по
# которой будет проходить тест.
print('Привет кандидат. Впишите свое имя и выберите компанию, по которой будете проходить тест')
user_name = input('Ваше имя: ').upper()
print(f'{user_name} выберите компанию: HP, CANON, KYOCERA')

# Выбор теста
user_answer = None
while user_answer != hp or canon or kyocera:
    user_answer = input().lower()
    if user_answer == 'hp':
        print(f'Вы выбрали {user_answer.upper()}. Вам нужно угадать ресурс страниц картриджа по его'
              f'названию')
        cartridges = hp
        break
    elif user_answer == 'canon':
        print(f'Вы выбрали {user_answer.upper()}. Вам нужно угадать ресурс страниц картриджа по его'
              f'названию')
        cartridges = canon
        break
    elif user_answer == 'kyocera':
        print(f'Вы выбрали {user_answer.upper()}. Вам нужно угадать ресурс страниц картриджа по его'
              f'названию')
        cartridges = kyocera
        break
    else:
        print('Вы неправильно написали название бренда')

for cartridge, pages in cartridges.items():
    print(f'Картридж: {cartridge}')
    user_input = input('На какое количество страниц он рассчитан?: ')
    if user_input in pages:
        print('Верно')
    else:
        print('Неверно')