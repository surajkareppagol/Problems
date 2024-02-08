def areOccurrencesEqual(s: str) -> bool:
    occurrences = {}

    for i in s:
        if i not in occurrences.keys():
            occurrences[i] = 1
        else:
            occurrences[i] += 1

    initial_value = occurrences[s[0]]

    for c in occurrences.values():
        if c != initial_value:
            return False

    return True


print(areOccurrencesEqual("aab"))
