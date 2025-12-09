if __name__ == "__main__":
    #voltage ranges from 1 to 9
    fname = "input.txt"
    #fname = "test.txt"
    file = open(fname)
    tot_volts = 0
    for bank in file:
        bank = bank.strip() #removes trailing whitespace
        biggest = [0, 0]
        for i in range(len(bank)):
            if(int(bank[i]) > biggest[1]):
                biggest[1] = int(bank[i])
                if(biggest[1] > biggest[0] and i != len(bank) - 1):
                    biggest[0] = biggest[1]
                    biggest[1] = 0
        tot_volts += biggest[0] * 10 + biggest[1] 
    print(tot_volts)