def sortArrayByParityII(nums: list) -> list:
    even, odd = [], []

    for i in nums:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    result = []

    for i in zip(even, odd):
        result.extend(i)

    return result


print(sortArrayByParityII([4, 2, 5, 7]))
print(sortArrayByParityII([2, 3]))
