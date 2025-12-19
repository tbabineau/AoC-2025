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
            changed = False
            i = 0
            while(i+1 < len(ranges)):
                if(ranges[i][1] >= ranges[i+1][0]):
                    ranges[i][0] = min(ranges[i][0], ranges[i+1][0])
                    ranges[i][1] = max(ranges[i+1][1], ranges[i][1])
                    ranges.pop(i+1)
                else:
                    i += 1
            for i in range(len(ranges) - 1):
                if(ranges[i][0] == ranges[i+1][0]):
                    print("FLAG")
            for nums in ranges:
                count += nums[1] - nums[0] + 1
            print(count)
        elif(not done): #Collect ranges
            line = line.split("-")
            nums = [int(line[0]), int(line[1])]
            placed = False
            for i in range(len(ranges)):
                if(nums[0] <= ranges[i][0]):
                    ranges.insert(i, [nums[0], nums[1]])
                    placed = True
                    break
            if(not placed):
                ranges.append([nums[0], nums[1]])
        else:
            break #Don't need that input