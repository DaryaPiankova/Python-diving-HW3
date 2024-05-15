things_dict = {
    "палатка": 5,
    "посуда на 1 чел.": 1,
    "фонарь": 0.2,
    "лопата": 0.8,
    "спальный мешок": 1,
    "продукты на 1 чел.": 2,
}
backpack_weight = int(input("Введите грузоподъемность вашего рюкзака: "))
packed_things = []

for k, v in things_dict.items():
    if (backpack_weight - v) < 0:
        break
    else:
        packed_things.append(k)
        backpack_weight -= v
print(packed_things)
