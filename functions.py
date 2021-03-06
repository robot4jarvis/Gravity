from math import hypot

bodyList = []
G = 6.67408e-11  # Universal gravitational constant (6.67408e-11)
timeStep = 0.1  # time passed each step
time = 0.0


class Body:
    """(name,m,R,pos,v,F)
       A spherical body with name, mass, radius, position, speed and force applied."""

    def __init__(self, name, m, R, pos, v, F):
        self.name = name  # string
        self.m = float(m)  # mass, scalar magnitude
        self.R = float(R)  # radius, scalar magnitude
        if isinstance(pos, str):  # if it receives a String (it'll only happen the first time)
            temp = pos[1:-1]  # takes out the parenthesis
            self.pos = [float(i) for i in temp.split(",")]  # turns the string into a list
        else:
            self.pos = pos  # if we hadn't received a string, it just asigns the value given

        if isinstance(v, str):  # speed, vector (array with 3 values)
            temp = v[1:-1]
            self.v = [float(i) for i in temp.split(",")]
        else:
            self.v = v

        if isinstance(F, str):  # force applied, vector (array with 3 values)
            temp = F[1:-2]
            self.F = [float(i) for i in temp.split(",")]
        else:
            self.F = F


def setBodies():
    """Takes all info from file 'bodies.txt' and pastes it to object list 'bodyList[]'."""
    with open("bodies.txt") as file:  # open the file with the list of bodies
        for line in "bodies.txt":  # read each line
            reading = file.readline()  # read a line
            if reading[0] == "#" or reading[0] == "\n":  # pass a line if it's a comment or if it's in blank
                pass
            else:
                if reading[0] == "/":  # end file if a certain character is found
                    break
                lect = reading.split(";")  # split line in parts
                bodyList.append(Body(lect[0], lect[1], lect[2], lect[3], lect[4], lect[5]))  # adds an object to "bodyList" that contains the information needed.


def addGravities(body):
    """ Applies gravitational forces from all bodies to 'body'"""
    body.F = [0 for b in body.F]  # we set all values in "Force" to 0
    for j in bodyList:
        if j is body:
            pass
        else:
            body.F[0] += gravityAxis(body, j, 0)  # Apply force in x axis
            body.F[1] += gravityAxis(body, j, 1)  # Apply force in y axis
            body.F[2] += gravityAxis(body, j, 2)  # Apply force in z axis


def gravityAxis(A, B, axis):
    """A:Body where the force is being applied, B:body that applies the force, 'axis': axis n??."""
    dAxis = A.pos[axis] - B.pos[axis]  # Determines the distance in axis "axis"
    pytDist = hypot((A.pos[0] - B.pos[0]), (A.pos[1] - B.pos[1]), (A.pos[2] - B.pos[2]))  # determines the pythagorean distance
    gravity = (A.m * B.m * G) / (pytDist ** 2)  # determines the module of gravity
    return (-gravity * dAxis) / pytDist  # returns the gravity in a certain axis (similar triangles). I don't know why, but it needs a "-".


def move(A):
    for i in range(0, 3):
        A.pos[i] += A.v[i] * timeStep + 0.5 * (A.F[i] / A.m) * (timeStep ** 2)  # s = so + vo*t + (1/2)*a*t^2 for all axis
        A.v[i] += (A.F[i] / A.m)*timeStep  # speed

