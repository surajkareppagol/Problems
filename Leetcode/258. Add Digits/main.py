def addDigits(num: int) -> int:
    result = 0
    last_digit = 0

    while True:
        for _ in range(len(str(num))):
            last_digit = num % 10
            result += last_digit
            num //= 10

        if len(str(result)) == 1:
            break

        num = result
        result = 0

    return result


print(addDigits(38))
print(addDigits(0))
