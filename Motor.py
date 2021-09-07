'''
Universidad del Valle de Guatemala
Graficas por computadora - Bryann Alfaro
Laboratorio 2 - Shaders
'''
from gl import Renderer, color
from textures import Texture
from Funciones.utilities import *


a = 3.14/2
pi = 3.14
r =  Renderer()
r.glInit()
r.glCreateWindow(800,600)
r.glClear()
t= Texture('./Texturas/model.bmp')
r.texture = t
r.load('./modelos/model.obj',(300,300,0),(200,200,200),(pi/8,pi/5,0))
r.draw_arrays('TRIANGLES')
r.glFinish("./salidas/clear.bmp")
