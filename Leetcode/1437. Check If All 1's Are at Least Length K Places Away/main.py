def kLengthApart(nums: list, k: int) -> bool:
    c = k
    for i in nums:
        if i == 0:
            c += 1
        if i == 1:
            if c < k:
                return False
            c = 0
    return True


print(kLengthApart([1, 0, 0, 0, 1, 0, 0, 1], 2))
print(kLengthApart([1, 0, 0, 1, 0, 1], 2))
