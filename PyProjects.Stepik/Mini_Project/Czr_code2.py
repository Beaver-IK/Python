'''
На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова.
Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова).
Строчные буквы при этом остаются строчными, а прописные – прописными.
'''

line = input('Please, enter the text:\n')
word_list = line.split()
crypt_list = []

def char_counter(a):
    counter = 0
    list_a = list(a)
    for i in range(len(list_a)):
        c = list_a[i]
        if c.isalpha():
            counter += 1
    return (counter)

for i in range(len(word_list)):
    l = word_list[i]
    lenght = char_counter(l)
    for j in range(len(l)):
        sim = ord(l[j]) + lenght
        if l[j].isalpha():
            if l[j].isupper():
                if sim > 90:
                    sim -= 26
                    crypt_list.append(chr(sim))
                else:
                    crypt_list.append(chr(sim))
            elif sim > 122:
                sim -= 26
                crypt_list.append(chr(sim))
            else:
                crypt_list.append(chr(sim))
        else:
            crypt_list.append(l[j])
    crypt_list.append(' ')
print(''.join(crypt_list))



