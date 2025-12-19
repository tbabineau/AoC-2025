if __name__ == "__main__":
    fname = "input.txt"
    #fname = "test.txt"
    file = open(fname)
    grid = []
    tot = 0
    temp = 0
    #Taking in the numbers as a big 2D array
    file = file.read().split("\n")
    for line in file:
        row = []
        for var in line:
            row.append(var)
        grid.append(row)
    cols = len(grid[0]) #num of columns
    rows = len(grid) #num of rows
    op = ''
    for i in range(cols):
        num = 0
        for j in range(rows - 1):
            if(grid[j][i] != ' '):
                num = num*10 + int(grid[j][i])
        if(grid[rows-1][i] != ' '):#new operation, have to change it
            op = grid[rows-1][i]
            tot += temp
            if(op == '*'):
                temp = 1
            else:
                temp = 0
        if(num != 0):
            if(op == '*'):
                temp *= num
            else:
                temp += num
    tot += temp
            
    print(tot)