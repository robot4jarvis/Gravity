from math import sqrt, pow, hypot


class Body:
    """(name,m,R,pos,v,F)
       A spherical body with name, mass, radius, position, speed and force applied."""

    def __init__(self, name, m, R, pos, v, F):
        self.name = name  # string
        self.m = float(m)  # mass, scalar magnitude
        self.R = float(R)  # radius, scalar magnitude
        if isinstance(pos, str):  # position, vector (array with 3 values)
            temp = pos[1:-1]
            self.pos = temp.split(",")
        else:
            self.pos = pos

        if isinstance(v, str):  # speed, vector (array with 3 values)
            temp = v[1:-1]
            self.v = temp.split(",")
        else:
            self.v = v

        if isinstance(F, str):  # force applied, vector (array with 3 values)
            temp = F[1:-1]
            self.F = temp.split(",")
        else:
            self.F = F


bodyList = []  # list with all bodies.
G = 6.67408e-11  # Universal gravitational constant (6.67408e-11)


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


def addGravities(bodyN):
    for j in bodyList:
        if j is bodyList[bodyN]:
            pass
        else:
            bodyList[bodyN].F[0] = gravityAxis(bodyList[bodyN], j, 0)
            bodyList[bodyN].F[1] = gravityAxis(bodyList[bodyN], j, 1)
            bodyList[bodyN].F[2] = gravityAxis(bodyList[bodyN], j, 2)


def gravityAxis(A, B, axis):
    """A:Body where the force is being applied, B:body that applies the force, 'axis': axis nº."""
    dAxis = float(A.pos[axis]) - float(B.pos[axis])  # Determines the distance in axis "axis"
    pytDist = hypot((float(A.pos[0]) - float(B.pos[0])), (float(A.pos[1]) - float(B.pos[1])), (float(A.pos[2]) - float(B.pos[2])))  # determines the pythagorean distance
    gravity = (A.m * B.m * G) / (pytDist ** 2)  # determines the module of gravity
    return (gravity * dAxis) / pytDist  # returns the gravity in a certain axis


setBodies()  # creates an object for every body in the system (file bodies.txt)
# """
# ORDER:
# 0. Set up the system (create an object for each body)
# 1. Determine all gravitational forces applied. (F=(Gmm)/r^2)
# 2. With the speed and positions from last step, determine the current position
# 3. Actualize the position and speed of the object."""
