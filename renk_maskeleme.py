import cv2
import numpy as np
 
kamera = cv2.VideoCapture(0)
 
while(True):
    ret, bilgisayarKamerasi = kamera.read()
    hsv=cv2.cvtColor(bilgisayarKamerasi,cv2.COLOR_BGR2HSV)
    baslangic_altKirmizi=np.array([30,150,50])
    bitis_ustKirmizi=np.array([255,255,180]) 
    maskeleme=cv2.inRange(hsv,baslangic_altKirmizi,bitis_ustKirmizi)
    filtreli_goruntu=cv2.bitwise_and(bilgisayarKamerasi,bilgisayarKamerasi,mask=maskeleme)
    gray = cv2.cvtColor(filtreli_goruntu,cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray,30,200)
    kernel = np.ones((5,5), np.uint8)
    img_erosion = cv2.erode(edged, kernel, iterations=1)
    contours, hierarchy = cv2.findContours(img_erosion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(bilgisayarKamerasi, contours, -1, (0, 255, 0), 3)

    cv2.imshow('Orjinal Goruntu (Bilgisayar Kamerasi)',bilgisayarKamerasi)
    cv2.imshow('Filtrenlemis Goruntu (Bilgisayar Kamerasi)',filtreli_goruntu)
    cv2.imshow('gray',gray)
    cv2.imshow('edged',edged)
    if cv2.waitKey(25) & 0xFF == ord('x'):
        exit()
