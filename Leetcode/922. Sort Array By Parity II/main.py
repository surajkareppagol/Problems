def sortArrayByParityII(nums: list) -> list:
    even = [i for i in nums if i % 2 == 0]
    odd = [i for i in nums if i % 2 != 0]

    result = []

    for e, o in zip(even, odd):
        result.append(e)
        result.append(o)

    return result


print(sortArrayByParityII([4, 2, 5, 7]))
print(sortArrayByParityII([2, 3]))
