'''Напишите функцию is_password_good(password), которая принимает в качестве аргумента
строковое значение пароля password и возвращает значение True
если пароль является надежным и False в противном случае.

Пароль является надежным если:

его длина не менее 8 символов;
он содержит как минимум одну заглавную букву (верхний регистр);
он содержит как минимум одну строчную букву (нижний регистр);
он содержит хотя бы одну цифру.
'''

def good_password(password):
    flag = False
    if len(password) >= 8:
        if password.islower():
            flag = False
            pass
        elif password.isupper():
            flag = False
            pass
        elif password.isnumeric():
            flag = False
            pass
        elif password.isalpha():
            flag = False
            pass
        else:
            flag = True
            for i in range(len(password)):
                if 48 <= ord(password[i]) <= 57:
                    flag = True
                elif 65 <= ord(password[i]) <= 90:
                    flag = True
                elif 97 <= ord(password[i]) <= 122:
                    flag = True
                else:
                    flag = False
    return (flag)

line = input()
print(good_password(line))
