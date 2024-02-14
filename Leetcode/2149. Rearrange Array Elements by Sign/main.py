def rearrangeArray(nums: list) -> list:
    positive = [i for i in nums if i > 0]
    negative = [i for i in nums if i < 0]

    result = []
    for i in range(len(positive)):
        result.append(positive[i])
        result.append(negative[i])

    return result


print(rearrangeArray([3, 1, -2, -5, 2, -4]))
print(rearrangeArray([-1, 1]))
