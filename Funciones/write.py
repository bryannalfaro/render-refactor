from Funciones.characters import *
from Funciones.utilities import *

def glFinish(self, filename):
        #bw means binary write
        f = open(filename, 'bw')
        #file header
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14+40+ 3*(self.width*self.height)))
        f.write(dword(0))
        f.write(dword(14+40))

        #info header
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(3*(self.width*self.height)))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))

        #bitmap
        for y in range(self.height):
            for x in range(self.width):
                f.write(self.framebuffer[y][x].toBytes())

        f.close()

def glFinish_ZBUFFER(self, filename):
    #bw means binary write
    f = open(filename, 'bw')
    #file header
    f.write(char('B'))
    f.write(char('M'))
    f.write(dword(14+40+ 3*(self.width*self.height)))
    f.write(dword(0))
    f.write(dword(14+40))

    #info header
    f.write(dword(40))
    f.write(dword(self.width))
    f.write(dword(self.height))
    f.write(word(1))
    f.write(word(24))
    f.write(dword(0))
    f.write(dword(3*(self.width*self.height)))
    f.write(dword(0))
    f.write(dword(0))
    f.write(dword(0))
    f.write(dword(0))

    z_min = float('inf')
    z_max = -float('inf')

    for x in range(self.height):
        for y in range(self.width):
            if self.zbuffer[x][y] != -float('inf'):
                if self.zbuffer[x][y] > z_max:
                    z_max = self.zbuffer[x][y]

                if self.zbuffer[x][y] < z_min:
                    z_min = self.zbuffer[x][y]

    for x in range(self.height):
        for y in range(self.width):
            z_value = self.zbuffer[x][y]

            if z_value == -float('inf'):
                z_value = z_min

            z_value = round(((z_value - z_min) / (z_max - z_min)) * 255)

            z_color = color(z_value, z_value, z_value)
            f.write(z_color)

    f.close()