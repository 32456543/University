from cod import *
#меню по смене дирректиории
def changing_directory():
    path = input("Укажите путь к рабочему каталогу: ")
    change_catalog(path)
    print()

#функция конвертирует из pdf в docx и наоборот
#file_format формат файла из которого конвертируется
def converter_file(file_format: str):
    files = get_files_format(get_current_catalog(), file_format)
    count = 1
    if len(files) == 0:
        if file_format == ".pdf":
            print("0 файлов PDF в данной директории.")
        elif file_format == ".docx":
            print("0 файлов Docx в данной директории.")
        print()
        return

    print(f"Список файлов с расширением {file_format} в данном каталоге:\n")

    for file in files:
        print(f"{count}. {file}")
        count += 1
    try:
        num = int(input("Введите номер файла для преобразования "
                        ",чтобы преобразовать все файлы "
                        "из данного каталога введите: "))

        if 0 <= num <= len(files):
            if num == 0:
                if file_format == ".pdf":
                    all_convert_pdf_to_docx(files)
                elif file_format == ".docx":
                    all_convert_docx_to_pdf(files)
            else:
                if file_format == ".pdf":
                    convert_pdf_to_docx(files[num - 1])
                elif file_format == ".docx":
                    convert_docx_to_pdf(files[num - 1])
        else:
            print("Такого числа нет в списке!")
    except ValueError:
        print("Введено не число!")
    print()

#меню для сжатия изображения
def image_compression():
    files = get_files_formats(get_current_catalog(), [".jpeg", ".gif", ".png", ".JPG"])
    count = 1

    if len(files) == 0:
        print("0 файлов изображения в данной директории.\n")
        return

    print("Список файлов с расширением (\'.jpeg\', \'.gif\', \'.png\', \'.JPG\') в данном каталоге: \n")

    for file in files:
        print(f"{count}. {file}")
        count += 1

    try:
        num = int(input("Введите номер файла для преобразования "
                        ",чтобы преобразовать все файлы "
                        "из данного каталога введите 0: "))

        if 0 <= num <= len(files):
            quality = int(input("Введите параметр сжатия (от 0 до 105): "))
            if 0 <= quality <= 105:
                if num == 0:
                    for file in files:
                        compression(file, quality)
                else:
                    compression(files[num - 1], quality)
            else:
                print("Число не входит в диапозон от 0 до 105")
    except ValueError:
        print("Введено не число!")
    print()

#меню для удаления
def delete_files():
    print("Выберите действие:\n\n1. Удалить все файлы начинающиеся на определенную подстроку"
          "\n2. Удалить все файлы заканчивающиеся на определенную подстроку"
          "\n3. Удалить все файлы содержащие определенную подстроку"
          "\n4. Удалить все файлы по расширению")
    num = input("Введите номер действия: ")

    match num:
        case "1":
            delete_files_start(get_current_catalog(), input("Введите подстроку: "))
        case "2":
            delete_files_end(get_current_catalog(), input("Введите подстроку: "))
        case "3":
            delete_files_inside(get_current_catalog(), input("Введите подстроку: "))
        case "4":
            delete_files_formats(get_current_catalog(), input("Введите подстроку: "))
        case _:
            print("Нет такого действия!")

#основное меню
def show():
    while True:
        print(f"Текущий каталог: {get_current_catalog()}\n\nВыберите действие: \n\n0. Сменить рабочий каталог\n"
              f"1. Преобразовать PDF в Docx\n2. Преобразовать Docx в PDF\n"
              f"3. Произвести сжатие изображения\n4. Удалить группу файлов\n5. Выход\n")
        user_input = input("Ваш выбор: ")
        print()

        match user_input:
            case "0":
                changing_directory()
            case "1":
                converter_file(".pdf")
            case "2":
                converter_file(".docx")
            case "3":
                image_compression()
            case "4":
                delete_files()
            case "5":
                break


if __name__ == "__main__":
    show()
