from functions import addGravities, setBodies, bodyList, reposition

setBodies()  # creates an object for every body in the system (file bodies.txt)
for i in bodyList:  # computates the gravities for all bodies
    addGravities(i)
reposition(bodyList[0])
