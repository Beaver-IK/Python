


row = [x for x in input().split()]
n = int(input())
finish_list = []
for i in range(n):
    finish_list.append(row[i::n])

print(finish_list)
