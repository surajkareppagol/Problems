from typing import List

# ====================== #
# METHOD 1 - Time Limit Exceeded


# class Solution:
#     def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
#         max_happiness = 0
#         happiness = sorted(happiness)

#         for _ in range(k):
#             max_happiness += happiness.pop()

#             for i in range(0, len(happiness)):
#                 if happiness[i] > 0:
#                     happiness[i] -= 1

#         return max_happiness


# ====================== #
# METHOD 2 - From Editorial


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # 1. Sort happiness
        happiness = sorted(happiness, reverse=True)

        total = 0
        turns = 0

        # Add the max value
        for i in range(k):
            total += max(happiness[i] - turns, 0)

            turns += 1

        return total


# ====================== #

result = Solution().maximumHappinessSum([1, 2, 3], 2)
print(result)

# ====================== #

result = Solution().maximumHappinessSum([1, 1, 1, 1], 2)
print(result)

# ====================== #

result = Solution().maximumHappinessSum([2, 3, 4, 5], 1)
print(result)

# ====================== #
