def aniBisecti(x,y):
    for i in range(x+1,y):
        if i %4==0 and i%100!=0 or i%400==0:
            print (i)

def meniu():
    print("1.Afiseaza toti anii bisecti intre anul x si anul y")
    print("0. Iesire")

def interfata():
    x = int(input("Dati x:"))
    y = int(input("Dati y:"))
    meniu()

    while True:
        op=int(input("Optiunea e:"))
        if op==1:
            print("Anii bisecti sunt:")
            aniBisecti(x,y)
        elif op==0:
            break
        else:
            print("invalid")
interfata()

