class SuperStr(str):
    def is_repeatance(self, s):
        if self == "":
            return False
        if len(self) % len(s) != 0:
            return False
        repeat_count = len(self) // len(s)
        if self == s * repeat_count:
            return True
        else:
            return False

    def is_palindrom(self):
        normalized_str = self.lower()
        return normalized_str == normalized_str[::-1]


string1 = SuperStr("abcabcabc")
print(string1.is_repeatance("abc"))

string2 = SuperStr("hello")
print(string2.is_repeatance("hi"))

string3 = SuperStr("level")
print(string3.is_palindrom())

string4 = SuperStr("Python")
print(string4.is_palindrom())
