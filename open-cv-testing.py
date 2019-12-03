import numpy as np
import cv2
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('opencv/data/haarcascades/haarcascade_frontalface_default.xml')
# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
# eye_cascade = cv2.CascadeClassifier('opencv/data/haarcascades/haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

# Write some Text
font = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10, 400)
fontScale = 1
fontColor = (255, 255, 255)
lineType = 2

""" old floor
verticesFloor = (
    (-100, -1, 100),
    (100,  -1, 100),
    (100,  -1, -100),
    (-100, -1, -100)
)

edgesFloor = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0)
)

surfacesFloor = (
    (0, 1, 2, 3),
    (0, 1, 2, 3)
)"""

verticesFloor = (
    (-100, -1, -100),
    (100, -1, -100),
    (0, -1, 3)
)

edgesFloor = (
    (0, 1),
    (1, 2),
    (0, 2)
)

surfacesFloor = (
    (0, 1, 2),
    (0, 1, 2)
)

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
    )

surfaces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
    )


def Cube():
    glBegin(GL_QUADS)
    for surface in surfaces:
        for vertex in surface:
            glColor3fv((0,1,0))
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def Cube2():
    glBegin(GL_QUADS)
    for surface in surfaces:
        for vertex in surface:
            glColor3fv((1,0,0))
            glVertex3fv((vertices[vertex][0]-3, vertices[vertex][1], vertices[vertex][2]))
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv((vertices[vertex][0]-3, vertices[vertex][1], vertices[vertex][2]))
    glEnd()

def Cube3():
    glBegin(GL_QUADS)
    for surface in surfaces:
        for vertex in surface:
            glColor3fv((0, 0, 1))
            glVertex3fv((vertices[vertex][0]+3, vertices[vertex][1], vertices[vertex][2]))
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv((vertices[vertex][0]+3, vertices[vertex][1], vertices[vertex][2]))
    glEnd()


def Floor():
    glBegin(GL_QUADS)
    for surface in surfacesFloor:
        for vertex in surface:
            glColor3fv((1, 0.5, 0))
            glVertex3fv(verticesFloor[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edgesFloor:
        for vertex in edge:
            glVertex3fv(verticesFloor[vertex])
    glEnd()


def main():
    pygame.init()
    display = (1100, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    i=10
    d = -1
    fovy = -1
    lastfovy = -1
    lastdist = -1
    while 1:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        i+= .5
        for (x, y, w, h) in faces:
            if(fovy != -1):
                lastdist = d
                lastfovy = fovy
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

            avg = (w + h) / 2
            area = avg.__pow__(2)

            aspect = (display[0] / display[1])
            fovx = 10 + (w*90/350)
            fovy = 2 * np.arctan(np.tan(fovx * (np.pi/180) * .5)/aspect) * (180/np.pi)
            hw = 8.5

            glLoadIdentity()

            # update the field of view
            gluPerspective(fovy, aspect, 0.1, 50.0)

            # calculate distance from the camera
            d = hw / (2 * np.tan((fovx*(np.pi/180))/2))
            trn = 6 + d

            # calculate left-right and up-down distance
            centerX = 330
            scaleX = 35  # higher = moves slower
            newX = (x + w/2) / scaleX - (centerX / scaleX)  # centered about 330

            centerY = 235
            scaleY = 70
            newY = (y + h/2) / scaleY - (centerY / scaleY)  # centered about 235???

            # update the look at based on the user's position (position, lookat, up -> only position should change)
            gluLookAt(-newX, -newY, trn, 0, 0, -2, 0, 1, 0)

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            Floor()
            Cube()
            Cube2()
            Cube3()
            pygame.display.flip()
            pygame.time.wait(1)

        k = cv2.waitKey(30) & 0xff
        if k == 27:
            pygame.quit()
            quit()
            break

    cap.release()
    cv2.destroyAllWindows()


main()

