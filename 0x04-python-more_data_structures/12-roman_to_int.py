#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    if not roman_string.isupper():
        return 0

    roman_numerals = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
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
