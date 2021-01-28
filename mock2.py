n = 2
flowerbed = [1,0,0,0,0,1]
count = n
if flowerbed[0] == 0:
    for i in range(0,len(flowerbed)):
        if i % 2 == 0:
            flowerbed[i] == 0
        else:
            flowerbed[i] == 1
elif flowerbed[0] == 1:
    for i in range(0,len(flowerbed)):
        if i % 2 == 0:
            flowerbed[i] == 1
        else:
            flowerbed[i] == 0

