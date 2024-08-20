'''
Необходимо написать программу, реализующую алгоритм написания этой песни.
Алгоритм выводит в конце предложения следующую в алфавитном порядке букву,
если она встречается в строке текста, а очередную строку отображает уже без этой буквы.
'''


alpha_list = [chr(x) for x in range(ord('а'), ord('я') + 1)]
line = input()
full_line = [line]
full_line.append('запретил букву')
line = ' '.join(full_line)
i = 0
while len(line) > 0:
    if alpha_list[i] in line:
        print(line, alpha_list[i])
        while alpha_list[i] in line or '  ' in line:
            line = line.replace(alpha_list[i], '')
            line = line.lstrip()
            line = ' '.join(line.split())
        i += 1
    else:
        i += 1
