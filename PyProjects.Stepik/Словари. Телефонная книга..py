"""
Тимур записал телефоны всех своих друзей, чтобы автоматизировать поиск нужного номера.

У каждого из друзей Тимура может быть один или более телефонных номеров.
Напишите программу, которая поможет Тимуру находить все номера определённого друга.
"""

phone_book = {}

for _ in range(int(input())):
    phone = tuple(input().split())
    phone_book.setdefault(phone[1].capitalize(), []).append(phone[0])


request = []
for _ in range(int(input())):
    request.append(input().capitalize())

for key in request:
    if key in phone_book:
        print(*phone_book[key])
    else:
        print('абонент не найден')

