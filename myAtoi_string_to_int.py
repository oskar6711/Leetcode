def my_atoi(self, s: str) -> int:
    fixed_str = s.lstrip()

    if len(fixed_str) == 0:
        return 0

    start = 0
    sign = 1
    if fixed_str[0] == '-':
        sign = -1
        start = 1
    elif fixed_str[0] == '+':
        start = 1

    result = 0
    for i in range(start, len(fixed_str)):

        if not ('0' <= fixed_str[i] <= '9'):
            return result * sign

        result = result * 10 + ord(fixed_str[i]) - ord('0')
        int_range = 2 ** 31
        if result * sign <= -int_range:
            return -int_range
        elif result * sign >= int_range - 1:
            return int_range - 1

    return result * sign
