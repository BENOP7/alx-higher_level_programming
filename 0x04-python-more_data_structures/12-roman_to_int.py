#!/usr/bin/python3

def roman_to_int(roman_string):

    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {'I': 1, 'V': 5,
                  'X': 10, 'L': 50,
                  'C': 100, 'D': 500,
                  'M': 1000}

    roman_string = roman_string.upper()
    res = 0
    size = len(roman_string)
    i = 0

    while i < size:
        if roman_string[i] in roman_dict:
            if i + 1 < size:
                if roman_string[i] in 'I' and roman_string[i + 1]\
                        in ['V', 'X']:
                    res += roman_dict[roman_string[i + 1]] - 1
                    i += 2
                elif roman_string[i] in 'X' and\
                        roman_string[i + 1] in ['L', 'C']:
                    res += roman_dict[roman_string[i + 1]] - 10
                    i += 2
                elif roman_string[i] in 'C' and roman_string[i + 1]\
                        in ['D', 'M']:
                    res += roman_dict[roman_string[i + 1]] - 100
                    i += 2
                else:
                    res += roman_dict[roman_string[i]]
                    i += 1
            else:
                res += roman_dict[roman_string[i]]
                i += 1

    return res
