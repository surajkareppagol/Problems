def rearrangeArray(nums: list) -> list:
    result = []

    for positive, negative in zip(
        [i for i in nums if i > 0], [i for i in nums if i < 0]
    ):
        result.append(positive)
        result.append(negative)

    return result


print(rearrangeArray([3, 1, -2, -5, 2, -4]))
print(rearrangeArray([-1, 1]))
