# 1을 육지로 0을 물로 가정한 2D 그리드 맵이 주어졌을 때, 섬의 개수를 계산하라. (연결되어 있는 1의 덩어리 개수를 구하라.)

grid1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]


# def numOfIsland(grid):
#     def dfs(i, j):
#         if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
#             return
#         grid[i][j] = '0'
#
#         dfs(i + 1, j)
#         dfs(i - 1, j)
#         dfs(i, j + 1)
#         dfs(i, j - 1)
#
#     count = 0
#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             if grid[i][j] == '1':
#                 dfs(i, j)
#                 count += 1
#
#     return count
#
#
# print(numOfIsland(grid1))
# print(numOfIsland(grid2))


def numOfIsland(grid):
    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
            return
        grid[i][j] = '0'

        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1

    return count


print(numOfIsland(grid1))
print(numOfIsland(grid2))
