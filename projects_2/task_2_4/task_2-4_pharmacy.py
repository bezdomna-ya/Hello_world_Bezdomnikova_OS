capcule_quntity = int(input("Общее количество произведенных капсул: "))
packing_capacity = int(input("Вместимость одной упаковки: "))
full_packs = capcule_quntity // packing_capacity
remains = capcule_quntity % packing_capacity

print("--- Отчет фасовочного цеха ---")
print(f"Полных упаковок:\t {full_packs}")
print(f"Остаток капсул:\t\t {remains}")