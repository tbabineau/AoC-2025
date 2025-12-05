if __name__ == "__main__":
    #fname = "test.txt"
    fname = "input.txt"
    invalids = 0
    file = open(fname)
    text = file.read() #Takes the line in as a string
    found = []
    for numbers in text.split(','):
        numbers = numbers.split('-')
        count = 1
        while(count <= len(numbers[1])//2):
            low = len(numbers[0])
            high = len(numbers[1])
            nums = [int(numbers[0]), int(numbers[1])]
            curr = int("1" + "0"*(count-1))
            if(low % count != 0):
                low += count - low%count
            if(low == 1):
                low += 1
            while(len(str(curr)) == count):
                if(count == 1 or curr % int("1"*count) != 0):
                    for i in range(low//count, (high//count) + 1):
                        if(int(str(curr)*i) >= nums[0] and int(str(curr) * i) <= nums[1] and int(str(curr)*i) not in found):
                            invalids += int(str(curr) * i)
                            found.append(int(str(curr) * i))
                curr += 1
            count += 1
    print(invalids)