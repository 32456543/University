import os
from PIL import Image
from pdf2docx import Converter
from docx2pdf import convert


#текущий каталог
def get_current_catalog():
    return os.getcwd()

#функция меняет каталог
#path путь к каталогу
def change_catalog(path: str):
    if is_valid_path(path):
        os.chdir(path)

#проверка путя
#path путь к каталогу
def is_valid_path(path: str) -> bool:
    check = True
    if not os.path.exists(path):
        print(f"Такого пути \"{path}\" нет")
        return False
    else:
        return True

#Получение файлов по формату
#path каталог
#file_format формат файла
def get_files_format(path: str, file_format: str):
    files = []
    for file in os.listdir(path):
        if file.endswith(file_format):
            files.append(file)
    return files

#Получение файлов по несколько форматам
#path каталог
#file_format формат файла
def get_files_formats(path: str, file_formats: list):
    files = []
    for i in file_formats:
        for file in get_files_format(path, i):
            files.append(file)
    return files

#удаление файлов по формату
#path_name имя файла
#file_format формат файла
def delete_files_formats(path_name: str, file_format: str):
    files = get_files_format(path_name, file_format)
    if len(files) == 0:
        print("Нет файлов для удаления!")
    for file in files:
        os.remove(file)
        print(f"Файл: \"{file}\" успешно удалён!")

#удаление файлов по начальной подстраке
#path_name имя файла
#file_start начальная подстрака
def delete_files_start(path_name: str, file_start: str):
    files = []
    for file in os.listdir(path_name):
        if file.startswith(file_start):
            files.append(file)
    if len(files) == 0:
        print("Нет файлов для удаления!")
    for file in files:
        os.remove(file)
        print(f"Файл: \"{file}\" успешно удалён!")

#удаление файлов по концу названия
#path_name имя файла
#file_end конечная подстрака
def delete_files_end(path_name: str, file_end: str):
    files = []
    for file in os.listdir(path_name):
        if file.rsplit('.', maxsplit=1)[0].endswith(file_end):
            files.append(file)
    if len(files) == 0:
        print("Нету файлов для удаления")
    for file in files:
        os.remove(file)
        print(f"Файл: \"{file}\" успешно удалён")

#Удаление файла если есть подстрока в название файла
#path_name имя файла
#file_inside подстрока внутри слова
def delete_files_inside(path_name: str, file_inside: str):
    files = []
    for file in os.listdir(path_name):
        if file_inside in file.rsplit('.', maxsplit=1)[0]:
            files.append(file)
    if len(files) == 0:
        print("Нет файлов для удаления")
    for file in files:
        os.remove(file)
        print(f"Файл: \"{file}\" успешно удалён")

#сжатие изображения
#image_path пусть или название
#qeality качество сжатия
def compression(image_path: str, quality: int):
    image_file = Image.open(image_path)
    image_file.save(image_path, quality=quality)

#функция возращает список файлов PDF
#path каталог
def get_files_pdf(path: str) -> list:
    return get_files_format(path, ".pdf")

#функция возращает список файлов DOCX
#path каталог
def get_files_docx(path: str) -> list:
    return get_files_format(path, ".docx")

#конвертация всех файлов pdf in docx
#files список файлов
def all_convert_pdf_to_docx(files: list):
    for pdf_file in files:
        convert_pdf_to_docx(pdf_file)

#конвертация файла pdf in docx
#files список файлов
def convert_pdf_to_docx(pdf_file: str):
    docx_file = str(pdf_file) + ".docx"
    cv = Converter(pdf_file)
    cv.convert(docx_file)
    cv.close()

#конвертация всех файла docx in pdf
#files список файлов
def all_convert_docx_to_pdf(files: list):
    for pdf_file in files:
        convert_docx_to_pdf(pdf_file)

#конвертация файла docx in pdf
#files список файлов
def convert_docx_to_pdf(docx_file: str):
    convert(docx_file, docx_file + ".pdf")