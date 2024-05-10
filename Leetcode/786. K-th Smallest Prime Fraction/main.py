from typing import List

# ====================== #
# METHOD 1 - Time Limit Exceeded

# class Solution:
#     def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
#         result_str = []
#         result_int = []

#         result = []

#         for i in range(0, len(arr)):
#             for j in range(i, len(arr)):
#                 if i != j:
#                     result_int.append(arr[i] / arr[j])
#                     result_str.append(f"{arr[i]}/{arr[j]}")

#         for i in range(len(result_int)):
#             min_ = min(result_int)
#             min_index = result_int.index(min_)

#             result.append(result_str[min_index])
#             result_int[min_index] = 9999999

#             if len(result) >= k:
#                 break

#         return list(map(int, result[k - 1].split("/")))

# ====================== #
# METHOD 2 - Time Limit Exceeded


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        result = {}

        arr = tuple(arr)

        for i in range(0, len(arr)):
            for j in range(i, len(arr)):
                if i != j:
                    result[arr[i] / arr[j]] = f"{arr[i]}/{arr[j]}"

        i = 0
        while True:
            min_ = min(set(result.keys()))
            if i == k - 1:
                break

            del result[min_]
            i += 1

        return list(map(int, result[min_].split("/")))


# ====================== #

result = Solution().kthSmallestPrimeFraction([1, 2, 3, 5], 3)
print(result)

# ====================== #

result = Solution().kthSmallestPrimeFraction([1, 7], 1)
print(result)

# ====================== #
