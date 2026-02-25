fio = input("ФИО исследователя : ")
date = input("Дата: ")
expirement = input("Название эксперимента: ")
conclusion = input("Вывод: ")

lines = [
    "Электронный лабораторный журнал",
    f"ФИО исследователя : {fio}",
    f"Дата    : {date}",
    f"Эксперимент    : {expirement}",
    f"Вывод: {conclusion}"
]

max_len = max(len(line) for line in lines)
border = '+' + '-' * (max_len + 2) + '+'

with open('journal.txt', 'w', encoding='utf-8') as f:
    print(border, file=f)
    print(f"| {lines[0]:<{max_len}} |", file=f)
    print(border, file=f)
    for line in lines[1:5]:  
        print(f"| {line:<{max_len}} |", file=f)
    print(border, file=f)
    print(f"| {lines[-1]:<{max_len}} |", file=f)
    print(border, file=f)

print("Файл 'journal.txt' успешно сформирован!")
