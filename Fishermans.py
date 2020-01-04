second = 100000000000000000000
for i in range(0,second,6):

    if (i%5 == 0 and i>0):
        if(i%4 == 0):
            if(i%3 == 0):
                if(i%2 == 0):
                    print(i)
                    break
