#假设大鸡5元一只，中鸡3元一只，小鸡1元三只，现在有一百元钱想买一百只鸡，有多少种买法？

daji = []
zhongji = []
xiaoji= []

# x 代大鸡，如果只买大鸡，那大鸡最多20只。
for x in range(21):

    #y 代表中鸡，如果只买中鸡，那中鸡最多33只。
    for y in range(34):
        z = 100 - x - y #z代表小鸡，小鸡=100-大鸡 - 中鸡

        #小鸡的数量要能被3整除，三种鸡的数量是100
        if z % 3 == 0 and 5 * x + 3 * y + z // 3 == 100:
            daji.append(x)
            zhongji.append(y)
            xiaoji.append(z)
print(f'总的买法有{len(daji)}种!!\n它们分别是：')
for i in range(len(daji)):
    print("大鸡是{}只，中鸡是{}只，小鸡是{}只".format(daji[i],zhongji[i],xiaoji[i]))