from Funciones.math import *

def normal(render,**kwargs):
        w,v,u = kwargs['bar']
        tx,ty = kwargs['tex_coords']
        nA,nB,nC = kwargs['varying_normals']
        A,B,C = kwargs['triangle']

        tcolor = render.texture.get_color(tx,ty)
        iA,iB,iC = [dot(n,render.light) for n in(nA,nB,nC)]
        intensity = w*iA+v*iB+u*iC

        txtNormal = norm(V3((intensity[2]*2-1),(intensity[1]*2-1),(intensity[0]*2-1)))
        e1 = sub(B,A)
        e2 = sub(C,A)

        changeUV1 = sub(V3())

        return tcolor*intensity