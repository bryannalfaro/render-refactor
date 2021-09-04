from numpy import sin,cos,matrix
from gl import *
from Funciones.utilities import *
from Funciones.math import Matrix

r =  Renderer()
r.glInit()
r.glCreateWindow(1000,1000)
r.glClear()


def line(A,B):
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

                r.point(pointf[1],pointf[0])

points = [
  [200.0, 200.0],
  [400.0, 200.0],
  [400.0, 400.0],
  [200.0, 400.0]
]

center = V3(300, 300)

a = 3.14 / 4


move_to_origin = Matrix([
  [1, 0, -center.x],
  [0, 1, -center.y],
  [0, 0, 1]
])


rotation_matrix = Matrix([
  [cos(a), -sin(a), 0],
  [sin(a), cos(a), 0],
  [0, 0, 1]
])

identity_matrix = Matrix([
  [1, 0, 0],
  [0, 1, 0],
  [0, 0, 1]
])

scale_matrix = Matrix([
  [1.5, 0, 0],
  [0, 1.5, 0],
  [0, 0, 1]
])

move_back = Matrix([
  [1, 0, center.x],
  [0, 1, center.y],
  [0, 0, 1]
])

move_to_origin2 = matrix([
  [1, 0, -center.x],
  [0, 1, -center.y],
  [0, 0, 1]
])


rotation_matrix2 = matrix([
  [cos(a), -sin(a), 0],
  [sin(a), cos(a), 0],
  [0, 0, 1]
])

identity_matrix2 = matrix([
  [1, 0, 0],
  [0, 1, 0],
  [0, 0, 1]
])

scale_matrix2 = matrix([
  [1.5, 0, 0],
  [0, 1.5, 0],
  [0, 0, 1]
])

move_back2 = matrix([
  [1, 0, center.x],
  [0, 1, center.y],
  [0, 0, 1]
])

transform_matrix = move_back * scale_matrix * rotation_matrix * move_to_origin
transform_matrix2 = move_back2 * scale_matrix2 * rotation_matrix2 * move_to_origin2


print(transform_matrix)
print(transform_matrix2)
transformed_points = []

for point in points:
  point = V3(*point)
  tpoint = transform_matrix * Matrix([ [point.x], [point.y], [1]])
  tpoint2 = transform_matrix2 @ [ point.x, point.y, 1]
  print('t',tpoint)
  print('correcta',tpoint2)
  tpoint = tpoint.tolist()
  tpoint2 = tpoint2.tolist()[0]
  print('t3',tpoint)
  print('correcta',tpoint2)
  tpoint2D = V3(
    int(tpoint[0][0]/tpoint[2][0]),
    int(tpoint[1][0]/tpoint[2][0])
  )

  transformed_points.append(tpoint2D)



point = transformed_points[-1]
prev_point = V3(point[0], point[1])
for point in transformed_points:
  r.glColor(234,200,233)
  line(prev_point, point)
  prev_point = point

point = points[-1]
prev_point = V3(int(point[0]), int(point[1]))
for point in points:
  point = V3(int(point[0]), int(point[1]))
  r.glColor(222,25,25)
  line(prev_point, point)
  prev_point = point


r.glFinish("./salidas/t.bmp")