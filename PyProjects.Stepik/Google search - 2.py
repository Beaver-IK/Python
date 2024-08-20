'''На вход программе подается натуральное число n, затем n строк,
затем число k — количество поисковых запросов, затем k строк — поисковые запросы.
Напишите программу, которая выводит все введенные строки, в которых встречаются все поисковые запросы.'''




main_list = []
search_list = []
for lines in range(int(input())):
    main_list.append(input())
for search in range(int(input())):
    search_list.append(input())
    
for i in main_list:
    hit_couter = 0
    for j in search_list:
        if j.lower() in i.lower():
            hit_couter += 1
        if hit_couter == len(search_list):
            print(i)
