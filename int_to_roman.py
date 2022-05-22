def int_to_roman(num: int) -> str:
    roman = [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
             ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
             ('X', 10,), ('IX', 9,), ('V', 5,), ('IV', 4,), ('I', 1)]

    res = ''

    for rom, val in roman:
        if num >= val:
            x = num // val
            res += ''.join(rom * x)
            print(res)
            num -= (val * x)
    return res

print(int_to_roman(24))
