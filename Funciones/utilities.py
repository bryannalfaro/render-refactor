from Funciones.math import *

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
    return xs[0],xs[-1],ys[0],ys[-1]