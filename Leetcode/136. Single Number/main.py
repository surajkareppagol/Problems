def singleNumber(nums: list) -> int:
    initial = []
    for i in nums:
        if i in initial:
            initial.remove(i)
            continue
        initial.append(i)

    return initial[0]


print(singleNumber([2, 2, 1]))
print(singleNumber([4, 1, 2, 1, 2]))
print(singleNumber([1]))

# Another approach is using XOR, which leads to o(1) space

# def singleNumber(nums: list) -> int:
#     xor = 0
#     for num in nums:
#         xor ^= num

#     return xor
