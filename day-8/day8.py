def is_visible(n,m, grid):
    # Check if visible from the right
    for i in range(m+1, len(grid[n])):
        if grid[n][m] <= grid[n][i]:
            return False
    # Check if visible from the left
    for i in range(0, m):
        if grid[n][m] <= grid[n][i]:
            return False
    # Check if visible from above
    for i in range(0, n):
        if grid[n][m] <= grid[i][m]:
            return False
    # Check if visible from below
    for i in range(n, len(grid)):
        if grid[n][m] <= grid[i][m]:
            return False
    return True


data = open("test_input", "r")
forrest = data.readlines()
visible_trees = 0
for n in range(0, len(forrest)):
    for m in range(0, len(forrest[0])):
        if is_visible(n, m, forrest):
            visible_trees += 1
print(visible_trees)
