# a = 100; b = 200; sum = 0
# a = 4573; b = 8995; sum = 0
a = 4863; b = 9006; sum = 0
# if((a < b) and (a < 1000) and (b < 1000)):
for i in range((a-1), (b+1)):
    if(i % 2 == 1):

        sum += i
    else: pass
# else: pass
print(sum)
