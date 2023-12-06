import re

file = open("journal.txt", encoding='utf8').read()

pattern = r"(?:.+)(?P<route>[0-9]{3})(?:\s.[^\s]+\s)(?P<cities>[а-я]+\s[А-Я][а-я]+)(?:\s.\s)(?P<time>\d+:\d+:\d+)"
match = re.findall(pattern, file)

with open("new_journal.txt", "w", encoding='utf8') as f:
    matches = re.finditer(pattern, file)
    for match in matches:
        f.write(f"[{match.group('time')}] - Поезд № {match.group('route')} {match.group('cities')}\n")