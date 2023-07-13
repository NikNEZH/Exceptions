class InvalidDataException(Exception):
    pass

class UserData:
    def __init__(self, last_name, first_name, middle_name, date_of_birth, phone_number, gender):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number
        self.gender = gender

def main():
    try:
        input_data = input("Введите данные в формате: Фамилия Имя Отчество датарождения номертелефона пол\n")
        data = input_data.split(" ")
        if len(data) != 6:
            raise InvalidDataException("Неверное количество данных")

        last_name = data[0]
        first_name = data[1]
        middle_name = data[2]
        date_of_birth = data[3]
        phone_number = int(data[4])
        gender = data[5]

        validate_data(last_name, first_name, middle_name, date_of_birth, phone_number, gender)

        user_data = UserData(last_name, first_name, middle_name, date_of_birth, phone_number, gender)

        save_user_data(user_data)
    except InvalidDataException as e:
        print("Ошибка: " + str(e))
    except ValueError:
        print("Ошибка: Неверный формат номера телефона")
    except Exception as e:
        print("Ошибка: " + str(e))
        raise

def validate_data(last_name, first_name, middle_name, date_of_birth, phone_number, gender):
    if not last_name or not first_name or not middle_name or not date_of_birth or not gender:
        raise InvalidDataException("Отсутствуют обязательные данные")

    if len(date_of_birth) != 10 or date_of_birth[2] != '.' or date_of_birth[5] != '.':
        raise InvalidDataException("Неверный формат даты рождения")

    if not gender in ['f', 'm']:
        raise InvalidDataException("Неверный символ пола")

def save_user_data(user_data):
    filename = user_data.last_name + ".txt"
    with open(filename, "a") as file:
        file.write(user_data.last_name + user_data.first_name + user_data.middle_name +
                   " " + user_data.date_of_birth + " " + str(user_data.phone_number) +
                   user_data.gender + "\n")
    print("Данные успешно сохранены в файл: " + filename)

if __name__ == "__main__":
    main()