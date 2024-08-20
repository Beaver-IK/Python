'''На вход программе подается натуральное число n, затем n строк, затем еще одна строка — поисковый запрос.
Напишите программу, которая выводит все введенные строки, в которых встречается поисковый запрос.
Поиск не должен быть чувствителен к регистру'''

main_list = []
for lines in range(int(input())):
    main_list.append(input())
search_line = input()
for search in range(len(main_list)):
    if search_line.lower() in main_list[search].lower():
        print(main_list[search])
