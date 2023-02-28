# In the following given program, the function of the fun function is:
# Count the number of uppercase and lowercase letters in a string separately.

def Upper(s):
    a = 0
    for i in range(len(s)):
        if ( s[i] >= 'A' and s[i] <= 'Z' ):
            a += 1
    return a

def Lower(s):
    b = 0
    for i in range(len(s)):
        if ( s[i] >= 'a' and s[i] <= 'z' ):
            b += 1
    return b

def main():
    s = input("Please enter a string:")
    upper = Upper(s)
    lower = Lower(s)
    print("Upper = ", format(upper))
    print("Lower = ", format(lower))

if __name__ == '__main__' :
    main()