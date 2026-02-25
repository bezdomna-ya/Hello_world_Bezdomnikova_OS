donor = input("Введите фенотип группы крови ДОНОРА (I, II, III, IV): ").strip().upper()
pacient = input("Введите фенотип группы крови ПАЦИЕНТА (I, II, III, IV): ").strip().upper()
if donor == pacient or donor == "I":
    print("Переливание возможно")
else:
    print("Переливание невозможно")