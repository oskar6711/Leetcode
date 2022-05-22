def reverse(x: int) -> int:

    sign_multiplier = 1

    if x < 0:
        sign_multiplier = -1
        x *= sign_multiplier

    result = 0
    int_range = 2 ** 31

    while x > 0:

        result = result * 10 + x % 10

        if result * sign_multiplier <= -int_range or result * sign_multiplier >= int_range - 1:
            return 0

        x //= 10

    return result * sign_multiplier
