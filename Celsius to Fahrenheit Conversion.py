def main():
    TempStr = input("Please enter the temperature value (C/F) with sign: ")
    if TempStr[-1] in ['F', 'f']:
        C = (eval(TempStr[0: -1]) - 32)/1.8
        print("The converted temperature is: {:.2f}C".format(C))
    elif TempStr[-1] in ['C', 'c']:
        F = 1.8*eval(TempStr[0:-1]) + 32
        print("The converted temperature is: {:.2f}F".format(F))
    else:
        print("wrong input format")

if __name__ == '__main__':
    main()