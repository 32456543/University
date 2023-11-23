def read_numbers_from_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            count = int(lines[0])
            numbers = [int(line.strip()) for line in lines[1:count+1]]
            return numbers
    except FileNotFoundError:
        print("Файл не найден.")
        return []
    except ValueError:
        print("Неверный формат чисел в файле.")
        return []
    except Exception as e:
        print("Произошла ошибка:", e)
        return []

try:
    filename = input("Введите имя файла: ")
    numbers = read_numbers_from_file(filename)
    print(numbers)
except Exception as e:
    print("Произошла ошибка:", e)