q=1
while q<1000:
    import random
    import time

    alist = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m',' ']
    blist = ['h','e','l','l','o',' ' ,'w','o','r','l','d']
    astr = ''

    x=0
    y=0

    f = open('val.txt','a+')

    while x<len(blist):
        y += 1
        p = random.randint(0,len(alist)-1)
        if(q==1):
            print(astr + ' - '+ alist[p])
        'time.sleep(2)'
        if alist[p] == blist[x]:
            astr = astr + alist[p]
            x += 1
            if(q==1):
                print(astr)

    f.write(str(y) + '\n')
    f.close()
    f = open('val.txt','r')
    clist = f.readlines()
    count = 0
    total = 0
    for i in clist:
        total += int(i)
        count += 1

    avg = total/count
    if(q==999):
        print(f'On average it takes {avg} tries to print hello world')
    q += 1


        
    
