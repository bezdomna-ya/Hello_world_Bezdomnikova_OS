fio = input("Введите имя оператора: ")
pressure = input("Введите текущее значение давления (Па): ")

with open("sensor_log.txt", "w", encoding="utf-8") as info:
    info.write(f"Оператор\tЗначение\n{fio}\t{pressure}")

print("Данные успешно сохранены в sensor_log.txt")