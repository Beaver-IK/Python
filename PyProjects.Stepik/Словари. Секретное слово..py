"""
Напишите программу для расшифровки секретного слова методом
частотного анализа.

"""

word = tuple(input())
word_dict = {}
for key in word:
    word_dict[key] = word_dict.get(key, 0) + 1

frequency_dict = {}
for _ in range(int(input())):
    frequency = tuple(input().split(': '))
    frequency_dict.setdefault(frequency[1], frequency[0])

for key in word:
    print(frequency_dict[f'{word_dict[key]}'], end='')
