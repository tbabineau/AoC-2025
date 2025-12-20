if __name__ == "__main__":
    fname = "input.txt"
    #fname = "test.txt"
    file = open(fname)
    grid = []
    for line in file:
        row = []
        for char in line:
            if(char != '\n'):
                row.append(char)
        grid.append(row)
    
    rows = len(grid)
    cols = len(grid[0])
    num_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows-1): #Filling out the grid, like in part one
        for j in range(cols):
            if(grid[i][j] == 'S'):
                grid[i+1][j] = '|'
                num_grid[i+1][j] = 1
            elif(grid[i][j] == '|'):
                if(grid[i+1][j] == '^'):
                    grid[i+1][j-1] = grid[i+1][j+1] = '|'
                    num_grid[i+1][j-1] = num_grid[i+1][j+1] = 1
                else:
                    grid[i+1][j] = '|'
                    num_grid[i+1][j] = 1
    
    for i in range(rows-1, 0, -1):#Range goes from lower(inclusive) to upper (non-inclusive)
        for j in range(cols):
            if(grid[i][j] == '^'):
                num_grid[i][j] = num_grid[i-1][j] = num_grid[i][j-1] + num_grid[i][j+1]
                temp_row = i-1
                while(grid[temp_row][j] == '|'):
                    num_grid[temp_row][j] = num_grid[temp_row+1][j] #Send the change up the line
                    temp_row -= 1
                if(grid[temp_row][j] == 'S'):
                    print(num_grid[temp_row+1][j])


    
    