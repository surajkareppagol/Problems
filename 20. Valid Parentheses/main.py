def isValid(s: str) -> bool:
    stk = []

    for br in s:
        if br in ["{", "(", "["]:
            stk.append(br)
        if stk and br == "}" and stk[-1] == "{":
            stk.pop()
        elif stk and br == "]" and stk[-1] == "[":
            stk.pop()
        elif stk and br == ")" and stk[-1] == "(":
            stk.pop()
        else:
            stk.append(br)

    if len(stk) == 0:
        return True
    else:
        return False


print(isValid("]"))
print(isValid(")(){}"))
