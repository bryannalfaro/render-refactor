'''
Universidad del Valle de Guatemala
Graficas por computadora - Bryann Alfaro
Proyecto 1 - Software Rendering.

Puntos implementados:
10 puntos por cada modelo que se cargue y renderize. Máximo de 5 modelos
5 puntos por cada shader distinto que se aplique a un modelo. Máximo 5 shaders (Se implementaron 3)
0 - 20 puntos según la complejidad del modelo más complejo (20 es muy complejo, algo cómo un personaje, 0 es algo como un cubo o una pirámide)
0 - 20 puntos según la estética de la escena (20 es una escena que se mira muy bien y no deja espacios en negro, 0 es un cubo en un fondo negro)
'''
from gl import Renderer
from Funciones.textures import Texture
from Funciones.utilities import *
from Funciones.shaders import *
pi = 3.14

r =  Renderer()
r.glInit()
r.glCreateWindow(640,300)
bg = Texture('./Texturas/parg.bmp')
r.framebuffer = bg.pixels
r.lookAt(V3(-0.3,0,5),V3(0,0.4,-1),V3(0,1,0))


#TRUMP MODEL WITH GOURAD SHADER
r.active_shader = gourad

t= Texture('./Texturas/trump.bmp')
r.texture = t
r.load('./newModels/trump.obj',(0.02,0.2,0.8),(0.2,0.2,0.2),(0,0,0))
r.draw_arrays('TRIANGLES')

#HORSE MODEL WITH CUSTOM SHADER
r.active_shader = custom
t = Texture('./Texturas/Horse_v01.bmp')
r.texture = t
r.load('./newModels/horse1.obj',(0,0,0.7),(0.0003,0.0003,0.0003),(-pi/2,2*pi,2*pi))
r.draw_arrays('SQUARE')

#DOG MODEL WITH CUSTOM SHADER
t = Texture('./Texturas/doff.bmp')
r.texture = t
r.load('./newModels/dog11.obj',(0.3,0,0.7),(0.005,0.005,0.005),(-pi/2,2*pi,-pi/2))
r.draw_arrays('SQUARE')

#WINE MODEL WITH UNLIT SHADER
r.active_shader = unlit
t = Texture('./Texturas/wine.bmp')
r.texture = t
r.load('./newModels/wine.obj',(0.2,0.4,0.5),(0.004,0.004,0.009),(pi/2,pi,pi))
r.draw_arrays('SQUARE')

#WOLF MODEL WITH CUSTOM SHADER
r.active_shader = custom
t = Texture('./Texturas/textureWolf.bmp')
r.texture = t
r.load('./newModels/wolf.obj',(-0.7,0,0),(0.003,0.003,0.003),(0,pi/4,0))
r.draw_arrays('TRIANGLES')

r.glFinish("./salidas/proyecto.bmp")

