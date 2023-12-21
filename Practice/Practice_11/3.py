class SuperStr(str):
    def __init__(self, stroka):
        self.stroka = stroka

    def is_repeatance(self, s):
        if not isinstance(s, str):
            return False
        return len(self.stroka.split(s)) > 1

    def is_palindrom(self):
        return self.stroka == self.stroka[::-1]

s = SuperStr("123123123123")
print(s.is_repeatance("123"))  # True
print(s.is_repeatance("123123"))  # True
print(s.is_repeatance("123123123123"))  # True
print(s.is_repeatance("12312"))  # False
print(s.is_repeatance(123))  # False
print(s.is_palindrom())  # False
print(s)  # 123123123123 (строка)
print(int(s))  # 123123123123 (целое число)
print(s + "qwe")  # 123123123123qwe
p = SuperStr("123_321")
print(p.is_palindrom())  # True
