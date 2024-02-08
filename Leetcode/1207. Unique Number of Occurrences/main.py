def uniqueOccurrences(arr) -> bool:
    occurrences = {}

    for i in arr:
        if i not in occurrences.keys():
            occurrences[i] = 1
        else:
            occurrences[i] += 1

    repeated = []

    for c in occurrences.values():
        if c in repeated:
            return False
        else:
            repeated.append(c)

    return True


print(uniqueOccurrences([1, 2, 2, 1, 1, 3]))
print(uniqueOccurrences([1, 2]))
print(uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))
