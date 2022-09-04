import random
import math
import matplotlib.pyplot as plt

xf = random.randint(0, 999)
yf = random.randint(0, 999)

xb = random.randint(0, 999)
yb = random.randint(0, 999)

vf = 20
t = 0
# vb = 15
thresold = 100
flag = False

point1 = []
point2 = []

while(not flag or t>999):
    dist = math.sqrt((xb-xf)**2+(yb-yf)**2) 
    if(dist<100 or dist >999):
        if(dist<100):
            print(f'Fighter positoin {point1}')
            print(f'Bomber position {point2}')
            print(f'At {t}s')
            print('Cought')
        elif(dist>999):
            print(point1)
            print(point2)
            print('Scaped')

        flag = True
        break
    else:
        fsin = (yb-yf)/dist
        fcos = (xb-xf)/dist
        t =t+1
        xf = xf + vf*fcos
        yf = yf + vf*fsin


        xb = random.randint(0, 999)
        yb = random.randint(0, 999)

        # bsin = (yb-yf)/dist
        # bcos = (xb-yf)/dist
        # xb = xb + vb*bcos
        # yb = xb + vb*bsin


        

    point1.append([xf, yf])
    point2.append([xb, yb])
    


    plt.scatter(point1,point2)
    
    
    plt.pause(0.1)
    plt.title('Pure Pursuit')
    plt.xlabel('x-value')
    plt.ylabel('y-value')
    

plt.show()


    
        



