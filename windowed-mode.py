import numpy as np
import cv2
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('opencv/data/haarcascades/haarcascade_frontalface_default.xml')
# face_cascade = cv2.CascadeClassifier('opencv/data/haarcascades/haarcascade_frontalface_alt.xml')
# face_cascade = cv2.CascadeClassifier('opencv/data/haarcascades/haarcascade_frontalface_alt2.xml')
# face_cascade = cv2.CascadeClassifier('opencv/data/haarcascades/haarcascade_frontalface_alt_tree.xml')

cap = cv2.VideoCapture(0)

# Write some Text
font = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10, 400)
fontScale = 1
fontColor = (255, 255, 255)
lineType = 2


def main():
    display = (1100, 600)
    fovx = -1
    lastfovx = -1
    while 1:
        if fovx != -1:
            lastfovx = fovx


        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            fovx = 10 + (w * 90 / 350)
            if lastfovx != -1:
                dif = np.abs((fovx - lastfovx))/10
                if dif < 1:
                    if fovx < lastfovx:
                        fovx = lastfovx - (dif*dif*10)
                    else:
                        fovx = lastfovx + (dif*dif*10)

            aspect = (display[0] / display[1])
            fovy = 2 * np.arctan(np.tan(fovx * (np.pi / 180) * .5) / aspect) * (180 / np.pi)
            hw = 8.5
            d = hw / (2 * np.tan((fovx * (np.pi / 180)) / 2))


            img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            newx = int((x + w/2) - 1)
            newy = int((y + h/2) - 1)
            img = cv2.rectangle(img, (newx,newy),(newx,newy), (255, 0, 0), 2)
            cv2.putText(img, str(fovx), bottomLeftCornerOfText, font, fontScale, fontColor, lineType, cv2.LINE_AA)
            cv2.imshow('img', img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


main()

