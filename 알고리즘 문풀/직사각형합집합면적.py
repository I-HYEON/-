grid = [[0 for _ in range(100)]for _ in range(100)]
for _ in range(4):
    j1,i1,j2,i2 = map(int,input().split())
    for i in range(i1,i2):
        for j in range(j1,j2):
            grid[i][j] = 1

sum = 0
for i in range(100):
    for j in range(100):
        sum += grid[i][j]

print(sum)