if __name__ == "__main__":
    #fname = "test.txt"
    fname = "input.txt"
    invalids = 0
    file = open(fname)
    text = file.read() #Takes the line in as a string
    for numbers in text.split(','):
        numbers = numbers.split('-')
        low = len(numbers[0])
        high = len(numbers[1])
        nums = [int(numbers[0]), int(numbers[1])]
        #Since it's two groups of numbers, if the range is odd then it must be valid
        if(not(low == high and low % 2 != 0)):
            curr = 0
            mult = 0
            if(low % 2 == 0): #If even
                mult = 10**(low//2)
                curr = (nums[0] - (nums[0] % (mult)))//(mult) #Sets curr to the first half of the digits
                if(curr < nums[0] % (mult)): #If curr is outside the range
                    curr += 1
            else:
                low += 1
                mult = 10**((low)//2)
                curr = 1 * (10**(((low)//2)-1))

            while(curr*mult + curr <= nums[1]): 
                invalids += curr*mult + curr
                curr += 1
                if(len(str(curr)) > low//2):
                    low += 2
                    mult = 10**((low)//2)
                    curr = 1 * (10**(((low)//2)-1))

    print(invalids)
            