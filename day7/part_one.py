if __name__ == "__main__":
    #fname = "input.txt"
    fname = "test.txt"
    file = open(fname)
    grid = []
    split_count = 0
    for line in file:
        row = []
        for char in line:
            if(char != '\n'):
                row.append(char)
        grid.append(row)
    
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows-1): #No splitting happens on the bottom row
        for j in range(cols):
            if(grid[i][j] == 'S'):
                grid[i+1][j] = '|'
            elif(grid[i][j] == '|'):
                if(grid[i+1][j] == '^'):
                    split_count += 1
                    grid[i+1][j-1] = grid[i+1][j+1] = '|'
                else:
                    grid[i+1][j] = '|'
    for line in grid:
        print(line)
    print(split_count)