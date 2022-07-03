def nothing(x):
    pass 
import cv2
import numpy as np
import serial
import time
from msvcrt import getch
import pyfirmata
import pygame
pygame.init()
width, height = 20, 20
screen = pygame.display.set_mode((width, height))
board = pyfirmata.Arduino('COM24')
print("Communication Successfully started")
servo1 = 6
servo2 = 3
servo3 = 5
servo4 = 10
servo5 = 9
servo6 = 7
servo7 = 11
servo1a = 0
servo1b = 0
servo2c = 0
servo3a = 0
servo3b = 0
servo4a = 0
servo4b = 0
servo5c = 0
servo6a = 0
servo6b = 0
servo7a = 0
kamera_servo = 8
def rotate(pin, angle):
        board.digital[pin].write(angle)
        time.sleep(0.015)
def ust_motor(*args):
    cv2.setTrackbarPos('ust_motor_hiz','image',300)    
    cv2.setTrackbarPos('motor7_hiz','image',300)
cap = cv2.VideoCapture(0)
img = np.zeros((300,500,3), np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('low_b','image',0,255,nothing)
cv2.createTrackbar('low_g','image',0,255,nothing)
cv2.createTrackbar('low_r','image',0,255,nothing)
cv2.createTrackbar('high_b','image',0,255,nothing)
cv2.createTrackbar('high_g','image',0,255,nothing)
cv2.createTrackbar('high_r','image',0,255,nothing)
cv2.createTrackbar('erosion','image',0,10,nothing)
cv2.createTrackbar('dilation','image',0,10,nothing)
cv2.createTrackbar('ana_motor_hiz','image',0,100,nothing)
cv2.createTrackbar('ust_motor_hiz','image',0,600,nothing)
cv2.createTrackbar('motor7_hiz','image',0,600,nothing)
cv2.createTrackbar('motor_sifirla','image',0,1,ust_motor)
rotate(servo1,1470)
rotate(servo2,1470)
rotate(servo3,1470)
rotate(servo4,1470)
rotate(servo5,1470)
rotate(servo6,1470)
rotate(servo7,1470)
rotate(kamera_servo,90)
cv2.setTrackbarPos('low_b','image',30)
cv2.setTrackbarPos('low_g','image',150)
cv2.setTrackbarPos('low_r','image',50)
    
cv2.setTrackbarPos('high_b','image',255)
cv2.setTrackbarPos('high_g','image',255)
cv2.setTrackbarPos('high_r','image',180)
cv2.setTrackbarPos('erosion','image',8)
cv2.setTrackbarPos('ana_motor_hiz','image',50)
cv2.setTrackbarPos('ust_motor_hiz','image',300)
cv2.setTrackbarPos('motor7_hiz','image',300)
time.sleep(7)
while cap.isOpened():
    ret,image = cap.read()
    low_b = cv2.getTrackbarPos('low_b',"image")
    low_g = cv2.getTrackbarPos('low_g',"image")
    low_r = cv2.getTrackbarPos('low_r',"image")
    high_b = cv2.getTrackbarPos('high_b',"image")
    high_g = cv2.getTrackbarPos('high_g',"image")
    high_r = cv2.getTrackbarPos('high_r',"image")
    erosion = cv2.getTrackbarPos('erosion',"image")
    dilation = cv2.getTrackbarPos('dilation',"image")
    ana_hiz = cv2.getTrackbarPos('ana_motor_hiz','image')
    ust_motor_hiz = cv2.getTrackbarPos('ust_motor_hiz','image') -300
    motor7_hiz = cv2.getTrackbarPos('motor7_hiz','image') -300
    servo2c = ust_motor_hiz
    servo5c = ust_motor_hiz
    servo7a = motor7_hiz
    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    low = (low_b,low_g,low_r) #blue (100,60,60) # red (30,150,50)
    high = (high_b,high_g,high_r) #blue (140,255,255) #red (255,255,180)
    mask = cv2.inRange(hsv,low,high)
    result = cv2.bitwise_and(image, image, mask = mask)
    kernel = np.ones((5,5), np.uint8)
    img_erosion = cv2.erode(result, kernel, iterations=erosion)
    img_dilation = cv2.dilate(img_erosion, kernel, iterations=dilation)
    gray = cv2.cvtColor(img_dilation,cv2.COLOR_BGR2GRAY)
    contours, hierarchy = cv2.findContours(gray.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True),True)
        if (len(approx) > 7) and (len(approx) < 17):
            cv2.drawContours(image, [cnt], 0, (0,255,255),-1)
            moments = cv2.moments(cnt)
            try:
                cx = int(moments['m10']/moments['m00'])
                cy = int(moments['m01']/moments['m00'])
                cv2.putText(image,str(cx,cy),(cx-50,cy),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1)
                cv2.putText(image,".",(cx,cy),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),1)
                print(cx,cy)
            except:
                print("şekil tespit hatası")
    cv2.imshow("mask",img_dilation)
    cv2.imshow("frame",image)
    cv2.imshow("image",img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("ğ"):
        exit()
    screen.fill((20, 20, 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYUP:
            servo1a = 0
            servo3a = 0 
            servo4a = 0
            servo6a = 0
            servo1b = 0
            servo3b = 0 
            servo4b = 0
            servo6b = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        servo1a = 300
        servo3a = 300
        servo4a = 300
        servo6a = 300
        if keys[pygame.K_a]:
            servo1b = 300
            servo3b = -300
            servo4b = -300
            servo6b = -300
        if keys[pygame.K_d]:
            servo1b = -300
            servo3b = 300
            servo4b = 300
            servo6b = 300
    elif keys[pygame.K_a]:
        servo1b = 300
        servo3b = -300
        servo4b = -300
        servo6b = -300
    elif keys[pygame.K_d]:
        servo1b = -300
        servo3b = 300
        servo4b = 300
        servo6b = 300
    elif keys[pygame.K_s]:
        servo1a = -300
        servo3a = -300 
        servo4a = -300
        servo6a = -300
    rotate(servo1,1470+((servo1a+servo1b)*(ana_hiz/100)))
    rotate(servo2,1470+(servo2c*(ust_motor_hiz/100)))   
    rotate(servo3,1470+(((-1*servo3a)+(servo3b))*ana_hiz/100))
    rotate(servo4,1470+((servo4a+servo4b)*ana_hiz/100))
    rotate(servo5,1470+((servo5c)*ust_motor_hiz/100))
    rotate(servo6,1470+(((servo6a)+(servo6b))*ana_hiz/100))
    rotate(servo7,1470+((servo7a)*motor7_hiz/100))
    
    #print("servo1",1470+((servo1a+servo1b)*(ana_hiz/100))," servo2",1470+(servo2c*(ust_motor_hiz/100))," servo3",1470+(((-1*servo3a)+(servo3b))*ana_hiz/100)," servo4",1470+((servo4a+servo4b)*ana_hiz/100)," servo5",1470+((servo5c)*ust_motor_hiz/100)," servo6",1470+(((servo6a)+(servo6b))*ana_hiz/100)," servo7",1470+((servo7a)*motor7_hiz/100))
    pygame.display.flip()
