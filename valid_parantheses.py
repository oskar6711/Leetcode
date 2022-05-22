def is_valid(s: str) -> bool:

    op_b = ['[', '{', '(']
    stack = []

    for p in s:
        if p in op_b:
            stack.append(p)
        elif stack:
            if p == ')' and stack[-1] != '(':
                return False

            if p == ']' and stack[-1] != '[':
                return False

            if p == '}' and stack[-1] != '{':
                return False

            stack.pop()
        else:
            return False

    return len(stack) == 0
