import re

def get_books(stroke):
    pattern = r"(?P<isbn>[\d-]+)(?:\|)(?P<title>[\w\s]+)(?:\|)(?P<author>[\w\s]+)(?:\|)(?P<quantity>\d+)(?:\|)(?P<price>[\d.\d]+)"
    file = open("books.csv").read()
    matches = re.findall(pattern, file)
    arr = list()
    for match in matches:
        for i in range(len(match)):
            if stroke in match[i]:
                arr.append(list(match))
    return arr

def get_totals():
    arr = get_books(gets)
    new_arr = []
    for i in range(len(arr)):
        listik = (arr[i][0], float(arr[i][-1]) * int(arr[i][-2]))
        new_arr.append(listik)

    for i in range(len(new_arr)):
        new_arr[i] = list(new_arr[i])
        if new_arr[i][-1] < 500:
            new_arr[i][-1] += 100

    for i in range(len(new_arr)):
        new_arr[i] = tuple(new_arr[i])

    return new_arr


gets = input("Введите слово: ")
if gets.isalpha():
    print(get_books(gets))
    print(get_totals())
else:
    print("Попробуйте снова\n")