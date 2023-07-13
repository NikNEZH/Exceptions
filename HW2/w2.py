int_array = [0, 1, 2, 3, 4, 5, 6, 1, 8, 9]

d = 1
if len(int_array) - 1 < 8:
    print("Массив содержит недостаточно элементов")
elif d == 0:
    print("Деление на 0")
else:
    catched_res1 = int_array[8] / d
    print("catchedRes1 =", catched_res1)