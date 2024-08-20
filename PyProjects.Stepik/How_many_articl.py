'''На вход программе подается строка, содержащая английский текст.
Напишите программу, которая подсчитывает общее количество артиклей: 'a', 'an', 'the' '''

text = input()
text_list = text.split()
art_count = 0
for i in text_list:
    if str(i).lower() == 'a' or str(i).lower() == 'an' or str(i).lower() == 'the':
        art_count += 1
print('Общее количество артиклей:', art_count)
