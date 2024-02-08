def isSumEqual(firstWord: str, secondWord: str, targetWord: str) -> bool:
    first_num = ""
    for i in firstWord:
        first_num += str(ord(i) - 97)
    second_num = ""
    for i in secondWord:
        second_num += str(ord(i) - 97)
    target_num = ""
    for i in targetWord:
        target_num += str(ord(i) - 97)

    if int(first_num) + int(second_num) == int(target_num):
        print(True)
    print(False)


isSumEqual("acb", "cba", "cdb")
isSumEqual("aaa", "a", "aab")
isSumEqual("aaa", "a", "aaaa")
