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
        temp = int(line[1:])
        count += (temp - temp%100)/100
        prev = curr
        curr = (curr + (temp * sign)) % 100
        if(curr == 0):
            count += 1
        elif(prev != 0 and((sign < 0 and curr > prev) or (sign > 0 and curr < prev))):
            count += 1
        print(temp, count)
    print(count)