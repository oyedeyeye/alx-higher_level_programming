def roman_to_int(roman_string):
    if len(roman_string) is not None:
        roman_numerals = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1
        }
        temp = []
        result = 0

        for i in roman_string:
            temp.append(roman_numerals[i])
        if len(temp) == 1:
            result += temp[0]
            return result

        j = 0
        while j < len(temp):
            if temp[j] == temp[len(temp) - 1]:
                result += temp[j]
            elif temp[j] >= temp[j + 1]:
                result += temp[j]
            else:
                result -= temp[j]
            j += 1
        return result
    else:
        return 0
