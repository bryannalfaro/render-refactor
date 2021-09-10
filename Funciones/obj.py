
class Obj(object):
    def __init__(self, filename):
        with open(filename) as f:
            self.lines = f.read().splitlines()

        self.vertices = []
        self.faces = []
        self.tvertices = []
        self.nvertices = []
        self.read()

    def read(self):
        for line in self.lines:
            if len(line)>2:
                if line.split(' ',1):
                    prefix, value = line.split(' ',1)
                    if prefix == 'v':
                        self.vertices.append(list(map(float,value.lstrip().split(' '))))
                    if prefix == 'vt':

                        self.tvertices.append(list(map(float,value.lstrip().split(' '))))
                    if prefix == 'vn':

                        self.nvertices.append(list(map(float,value.lstrip().split(' '))))
                    elif prefix == 'f':

                        self.faces.append([list(map(int,face.lstrip().split('/'))) for face in value.rstrip().split(' ')])


