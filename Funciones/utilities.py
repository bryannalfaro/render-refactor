from Funciones.math import *
import random
class V3(object):
    def __init__(self, x, y, z=None):
        self.x = x
        self.y = y
        self.z = z
    def __getitem__(self,i):
        if i == 0:
            return self.x
        elif i == 1:
            return self.y
        elif i == 2:
            return self.z
    def __repr__(self):
        return 'V3(%s, %s, %s)' % (self.x,self.y,self.z)

def ccolor(color):
    return max(0,min(255,int(color)))

class color(object):
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __getitem__(self,i):
        if i == 0:
            return self.r
        elif i == 1:
            return self.g
        elif i == 2:
            return self.b

    def __repr__(self):
        b= ccolor(self.b)
        g= ccolor(self.g)
        r= ccolor(self.r)
        return 'Y(%s,%s,%s)' % (b,g,r)

    def toBytes(self):
        b= ccolor(self.b)
        g= ccolor(self.g)
        r= ccolor(self.r)
        return bytes([b,g,r])

    def __mul__(self,k):
        r= ccolor(self.r*k)
        g= ccolor(self.g*k)
        b= ccolor(self.b*k)

        return color(r,g,b)

    def tolist(self):
        return color(self.r,self.g,self.b)

BLACK = color(0,0,0)
WHITE = color(255,255,255)

def barycentric(A,B,C,P):
        cx,cy,cz = cross(V3(B.x-A.x,C.x-A.x,A.x-P.x),V3(B.y-A.y,C.y-A.y,A.y-P.y))
        if cz ==0:
            return -1,-1,-1

        u = cx/cz
        v = cy/cz
        w = 1-(cx+cy)/cz

        return w,v,u

def bbox(A,B,C):
    xs = [A.x, B.x, C.x,]
    xs.sort()
    ys = [A.y, B.y, C.y,]
    ys.sort()
    return round(xs[0]),round(xs[-1]),round(ys[0]),round(ys[-1])


def shader(self, x,y):
        centerx,centery = 500,353
        centerx2,centery2 = 478,360
        circle1 = (x-centerx)**2+(y-centery)**2
        circle2 = (x-centerx2)**2+(y-centery2)**2

        #Colors of the image
        palette = [(171,42,120),(8,4,6),(246,130,199),
        (111,17,76),(92,15,58),(225,76,167),(238,94,183),
        (206,90,155),(76,76,76)]

        if y >= 100 and y < 165:
            if x > (300) and x< (460+random.randint(0,10)):
                return palette[3][2],palette[3][1],palette[3][0]
            return palette[4][2],palette[4][1],palette[4][0]

        if y >= 165 and y < (185+random.randint(0,12)):
            if x > (300) and x< (460+random.randint(0,20)):
                return palette[3][2],palette[3][1],palette[3][0]
            else:
                return palette[4][2],palette[4][1],palette[4][0]

        if y >= (185+random.randint(0,12)) and y < (220+random.randint(0,12)):
            return palette[0][2],palette[0][1],palette[0][0]

        if y>=220 and y < (250+random.randint(0,12)):
            if y > 220 and y < 230:
                if x > 300 and x< (480+random.randint(0,18)):
                    return palette[6][2],palette[6][1],palette[6][0]
            if y > 230 and y < 235:
                if x > 300 and x< (460+random.randint(0,18)):
                    return palette[6][2],palette[6][1],palette[6][0]
                if x > 460 and x< (520+random.randint(0,18)):
                    return palette[2][2],palette[2][1],palette[2][0]
            if y >= (235+random.randint(0,18)) and y <=(245+random.randint(0,18)):
                if x > (420+random.randint(0,15)) and x< (520+random.randint(0,18)):
                    return palette[2][2],palette[2][1],palette[2][0]
            if y > 245 and y < 250:
                if x > 300 and x< (480+random.randint(0,18)):
                    return palette[6][2],palette[6][1],palette[6][0]
                if x > 460 and x< (520+random.randint(0,18)):
                    return palette[2][2],palette[2][1],palette[2][0]
            if x > 300 and x< (430+random.randint(0,12)):
                return palette[6][2],palette[6][1],palette[6][0]
            return palette[7][2],palette[7][1],palette[7][0]


        if y >= 250 and y < (270+random.randint(0,12)):
            return palette[5][2],palette[5][1],palette[5][0]

        if y>=270 and y < (280+random.randint(0,16)):
            if x > 300 and x< (480+random.randint(0,18)):
                return palette[6][2],palette[6][1],palette[6][0]
            else:
                return palette[5][2],palette[5][1],palette[5][0]

        if y>=280 and y < (310+random.randint(0,30)):
            return palette[5][2],palette[5][1],palette[5][0]

        if y >= 310 and y < (340+random.randint(0,10)):
            return palette[7][2],palette[7][1],palette[7][0]

        if y >= 340 and y < (375):
            return palette[0][2],palette[0][1],palette[0][0]

        if y >=(375) and y < (395+random.randint(0,12)):
            if circle1 < 40**2:
                return palette[0][2],palette[0][1],palette[0][0]
            if circle2 < 30**2:

                return palette[0][2],palette[0][1],palette[0][0]
            if y > 375 and y <382:
                if x > (390+random.randint(0,15)) and x < (450+random.randint(0,14)):
                    return palette[2][2],palette[2][1],palette[2][0]
                if x > (480+random.randint(0,15)) and x < (580+random.randint(0,14)):
                    return palette[2][2],palette[2][1],palette[2][0]
            if y > 380 and y<395:

                if x > 300 and x < (430+random.randint(0,50)):
                    return palette[6][2],palette[6][1],palette[6][0]
            if x > 300 and x < (430+random.randint(0,15)):
                return palette[6][2],palette[6][1],palette[6][0]
            return palette[7][2],palette[7][1],palette[7][0]

        if y>=(395) and y < (410+random.randint(0,12)):
            return palette[5][2],palette[5][1],palette[5][0]

        if y >= 410 and y <(430+random.randint(0,4)):
            return palette[0][2],palette[0][1],palette[0][0]

        else:
            return palette[3][2],palette[3][1],palette[3][0]