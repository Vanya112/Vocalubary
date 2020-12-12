import os
import re
import random


def finder():
    dict = {}
    counter = 0
    score = 0
    path = "C:\\Users\\Vanek\\Desktop\\Vocalubary\\Dictionary"
    attempts = int(input("Сколько раз повторять: "))
    while attempts < 0 or attempts > 500:
        attempts = int(input("Сколько раз повторять: "))
    letterNumber = int(input("Номер буквы: "))
    while letterNumber < 0 or letterNumber > 25:
        letterNumber = int(input("Номер буквы: "))
    for file in os.listdir(path):
        if counter != letterNumber:
            counter += 1
            continue
        filename = os.fsdecode(file)
        print(f'Файл: {filename}')
        with open(path + "\\" + filename, encoding='utf-8') as f:
            content = f.readlines()
            if (len(content) < 2):
                break
            for line in content:
                english_word = line.split('-')[0]
                translate_word = str(''.join(line.split('-')[2:]))
                if len(translate_word) == 0:
                    translate_word = str(''.join(line.split('-')[1:]))
                english_word = str(re.sub(r'[^a-zA-Z]', '', english_word))
                vocalubary_string = [(english_word, translate_word)]
                dict.update(vocalubary_string)
            break
    words = list(dict.keys())
    translations = list(dict.values())
    for i in range(0, attempts):
        randomNumber = random.randint(0, len(words))
        print(f'Слово: {translations[randomNumber]}')
        answer = input("Введите правильный перевод: ")
        os.system('CLS')
        if answer.lower().replace(' ', '') == words[randomNumber].lower().replace(' ', ''):
            score += 1
            print(f'\nПравильно, {words[randomNumber].lower()}\n')
        else:
            print(f'\nНеправильно, надо {words[randomNumber].lower()}\n')
    os.system('CLS')
    print(f"\nВаш счёт: {score} из {attempts}")



if __name__ == '__main__':
    finder()
