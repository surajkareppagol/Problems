input_value = input()

lowercase, uppercase, odd_digits, even_digits = [], [], [], []

for i in input_value:
    if i.isupper():
        uppercase.append(i)
    elif i.islower():
        lowercase.append(i)
    elif int(i) % 2 != 0:
        odd_digits.append(i)
    else:
        even_digits.append(i)

print(
    f'{"".join(sorted(lowercase))}{"".join(sorted(uppercase))}{"".join(sorted(odd_digits))}{"".join(sorted(even_digits))}'
)
