def input_float():
    while True:
        try:
            float_number = float(input("Введите десятичное число: "))
            return float_number
        except ValueError:
            print("Это не десятичное число!")

# Пример использования
input_float_number = input_float()
print(input_float_number)