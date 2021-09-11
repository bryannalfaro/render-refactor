from Funciones.math import *
from Funciones.utilities import *
def gourad(render,**kwargs):
        w,v,u = kwargs['bar']
        tx,ty = kwargs['tex_coords']
        nA,nB,nC = kwargs['varying_normals']

        tcolor = render.texture.get_color(tx,ty)
        iA,iB,iC = [dot(n,render.light) for n in(nA,nB,nC)]
        intensity = w*iA+v*iB+u*iC
        return tcolor*intensity

def custom(render,**kwargs):
        w,v,u = kwargs['bar']
        tx,ty = kwargs['tex_coords']
        nA,nB,nC = kwargs['varying_normals']

        tcolor = render.texture.get_color(tx,ty)
        iA,iB,iC = [dot(n,render.light) for n in(nA,nB,nC)]
        intensity = w*iA+v*iB+u*iC
        return tcolor*intensity*2

def unlit(render,**kwargs):
        tx,ty = kwargs['tex_coords']

        tcolor = render.texture.get_color(tx,ty)

        return tcolor