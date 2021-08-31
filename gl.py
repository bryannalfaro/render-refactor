from obj import Obj
from Funciones.characters import *
from Funciones.math import *
from Funciones.utilities import *
from Funciones.write import *
import random

class Renderer(object):
    def __init__(self):
        self.default_color = color(0,0,139)
        self.cl_color = BLACK
        self.texture = None
        self.light =norm(V3(0,0,1))

    def point(self, x, y):
        self.framebuffer[y][x] =self.default_color

    def glInit(self):
        pass

    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height
        self.framebuffer = []

    def glViewPort(self, x, y, width, height):
        self.vp_x = x
        self.vp_y = y
        self.vp_width = width
        self.vp_height = height

    #Fill the bitmap
    def glClear(self):
        self.framebuffer = [
            [self.cl_color for x in range(self.width)] for y in range(self.height)
            ]
        self.zbuffer = [
            [-float('inf') for x in range(self.width)] for y in range(self.height)
            ]

    def frame(self):
        return self.framebuffer

    def glClearColor(self, r,g,b):
        if(r<=1 and g<=1 and b<=1):
            self.cl_color = color(int(r*255),int(g*255),int(b*255))
        else:
            self.cl_color = color(r,g,b)

        self.glClear()
    def backcolor(self, r,g,b):
        if(r<=1 and g<=1 and b<=1):
            self.cl_color = color(int(r*255),int(g*255),int(b*255))
        else:
            self.cl_color = color(r,g,b)

        return self.cl_color

    def customBackground(self):

        setr = [ BLACK,BLACK,BLACK, WHITE,BLACK,BLACK,BLACK,BLACK
        ,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK
        ,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK
        ,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK
        ,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK
        ,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK]


        self.framebuffer = [
            [self.backcolor(*random.choice(setr)) for x in range(self.width)] for y in range(self.height)
            ]

    def glVertex(self,x,y):
        #formula get from microsoft glViewport function
        x_pos = int((x+1)*(self.vp_width/2)+self.vp_x)
        y_pos = int((y+1)*(self.vp_height/2)+self.vp_y)
        self.point(x_pos,y_pos)

    #change color of vertex
    def glColor(self, r,g,b):
        try:
            self.default_color = color(r,g,b)
        except:
            self.default_color = color(int(r*255),int(g*255),int(b*255))

    #Using class implementation
    #REESCRIBIR
    def glLine(self,x0,y0,x1,y1):

        x0 = int((x0+1)*(self.vp_width/2)+self.vp_x)
        y0 = int((y0+1)*(self.vp_height/2)+self.vp_y)
        x1 = int((x1+1)*(self.vp_width/2)+self.vp_x)
        y1 = int((y1+1)*(self.vp_height/2)+self.vp_y)


        self.line(x0,y0,x1,y1)

    def line(self,A,B):
        x0 = A.x
        y0 = A.y
        x1 = B.x
        y1 = B.y

        dy = abs(y1-y0)
        dx = abs(x1-x0)

        steep = dy>dx
        #en caso de pendiente mayor a 1
        if steep:
            x0,y0 = y0,x0
            x1,y1 = y1,x1

            dy = abs(y1-y0)
            dx = abs(x1-x0)

        #en caso que el segundo valor sea menor que el primero
        if x1<x0:
            x0,x1 =x1,x0
            y0,y1 = y1,y0

            dy = abs(y1-y0)
            dx = abs(x1-x0)

        offset = 0 *2*dx
        threshold = 0.5 *2*dx
        y = y0

        points = []
        for x in range(x0,x1+1):
            if steep:
                points.append((y,x))

            else:
                points.append((x,y))

            offset += dy*2
            if offset >= threshold:

                y +=1 if y0<y1 else -1
                threshold +=1 *2* dx

            for pointf in points:
                self.point(*pointf)


    def load(self, filename, movement, scale):
        model = Obj(filename)

        vertex_buffer_object = []
        for face in (model.faces):
            for v in range(len(face)):
                vertex = transform(V3(*model.vertices[face[v][0]-1]), movement,scale)
                vertex_buffer_object.append(vertex)
            if self.texture:
                for v in range(len(face)):
                    tvertex =(V3(*model.tvertices[face[v][1]-1]))
                    vertex_buffer_object.append(tvertex)

        self.active_vertex_array = iter(vertex_buffer_object)

    def draw_arrays(self,polygon):
        self.polygon = polygon
        if polygon == 'WIREFRAME':
            pass
        elif polygon == 'TRIANGLES':
            try:
                while True:
                    self.triangle()
            except StopIteration:
                print('Done')
        elif polygon == 'SQUARE':
            try:
                while True:
                    self.square()
            except StopIteration:
                print('Done')

    def fill(self):
        bandera = False
        arreglo = []
        x0,y0 = 0,0
        x1,y1 = 0,0

        for i in range(len(self.frame())): #filas

            for j in range(len(self.frame())): #cada valor fila
                #color diferente al bitmap
                if((self.cl_color[2],self.cl_color[1],self.cl_color[0]) != (self.frame()[i][j][2],self.frame()[i][j][1],self.frame()[i][j][0]) ):
                    a=self.frame()[i][j][2],self.frame()[i][j][1],self.frame()[i][j][0]

                    arreglo.append([1,a]) #evaluar cada valor con su color si son diferentes
                else:
                     a=self.frame()[i][j][2],self.frame()[i][j][1],self.frame()[i][j][0]
                     arreglo.append([0,a])
            #por cada linea
            for pos in range(len(arreglo)):
                if arreglo[pos][0] == 1:
                    if(bandera):
                            if(arreglo[pos][1]!=a):
                                a = arreglo[pos][1]
                                x0,y0 = pos,i

                            else:
                                    x1,y1 = pos,i
                                    self.glColor(a[0]/255,a[1]/255,a[2]/255)
                                    self.line(x0,y0,x1,y1)
                    else:
                        a = arreglo[pos][1]
                        x0,y0 = pos,i
                else:
                    if(x0!=0):
                        bandera = True
                    else:
                            bandera = False
            arreglo = []
            bandera = False
            x0,y0 = 0,0
            x1,y1 = 0,0

    def triangle_wireframe(self,A,B,C):
        self.line(A,B)
        self.line(B,C)
        self.line(C,A)

    def square(self):
            A = next(self.active_vertex_array)
            B = next(self.active_vertex_array)
            C = next(self.active_vertex_array)
            D = next(self.active_vertex_array)

            if self.texture:
                tA = next(self.active_vertex_array)
                tB = next(self.active_vertex_array)
                tC = next(self.active_vertex_array)
                tD = next(self.active_vertex_array)

            for i in range(0,2):
                if i != 0:
                    B = C
                    C  = D
                    self.squareDraw(A,B,C,tA,tB,tC)
                else:
                    self.squareDraw(A,B,C,tA,tB,tC)

    def squareDraw(self,A,B,C,tA,tB,tC):
            xmin,xmax,ymin,ymax = bbox(A,B,C)
            normal = norm(cross(sub(B,A),sub(C,A)))
            intensity = dot(normal, self.light)
            col = None

            for x in range(xmin,xmax+1):
                for y in range(ymin,ymax+1):
                    P = V3(x,y)
                    w,v,u = barycentric(A,B,C,P)
                    if w<0 or v<0 or u<0:
                        continue

                    if self.texture:
                        tx = tA.x*w+tB.x*v+tC.x*u
                        ty = tA.y*w+tB.y*v+tC.y*u
                        fcolor = self.texture.get_color(tx,ty)
                        b,g,r = [round(c*intensity) if intensity>0 else 0 for c in fcolor]

                        col = color(r,g,b)

                    z = A.z * w+B.z*v+C.z*u
                    col = WHITE * intensity

                    try:
                        if z> self.zbuffer[y][x]:
                            if col==None:

                                self.point(x,y)
                                self.zbuffer[y][x] =z
                            else:

                                self.default_color = col
                                self.point(x,y)
                                self.zbuffer[y][x] =z
                    except:
                        pass
    def triangle(self):

            A = next(self.active_vertex_array)
            B = next(self.active_vertex_array)
            C = next(self.active_vertex_array)

            if self.texture:
                tA = next(self.active_vertex_array)
                tB = next(self.active_vertex_array)
                tC = next(self.active_vertex_array)

            xmin,xmax,ymin,ymax = bbox(A,B,C)
            normal = norm(cross(sub(B,A),sub(C,A)))
            intensity = dot(normal, self.light)
            col = None

            for x in range(xmin,xmax+1):
                for y in range(ymin,ymax+1):
                    P = V3(x,y)
                    w,v,u = barycentric(A,B,C,P)
                    if w<0 or v<0 or u<0:
                        continue

                    if self.texture:
                        tx = tA.x*w+tB.x*v+tC.x*u
                        ty = tA.y*w+tB.y*v+tC.y*u
                        fcolor = self.texture.get_color(tx,ty)

                        col = fcolor * intensity
                    else:
                        col = WHITE * intensity

                    z = A.z * w+B.z*v+C.z*u


                    try:
                        if z> self.zbuffer[y][x]:
                            if col==None:

                                self.point(x,y)
                                self.zbuffer[y][x] =z
                            else:

                                self.default_color = col
                                self.point(x,y)
                                self.zbuffer[y][x] =z
                    except:
                        pass



