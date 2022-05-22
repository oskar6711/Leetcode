def divide(dividend, divisor):
    abs_dividend = abs(dividend)
    abs_divisor = abs(divisor)
    result = 0
    while abs_dividend >= abs_divisor:
        if abs_dividend >= abs_divisor:
            abs_dividend -= abs_divisor
            result += 1

    if min(divisor, dividend) < 0 and (dividend > 0 or divisor > 0):
        return 0 - result
    return result


print(divide(10, 5))