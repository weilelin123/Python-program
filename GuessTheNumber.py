import random

num = random.randint(0, 100)
# num = 20

a = 0
b = 100

for i in range(1, 4):
    I_num = int(input("Please type in a integer between（{}-{}): ".format(a, b)))
    if I_num == num:
        print("Your are right! The right answer is: {}. You guess {} times".format(I_num, i))
        break
    elif I_num > num:
        b = I_num
        print("This is your {} guess, need to guess smaller".format(i))
    elif I_num < num:
        a = I_num
        print("This is your {} guess, need to guess bigger".format(i))
else:
    print("Times up! The program is end. The right answer is: {}".format(num))
