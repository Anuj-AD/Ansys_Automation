# Ansys_Automation
This script attempts to automate the recurring process of setting up a simulation in Ansys.
The script uses pyautogui to find specific elements of images on screen and then navigates to different parts and enters required values. The code here simply alters the value of mesh only once. However loops can be used to do the same process again and again. Further, similar algorithm can be used to do any task where a similar simulation is required to be done many times with very less changes in parameters. For example, this can be used to simulate an object for different forces.
The images need to be changed with the images of your own pc, if the code doesn't work. These images are taken from a 720p screen using snipping tool. 
Update file stores the result of each simulation, that is whether simulation is complete or not.
