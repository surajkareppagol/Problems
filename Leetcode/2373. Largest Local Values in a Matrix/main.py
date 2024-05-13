from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        # 1. Get the result grid size
        n_ = len(grid) - 2
        row_ = 0
        column_ = 0

        # 2. Set row and column origins
        column_origin = 0
        row_origin = 0

        # 3. Create a string grid
        string_grid = ["" for _ in range(n_)]
        string_index = 0

        # 4. For each strip get the value
        for _ in range(n_):
            for _ in range(n_):
                inter = []

                for i in range(row_, row_ + 3):
                    for j in range(column_, column_ + 3):
                        inter.append(grid[i][j])

                string_grid[string_index] = f"{string_grid[string_index]},{max(inter)}"

                row_ += 1
                column_ = column_origin
                string_index += 1

            # 5. Change to new strip
            row_ = row_origin
            column_origin += 1
            column_ = column_origin
            string_index = 0

        grid_ = []

        # 6. Collect values from string grid
        for i in string_grid:
            string = []
            for j in i.split(","):
                if j.isdigit():
                    string.append(int(j))
            grid_.append(string)

        return grid_


# ====================== #
# Minor Changes

# class Solution:
#     def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
#         # 1. Get the result grid size
#         n_ = len(grid) - 2
#         row_ = 0
#         column_ = 0

#         grid_ = [[0 for _ in range(n_)] for _ in range(n_)]
#         grid_row = 0
#         grid_column = 0

#         # 2. Set row and column origins
#         column_origin = 0
#         row_origin = 0

#         # 3. For each strip get the value
#         for _ in range(n_):
#             for _ in range(n_):
#                 max_ = 0

#                 for i in range(row_, row_ + 3):
#                     for j in range(column_, column_ + 3):
#                         if grid[i][j] > max_:
#                             max_ = grid[i][j]

#                 grid_[grid_row][grid_column] = max_

#                 row_ += 1
#                 column_ = column_origin
#                 grid_row += 1

#             # 4. Change to new strip
#             row_ = row_origin
#             column_origin += 1
#             column_ = column_origin
#             grid_row = 0
#             grid_column += 1

#         return grid_


# ====================== #

result = Solution().largestLocal(
    [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]
)
print(result)

# ====================== #

result = Solution().largestLocal(
    [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 2, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
    ]
)
print(result)

# ====================== #
