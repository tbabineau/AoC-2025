if __name__ == "__main__":
    fname = "input.txt"
    #fname = "test.txt"
    file = open(fname)
    grid = []
    tot = 0
    #Taking in the numbers as a big 2D array
    for line in file:
        row = []
        line = line.strip().split(" ")
        for var in line:
            if(var != ''):
                row.append(var)
        grid.append(row)
    cols = len(grid[0]) #num of columns
    rows = len(grid) #num of rows
    for i in range(cols):
        op = grid[rows-1][i]
        temp = (op == '*') #Will be a 1 if multiplying, 0 if adding
        for j in range(rows-1):
            if(op == '+'):
                temp += int(grid[j][i])
            else:
                temp *= int(grid[j][i])
        tot += temp
    print(tot)
    
