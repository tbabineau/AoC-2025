if __name__ == "__main__":
    fname = "input.txt."
    #fname = "test.txt"
    file = open(fname)
    grid = []
    total = 0
    for line in file:
        temp = []
        for char in line.strip():
            temp.append(char)
        grid.append(temp)
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if(grid[col][row] == '@'):
                count = 0
                if(col != 0): #left side
                    if(grid[col-1][row] == '@'):#W
                        count += 1
                    if(row != 0 and grid[col-1][row-1] == '@'):#NW
                        count += 1
                    if(row != len(grid) -1 and grid[col-1][row+1] == '@'):#SW
                        count += 1 
                if(col != len(grid[0]) - 1):#right side
                    if(grid[col+1][row] == '@'):#E
                        count += 1
                    if(row != 0 and grid[col+1][row-1] == '@'):#NE
                        count += 1
                    if(row != len(grid) - 1 and grid[col+1][row+1] == '@'):#SE
                        count += 1 
                if(row != 0 and grid[col][row-1] == '@'):#N
                        count += 1
                if(row != len(grid) - 1 and grid[col][row+1] == '@'):#S
                    count += 1
                total += (count < 4)
    print(total)