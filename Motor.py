'''
Universidad del Valle de Guatemala
Graficas por computadora - Bryann Alfaro

#TODO
#Ver dibujado correcto de escena y de modelo
#Organizar
'''
from gl import Renderer
from Funciones.textures import Texture
from Funciones.utilities import *
from Funciones.shaders import *


a = 3.14/2
pi = 3.14
r =  Renderer()
r.glInit()
r.glCreateWindow(640,300)
bg = Texture('./Texturas/parg.bmp')
r.framebuffer = bg.pixels


#t= Texture('./Texturas/model.bmp')
#r.texture = t
r.lookAt(V3(0,0,5),V3(0,0,0),V3(0,1,0))
#r.load('./modelos/model.obj',(0,0,0),(1,1,1),(0,0,0))
r.active_shader = gourad
#r.draw_arrays('TRIANGLES')

t= Texture('./Texturas/trump.bmp')
r.texture = t
r.load('./newModels/trump.obj',(0,0,0),(0.4,0.4,0.4),(0,0,0))
r.draw_arrays('TRIANGLES')

t = Texture('./Texturas/wine.bmp')
r.texture = t
r.load('./newModels/wine.obj',(0,0,0),(0.009,0.03,0.03),(pi/2,pi,pi))
r.draw_arrays('SQUARE')

'''t= Texture('./Texturas/Omnitrix.bmp')
r.texture = t
r.load('./newModels/ovni.obj',(0,0,0),(0.04,0.04,0.04),(0,pi/8,0))
r.draw_arrays('TRIANGLES')


t = Texture('./Texturas/Horse_v01.bmp')
r.texture = t
r.load('./newModels/horse1.obj',(0,0,0),(0.0002,0.0002,0.0002),(0,0,pi/8))
r.draw_arrays('SQUARE')

t = Texture('./Texturas/doff.bmp')
r.texture = t
r.load('./newModels/dog11.obj',(0.2,0,0),(0.005,0.005,0.005),(0,0,0))
r.draw_arrays('SQUARE')

t = Texture('./Texturas/wine.bmp')
r.texture = t
r.load('./newModels/wine.obj',(0,0,0),(0.009,0.03,0.03),(pi/2,pi,pi))
r.draw_arrays('SQUARE')

t = Texture('./Texturas/textureWolf.bmp')
r.texture = t
r.load('./newModels/wolf.obj',(0,0,0),(0.006,0.006,0.006),(0,0,0))
r.draw_arrays('TRIANGLES')'''
r.glFinish("./salidas/clear.bmp")

