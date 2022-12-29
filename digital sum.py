num = 0
m = int(input('Please input your final destination number:'))
n = int(input('Please input your Interval numbers:'))
for i in range(1, m + 1, n):
    num += i
print(num)