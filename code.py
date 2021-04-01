from functions import time, addGravities, setBodies, bodyList, move, timeStep

setBodies()  # creates an object for every body in the system (file bodies.txt)

while True:
    for i in bodyList:  # computates the gravities for all bodies
        addGravities(i)
    for i in bodyList:  # moves all bodies according to the forces applied
        move(i)
    time += timeStep


