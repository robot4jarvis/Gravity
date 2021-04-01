from math import hypot

from functions import addGravities, setBodies, Body, gravityAxis, bodyList

setBodies()  # creates an object for every body in the system (file bodies.txt)
for i in bodyList:  # computates the gravities for all bodies
    addGravities(i)
    print(i.F)
