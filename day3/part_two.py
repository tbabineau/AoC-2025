if __name__ == "__main__":
    #voltage ranges from 1 to 9
    fname = "input.txt"
    #fname = "test.txt"
    file = open(fname)
    tot_volts = 0
    for bank in file:
        bank = bank.strip() #removes trailing whitespace
        biggest = [0 for _ in range(12)]
        for i in range(len(bank)):
            temp = len(bank) - i - 1
            offset = 0
            if(temp < 11):
                offset = 11 - temp
            for j in range(offset, 12):
                if(int(bank[i]) > biggest[j]):
                    biggest[j] = int(bank[i])
                    for k in range(j+1, 12):
                        biggest[k] = 0
                    break

        count = 1
        for i in range(11, -1, -1):
            tot_volts += biggest[i] * count
            count *= 10 

    print(tot_volts)