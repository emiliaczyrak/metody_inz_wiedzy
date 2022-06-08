import random as rand

def montecarlo(foo,foo2, fx, lx, eps):
    oryginal = foo2(lx)-foo2(fx)
    wyliczone = 0
    punkty = 1000
    ile = 0
    minimum, maximum = foo(fx), foo(lx)
    wylosowane=[]
    ile=0
    while(abs(wyliczone-oryginal)>eps):
        punkty+=1000
        for i in range(1000):
            newx = rand.uniform(fx,lx)
            newy = rand.uniform(minimum, maximum)
            while((newx,newy) in wylosowane):
                newx = rand.uniform(fx,lx)
                newy = rand.uniform(minimum, maximum)
            wylosowane.append((newx,newy))
            
            wynik = foo(newx)
            if(newy<=wynik):
                ile+=1
        wyliczone = (lx-fx)*(maximum-minimum)*(ile/punkty)
        print("dokladnosc: {3} ilosc {0} pkt:{1} rzeczywiste {2}".format(punkty,wyliczone,oryginal,eps))
    return wyliczone

def f2(x):
    return x**2/2

def f(x):
    return x

def prostokaty(foo,foo2, fx, lx, eps):
    oryginal = foo2(lx)-foo2(fx)
    wyliczone = 0
    dzielnik = 1
    odleglosc = 1
    while(abs(wyliczone-oryginal)>eps):
        wyliczone = 0
        dzielnik*=2
        odleglosc = float(lx-fx)/float(dzielnik)
        for i in range(dzielnik):
            wyliczone+= foo(fx+odleglosc*i)*odleglosc
        print("dokladnosc: {3} ilosc {0} pkt:{1} rzeczywiste {2}".format(dzielnik,wyliczone,oryginal,eps))
    return wyliczone

def prostokaty2(foo,foo2, fx, lx, eps):
    oryginal = foo2(lx)-foo2(fx)
    wyliczone = 0
    dzielnik = 1
    odleglosc = 1
    while(abs(wyliczone-oryginal)>eps):
        wyliczone = 0
        dzielnik*=2
        odleglosc = float(lx-fx)/float(dzielnik)
        for i in range(1,dzielnik+1):
            wyliczone+= foo(fx+odleglosc*i)*odleglosc
        print("dokladnosc: {3} ilosc {0} pkt:{1} rzeczywiste {2}".format(dzielnik,wyliczone,oryginal,eps))
    return wyliczone

def prostokaty3(foo,foo2, fx, lx, eps):
    oryginal = foo2(lx)-foo2(fx)
    wyliczone = 0
    dolna = 0
    gorna = 0
    dzielnik = 1
    odleglosc = 1
    while(abs(wyliczone-oryginal)>eps):
        wyliczone = 0
        dzielnik*=2
        odleglosc = float(lx-fx)/float(dzielnik)
        for i in range(1,dzielnik+1):
            dolna = foo(fx+odleglosc*(i-1))*odleglosc
            gorna = foo(fx+odleglosc*i)*odleglosc
            wyliczone+= (dolna+gorna)/2
        print("dokladnosc: {3} ilosc {0} pkt:{1} rzeczywiste {2}".format(dzielnik,wyliczone,oryginal,eps))
    return wyliczone
           
print(prostokaty(f,f2, 0, 1, 0.01))
