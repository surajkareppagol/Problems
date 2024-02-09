def count_substring(string, sub_string):
    c = 0

    for i in range(len(string) + 1):
        for j in range(i + 1):
            if i != j:
                c += 1 if string[j:i] == sub_string else 0
    return c


if __name__ == "__main__":
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
