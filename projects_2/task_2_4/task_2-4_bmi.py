weight = float(input("Введите ваш вес (кг): "))
height = float(input("Введите ваш рост (см): "))
bmi = weight / ((height/100) ** 2)

print("--- Отчет о стостоянии здоровья ---")
print(f"Рост:\t{height}")
print(f"Вес:\t{weight}")
print(f"Индекс массы тела пациента:\t {bmi:.2f}")