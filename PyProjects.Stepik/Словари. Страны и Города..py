"""
На вход программе подается список стран и городов каждой страны.
Затем даны названия городов. Напишите программу, которая
для каждого города выводит, в какой стране он находится.
"""

city_dict = {}
for _ in range(int(input())):
    dict_tuple = input().split()
    dict_tuple = tuple(dict_tuple)
    city_dict.update(city_dict.fromkeys(dict_tuple[1:], dict_tuple[0]))

request = [input() for _ in range(int(input()))]

for key in request:
    print(city_dict[key])
