#!/usr/bin/env python
# -*- coding: utf-8 -*-


def roman2int(roman: str) -> int:
    """
        roman to integer
    :param roman:
    :return:
    """
    roman_dict_common = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
    }

    roman_dict_unique = {
        "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900
    }
    result = 0
    for key, value in roman_dict_unique.items():
        result += roman.count(key) * value
        roman = roman.replace(key, "")
    for key, value in roman_dict_common.items():
        result += roman.count(key) * value
    return result


if __name__ == '__main__':
    print(roman2int("MCMXCIX"))
