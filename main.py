#!/usr/bin/python
from time import sleep
from picamera import PiCamera
import zbar
import Image
import sqlite3

def initialize():
    # Load config
    municipalite = open('/home/pi/treasy/config.txt', 'r')
    global myMun
    global idMun
    myMun = municipalite.read()
    print myMun
    municipalite.close()

    # open DB
    global conn
    global cursor
    conn = sqlite3.connect('/home/pi/treasy/BD/Treasy_DB')
    cursor = conn.cursor()

    # Recover municipality id in database
    if myMun == '' or myMun is None:
        print('plop')
        # Creation processus menu
    else :
        requestMun = """SELECT idMun FROM Municipalite WHERE ville=?"""
        idMun = 0
        cursor.execute(requestMun, (myMun,))
        rows = cursor.fetchall()
        for row in rows :
            idMun = row[0]
            print "%d" % (row[0])
        print idMun


def barcodeReader():
    global barcode
    #Camera
    camera = PiCamera()

    while (barcode == ""):

        #camera.resolution(1024, 768)
        camera.start_preview()
        sleep(2)
        camera.capture('/home/pi/treasy/cam.jpg')

        img = "/home/pi/treasy/cam.jpg"

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
        request = "SELECT Poubelle.couleurPoub FROM Poubelle, Trie, EstFait WHERE Poubelle.idPoub = Trie.idPoub AND Trie.identifiantMat = EstFait.identifiantMat AND Trie.idMun=? AND EstFait.EAN = ?"

        # extract results
        for symbol in image:
            # do something useful with results
            print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data
            # find barcode in DB
            cursor.execute(request , (idMun, symbol.data))
            rows = cursor.fetchall()
            for row in rows:
                print('{0}'.format(row[0]))
                barcode = row[0]
            del(image)
    

myMun = ""
idMun = ""
conn = ""
cursor = ""


initialize()
print "test idMun"
print idMun


barcode = ""
barcodeReader()
print "test boucle2"
print barcode

# clean up
conn.close()




