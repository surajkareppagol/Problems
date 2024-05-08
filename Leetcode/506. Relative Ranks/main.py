from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rankings = ["" for _ in score]

        initial_rankings = 1
        for _ in range(len(score)):
            max_ = max(score)
            index_ = score.index(max_)
            score[index_] = -1

            if initial_rankings == 1:
                rankings[index_] = "Gold Medal"
            elif initial_rankings == 2:
                rankings[index_] = "Silver Medal"
            elif initial_rankings == 3:
                rankings[index_] = "Bronze Medal"
            else:
                rankings[index_] = str(initial_rankings)

            initial_rankings += 1

        return rankings


# ====================== #

result = Solution().findRelativeRanks([5, 4, 3, 2, 1])
print(result)

# ====================== #

result = Solution().findRelativeRanks([10, 3, 8, 9, 4])
print(result)

# ====================== #

result = Solution().findRelativeRanks([123123, 11921, 1, 0, 123])
print(result)

# ====================== #
