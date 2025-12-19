if __name__ == "__main__":
    fname = "input.txt"
    #fname = "test.txt"
    file = open(fname)
    done = False
    ranges = []
    spoiled = []
    count = 0
    for line in file:
        line = line.strip()
        if(line == ""): #Ranges are done being given
           done = True
           print("Done collecting ranges")
        elif(not done): #Collect ranges
            line = line.split("-")
            ranges.append((int(line[0]), int(line[1])))
            

        else:
            placed = False
            num = int(line)
            for (low, high) in ranges:
                if(not placed):
                    if(low <= num and num <= high):
                        placed = True
                        count += 1
    print(count)
