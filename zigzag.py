def convert(s: str, num_rows: int) -> str:
    if num_rows == 1:
        return s

    arr = ["" for i in range(len(s))]
    row = 0
    down = True

    for i in range(len(s)):

        arr[row] += s[i]

        if row == num_rows - 1:
            down = False

        elif row == 0:
            down = True

        if down:
            row += 1
        else:
            row -= 1

    result = ''

    for i in range(len(arr)):
        result += arr[i]

    return result
