if __name__ == "__main__":
    #fname = "test.txt"
    fname = "input.txt"
    invalids = 0
    file = open(fname)
    text = file.read() #Takes the line in as a string
    invalid = 0
    found = []
    for numbers in text.split(','):
        numbers = numbers.split('-')
        nums = [int(numbers[0]), int(numbers[1])]
        for i in range(nums[0], nums[1]+1):
            for j in range(len(str(i))):
                if(str(i).replace(str(i)[:j], "") == "" and i not in found):
                    invalid += i
                    found.append(i)
    print(invalid)
    print(found)
