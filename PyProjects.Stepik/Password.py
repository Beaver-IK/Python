'''
Действительный пароль банка имеет вид a:b:c, где a, b и c – натуральные числа.

число a – должно быть палиндромом;
число b – должно быть простым;
число c – должно быть четным.
'''


def is_valid_password(password):
    flag = False
    password_list = password.split(':')
    if len(password_list) == 3:
        if password_list[0] == password_list[0][::-1]:
            b = int(password_list[1])
            count = 0
            for i in range(1, b + 1):
                if b % i == 0:
                    count += 1
            if count == 2:
                c = int(password_list[2])
                if c % 2 == 0:
                    flag = True
    return (flag)

psw = input()
print(is_valid_password(psw))
