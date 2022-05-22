def letter_combinations(digits):

    if digits == "":
        return []

    letters = {'2': 'abc',
               '3': 'def',
               '4': 'ghi',
               '5': 'jkl',
               '6': 'mno',
               '7': 'pqrs',
               '8': 'tuv',
               '9': 'wxyz'}

    result = ['']

    for i in digits:
        temp = []
        print(f'Temp[{i}]: {temp}')
        for j in result:
            print(f'Result: {result}')
            for k in letters[i]:
                temp.append(j + k)
                print(f'Temp_add: {temp}')
        result = temp

    return result


print(letter_combinations('234'))
