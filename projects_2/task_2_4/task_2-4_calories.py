proteins = int(input("Масса белков в продукте (г): "))
fats = int(input("Масса жиров в продукте (г): "))
carbs = int(input("Масса углеводов в продукте (г): "))
calories = proteins*4 + fats*9 + carbs*4
print(f"Количеситво ккал в продукте: {calories}")