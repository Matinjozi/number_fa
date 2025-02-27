from .converter import NumberFa


class Number_Fa():
    def __init__(self):
        self.dict1 = {
            0: "صفر", 1: "یک", 2: "دو", 3: "سه", 4: "چهار", 5: "پنج", 6: "شش", 7: "هفت", 8: "هشت", 9: "نه",
            10: "ده", 11: "یازده", 12: "دوازده", 13: "سیزده", 14: "چهارده", 15: "پانزده", 16: "شانزده",
            17: "هفده", 18: "هجده", 19: "نوزده"
        }

        self.dict2 = {
            20: "بیست", 30: "سی", 40: "چهل", 50: "پنجاه", 60: "شصت", 70: "هفتاد", 80: "هشتاد", 90: "نود"
        }

        self.dict3 = {
            100: "صد", 200: "دویست", 300: "سیصد", 400: "چهارصد", 500: "پانصد",
            600: "ششصد", 700: "هفتصد", 800: "هشتصد", 900: "نهصد"
        }
        self.v = "و"

    def number_1_chr(self, number):
        if number in self.dict1:
            return self.dict1[number]

    def number_2_chr(self, number):

        if 10 <= number < 20:
            if number in self.dict1:
                return self.dict1[number]

        tens = (number // 10) * 10  # قسمت دهگان (20)
        ones = number % 10  # قسمت یکان (6)
        if tens in self.dict2:
            if ones in self.dict1:
                if ones == 0:
                    return self.dict2[tens]
                else:
                    return self.dict2[tens] + " " + self.v + " " + self.dict1[ones]

    def number_3_chr(self, number):
        hundreds = (number // 100) * 100  # بخش صدگان (300)
        tens = ((number % 100) // 10) * 10  # بخش دهگان (40)
        ones = number % 10  # بخش یکان (5)

        number_min = number - 100
        if 1 <= number_min < 20:
            if number_min in self.dict1:
                return self.dict3[hundreds] + " " + self.v + " " + self.dict1[number_min]

        if hundreds in self.dict3:

            if tens in self.dict2:

                if ones in self.dict1:

                    if ones == 0:
                        return self.dict3[hundreds] + " " + self.v + " " + self.dict2[tens]

                    return self.dict3[hundreds] + " " + self.v + " " + self.dict2[tens] + " " + self.v + " " + \
                        self.dict1[ones]
