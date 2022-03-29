A="09.02.2022"
b=A
def Main(b):
    Change(b)

def Change(b):
    while b!='05.06.2022':
        while b[0]+b[1]!='31':
            while b[1]!='0':
                n=b[1]
                b = b[:1] + str(Counter_of_Idiot(n)) + b[1+1:]
                print(b)
                if b=='05.06.2022':
                    exit()
            n=b[0]
            b = b[:0] + str(Counter_of_Idiot(n)) + b[0+1:]
            print(b)
            b = b[:1] + str(1) + b[1+1:]
            print(b)
        n=b[4]
        b = b[:4] + str(Counter_of_Idiot(n)) + b[4+1:]
        b = b[:0] + str(0) + b[0+1:]
        print(b)

def Counter_of_Idiot(n):
    if int(n)!=9:
        n=str(int(n)+1) 
    else:
        n=0
    return n
Main(b)

