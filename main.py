#!/usr/bin/python
import os
import time

def camera():
    print('enfant')
    time.sleep(3)


Municipalite = open('./configmunicipalite.txt', 'r')
myMunicipalite = Municipalite.read()
Municipalite.close()

if myMunicipalite == '' or myMunicipalite is None:
    print('plop')
    # A definir

newCam = os.fork()
if newCam == 0:
    camera()
else:
    os.wait()
    print('parent')



