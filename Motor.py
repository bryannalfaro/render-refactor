'''
Universidad del Valle de Guatemala
Graficas por computadora - Bryann Alfaro
Laboratorio 2 - Shaders
'''
from gl import Renderer, color
from textures import Texture


r =  Renderer()
r.glInit()
r.glCreateWindow(800,600)
r.glClear()
t= Texture('./Texturas/model.bmp')
r.texture = t
r.load('./modelos/model.obj',(1,1,1),(300,300,300))
r.draw_arrays('TRIANGLES')
r.glFinish("./salidas/clear.bmp")
