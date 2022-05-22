def substring(s):
    start = longest = 0
    seen = {}
    for i in range(len(s)):
        letter = s[i]
        if letter in seen:
            start = max(seen[letter] + 1, start)
            print(start)
        longest = max(longest, i - start + 1)
        print(longest)
        seen[letter] = i
    return longest

print(substring('ababc'))