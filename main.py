#!/usr/bin/python
import os
import time
import picamera
import io
from PIL import Image

def camera():
    stream = io.BytesIO()
    camera = picamera.PiCamera()
    #camera.resolution (1024, 768)
    camera.start_preview()
    time.sleep(2)
    camera.capture(stream, format='jpeg')
    stream.seek(0)
    image = Image.open(stream)
    print('camera')
    # Tourne et prend des photos, interprete le code barre

    #for i, filename in enumerate(camera.capture_continuous('image{counter:02d}.jpg')):
    #    print(filename)
    #    time.sleep(2)
    #    if i == 3 :
    #        break
    
    #for filemane in camera.capture_continuous('img{counter:03d}.jpg'):
    #    print ('Captured %s' % filename)
    #    sleep(2)
    camera.stop_preview()
    camera.close()

municipalite = open('./config.txt', 'r')
myMunicipalite = municipalite.read()
municipalite.close()

if myMunicipalite == '' or myMunicipalite is None:
    print('plop')
    # Creation processus menu

newCam = os.fork()
if newCam == 0:
    camera()
else:
    # Creation processus menu
    os.wait()
    print('parent')



