# Задание 4
with open('task4', 'r') as f:
    line = 0
    for x in f:
        line = line + 1
        print(x, len(x))
print(line)

# Домашнее задание
lst1 = ['hello', 1, 4, 56, 76, 'worlds', 13, 'word']
lst_num = []
lst_alpha = []
for item in lst1:
    if type(item) == str:
        lst_alpha.append(item)
    elif type(item) == int:
        lst_num.append(str(item))
lst_num.sort(key=int)
lst_alpha.sort(key=len)
with open('taskhw', 'w') as f:
    for elem in lst_alpha:
        f.writelines(elem + ' ')
    f.writelines('\n')
    for elem in lst_num:
        f.writelines(elem + ' ')

