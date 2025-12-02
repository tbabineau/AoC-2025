if __name__ == "__main__":
    curr = 50 #Dial starts on 50
    count = 0
    #fname = "test.txt"
    fname = "input.txt"
    file = open(fname)
    for line in file:
        line = line.strip() #Removes trailing whitespace in the line
        sign = 1
        if(line[0] == 'L'):
            sign = -1
        curr = (curr + int(line[1:]) * sign) % 100 #Keeps the numbers between 0 and 99
        if(curr == 0):
            count += 1
    print(count)
