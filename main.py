#!/usr/bin/python
from time import sleep
from picamera import PiCamera
import zbar
import Image
import sqlite3

# Load config
municipalite = open('./config.txt', 'r')
myMunicipalite = municipalite.read()
print myMunicipalite
municipalite.close()

# open DB
conn = sqlite3.connect('./BD/Treasy_DB')
cursor = conn.cursor()

if myMunicipalite == '' or myMunicipalite is None:
    print('plop')
    # Creation processus menu
else :
    requestMun = """SELECT idMun FROM Municipalite WHERE ville=?"""
    idMun = 0
    cursor.execute(requestMun, (myMunicipalite,))
    rows = cursor.fetchall()
    for row in rows :
        idMun = row[0]
        print "%d" % (row[0])
    print idMun
        
#Camera
camera = PiCamera()
#camera.resolution(1024, 768)
camera.start_preview()
sleep(10)
camera.capture('cam.jpg')

img = "cam.jpg"

# create a reader
scanner = zbar.ImageScanner()

# configure the reader
scanner.parse_config('enable')

# obtain image data
pil = Image.open(img).convert('L')
width, height = pil.size
raw = pil.tostring()

# wrap image data
image = zbar.Image(width, height, 'Y800', raw)
print image
# scan the image for barcodes
scanner.scan(image)

# Prepare request
request = """SELECT Poubelle.couleurPoub FROM Poubelle, Trie, EstFait WHERE Poubelle.idPoub = Trie.idPoub AND Trie.identifiantMat = EstFait.identifiantMat AND Trie.idMun=? AND EstFait.EAN = ?"""
#request2 = """SELECT Produit.nomP FROM Produit WHERE EAN=?"""
#request3 = """SELECT EstFait.identifiantMat FROM EstFait WHERE EstFait.EAN=?"""

# extract results
for symbol in image:
    # do something useful with results
    print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data
    # find barcode in DB
    cursor.execute(request , (idMun, symbol.data))
    rows = cursor.fetchall()
    for row in rows:
        print('{0}'.format(row[0]))

# clean up
conn.close()
del(image)



