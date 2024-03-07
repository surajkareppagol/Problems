def findMedianSortedArrays(nums1: list, nums2: list) -> float:
    def insert_values(nums1: list, v):
        for i, val in enumerate(nums1):
            if v < val:
                nums1.insert(i, v)
                return
        nums1.append(v)

    for v in nums2:
        insert_values(nums1, v)

    if len(nums1) % 2 != 0:
        return nums1[len(nums1) // 2]
    else:
        i = len(nums1) // 2
        return (nums1[i] + nums1[i - 1]) / 2


findMedianSortedArrays([1, 3], [2])
findMedianSortedArrays([1, 2], [3, 4])
