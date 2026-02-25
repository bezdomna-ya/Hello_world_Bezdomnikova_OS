name_of_nutrient_medium = input("Введите название питательной среды: ")
agar_concentation = input("Введите концентрацию агара (%): ")
sterilization_temp = input("Введите температуру стерилизации (°C): ")

with open("recipe.txt", "w", encoding="utf-8") as recipe:
    recipe.write(f"\t{name_of_nutrient_medium}\n-- {agar_concentation}\n-- {sterilization_temp}")

print("Файл 'recipe.txt' успешно сформирован!")