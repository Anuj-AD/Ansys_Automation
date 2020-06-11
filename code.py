import pyautogui as pag
import cv2
import imutils
import time
from datetime import datetime

#Ask for the desired Properties
mesh = input('Enter the value of mesh size (in m): ')
#Do this for a certain amount of time (8 hours)
timeout = time.time() + 8*60*60
while True:
    if time.time() > timeout:
        break
    image = pag.screenshot("ss.png")
    image = cv2.imread("ss.png")
    #cv2.imshow("Screenshot", imutils.resize(image, width = 400))
    #cv2.waitKey(0)
    logoLocation = pag.locateOnScreen('logo.png', confidence = 0.9)
    if logoLocation != None:
        #save as new project
        newLocation = pag.locateOnScreen('new.png', confidence = 0.9)
        newPoint = pag.center(newLocation)
        pag.moveTo(newPoint)
        pag.click()
        time.sleep(2)
        dt = datetime.now().strftime("%H%M%S_%d%m")
        newLocation = pag.locateOnScreen('name.png', confidence = 0.9)
        newPoint = pag.center(newLocation)
        pag.moveTo(newPoint)
        pag.click()
        pag.write("Snow Explosion_" + dt)
        time.sleep(1)
        newLocation = pag.locateOnScreen('save.png', confidence = 0.9)
        newPoint = pag.center(newLocation)
        pag.moveTo(newPoint)
        pag.click()
        time.sleep(10)
        #Go to Model
        newLocation = pag.locateOnScreen('Ed1.png', confidence = 0.9)
        newPoint = pag.center(newLocation)
        pag.moveTo(newPoint)
        pag.click()
        pag.click()
        #Go to Modal
        #newLocation = pag.locateOnScreen('Ed2.png', confidence = 0.9)
        #newPoint = pag.center(newLocation)
        #pag.moveTo(newPoint)
        #pag.click()
        #time.sleep(1)
        timex = time.time() + 5*60
        while True:
            if time.time() > timex:
                break
            #Go to mesh
            newLocation = pag.locateOnScreen('Ed3.png', confidence = 0.9)
            if newLocation != None:
                newPoint = pag.center(newLocation)
                pag.moveTo(newPoint)
                time.sleep(2)
                pag.click()
                break
            time.sleep(1)
        #Change sizing
        time.sleep(1)
        newLocation = pag.locateOnScreen('Ed4.png', confidence = 0.9)
        newPointx, newpointy = pag.center(newLocation)
        pag.moveTo(newPointx-22, newpointy)
        pag.click()
        time.sleep(1)
        #change element size
        newLocation = pag.locateOnScreen('Ed5.png', confidence = 0.9)
        newPointx, newpointy = pag.center(newLocation)
        pag.moveTo(newPointx+60, newpointy)
        pag.click()
        pag.write(str(mesh))
        time.sleep(1)
        #solve
        newLocation = pag.locateOnScreen('Ed6.png', confidence = 0.9)
        newPoint= pag.center(newLocation)
        pag.moveTo(newPoint)
        pag.click()
        time.sleep(60)
        #check the solution
        timex = time.time() + 8*60*60
        while True:
            if time.time() > timex:
                file1 = open("update.txt","a") 
                file1.write("Snow Explosion_" + dt + " INCOMPLETE")
                file1.close()
                break
            newLocation = pag.locateOnScreen('Ed8.png', confidence = 0.99)
            if newLocation != None:
                newPoint= pag.center(newLocation)
                pag.moveTo(newPoint)
                pag.click()
                file1 = open("update.txt","a") 
                file1.write("Snow Explosion_" + dt + " COMPLETED")
                file1.close()
                break       
        break
