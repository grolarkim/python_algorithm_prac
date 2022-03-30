a_list = [x for x in range(1,10000)]
b = [x for x in range(1,10000)]

for a in a_list:
    if a < 10:
        try:
            c=2*a
            b.remove(c)
        except:
            pass
    if a < 100:
        try:
            c = a + a//10 + a%10
            b.remove(c)
        except:
            pass
    if a < 1000:
        try:
            c = a + a//100 + (a//10)%10 + a%10
            b.remove(c)
        except:
            pass
    else:
        try:
            c = a + a//1000 + (a//100)%10 + (a//10)%10 + a%10
            b.remove(c)
        except:
            pass

for i in b:
    print(i)