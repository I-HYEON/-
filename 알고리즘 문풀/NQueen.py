N = int(input())
col = []
r_diag = []
l_diag = []
num = 0

def backtrack(row):
    global num
    if row == N:
        num += 1
    else:
        for c in range(N):
            if c not in col and row+c not in l_diag and row-c not in r_diag:
                col.append(c)
                l_diag.append(row+c)
                r_diag.append(row-c)
                backtrack(row+1)
                r_diag.pop()
                l_diag.pop()
                col.pop()

backtrack(0)
print(num)