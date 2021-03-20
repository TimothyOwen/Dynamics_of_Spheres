#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#TIMOTHY OWEN MILLFIELD SCHOOL 63437 2512
#A2 COMPUTING PROJECT CODE
#PYTHON
#-------------------------------------------------------------------------------
#SOME IMPORTANT NOTES
#1. A DOUBLE LINE OF HYPENS MEANS A BOUNDARY WITH TWO MAIN SECTIONS
#2. GLOBAL VARIABLES ARE GENERALLY DEFINED EACH TIME THEY ARE ASSIGNED TO IN A
#   A PROCEDURE.
#3. A CAPITAL LETTER OR A LETTER BEFORE A WORD GENERALLY DENOTES THE MODULE
#   THAT THE VARIABLE OR PROCEDURE IS LINKED TO
#4. A COMMENT IS GENERALLY REFERRING TO A LINE OF CODE UNDER IT,OR IF THERE IS
#   2 DIRECTLY ABOVE AND BELOW EACH OTHER THEN THE TOP ONE REFERS TO THE CODE
#   ABOVE IT AND VICE VERSA FOR THE BOTTOM ONE
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#IMPORTING EXTERNAL MODULES
from tkinter import *
from tkinter import ttk
import time
import random
import math
#IMPORTING INTERNAL MODULES
import projectile
import momentum
import shm
import orbit
#-------------------------------------------------------------------------------
#CREATING THE MAIN WINDOW
window=Tk()
window.title("Project")
#-------------------------------------------------------------------------------
#THE CODE CONSISTS OF FIVE PARTS
#-------------------------------------------------------------------------------
#1. UNIVERSAL PROCEDURES
#2. PROJECTILE MODULE
#3. MOMENTUM MODULE
#4. SIMPLE HARMONIC MOTION (SHM) MODULE
#5. ORBIT MODULE
#THEN AT THE END THERE IS SOME CODE TO CREATE THE WINDOWS
#-------------------------------------------------------------------------------
#START OF THE MAIN BODY OF THE CODE
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#CREATING THE CANVAS THE MAIN TOOL USED FOR ANIMATION
def create_canvas():
    global canvas
    canvas=Canvas(window, width=1200, height=600, background='grey')
    canvas.grid(row=0, column=0, sticky=(N,W,E,S))
#RESETTING THE BASE VARIABLES FOR EVERY MODULE EACH TIME YOU RESET ONE
def reset_basevars():
    global Pstop,Px,Pg,Pangle,PangleDeg,Pv,Mstop,Mx1,Mx2,Mm1,Mm2,Mv1,Mv2,Me,Sm,Sk,SA,Odirection,Oe,Oa,Ov
    #PROJECTILES
    #---------------------------------------------------------------------------
    Pstop='no'
    #X COORDINATE OF PROJECTILES MUST BE RESET EACH TIME YOU HIT RESET
    Px=1
    Pg=9.81
    #THE ANGLE USED FOR CALCULATIONS MUST BE IN RADIANS AND THE ONE FOR DISPLAY IN DEGREES, BEING
    #GLOBAL MEANS THAT I MUST HAVE TWO SEPERATE VARIABLES
    Pangle=45
    PangleDeg=Pangle
    Pv=100
    #---------------------------------------------------------------------------
    #MOMENTUM
    #---------------------------------------------------------------------------
    Mstop='no'
    Mx1=400
    Mx2=800
    Mm1=1
    Mm2=2
    Mv1=1
    Mv2=-1
    Me=1
    #---------------------------------------------------------------------------
    #SHM
    #---------------------------------------------------------------------------
    Sm=1
    Sk=0.01
    SA=100
    #---------------------------------------------------------------------------
    #ORBITS
    #---------------------------------------------------------------------------
    Odirection=1
    Oe=0
    Oa=100
    Ov=1
    #---------------------------------------------------------------------------
#PAUSING EACH ANIMATION
def pause_run():
    global pause
    #IF PAUSE IS EQUAL TO YES IT SHOULD CAUSE EACH ACTIVE LOOP TO PAUSE
    pause='yes'
#UNIVERSAL ERROR MESSAGE FOR EVERY MODULE
def error_message():
    canvas.create_text(600,300,text='# AN ERROR HAS OCCURED: THE DATA INPUTTED COULD BE INVALID, BE OUT OF RANGE, OR THE ANIMATION IS OUT OF DISPLAY RANGE: PLEASE RESET THE MODULE AND INPUT NEW DATA #',fill='red',font=("Arial", 8, "bold"),tags='error')
    canvas.update()
#-------------------------------------------------------------------------------
#MAIN MENU OF THE PROGRAM
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
def main_menu():
    #CREATING THE CANVAS ON THE MAIN WINDOW
    create_canvas()
    #READING THE DATA FILE INTO A ARRAY
    data_file()
    #MAIN MENU TITLE
    canvas.create_text(600,200,text="Main Menu",font="Helvetica 20")
    #BUTTONS TO EACH MODULE
    projectilebutton=Button(canvas,text="Projectiles",command=reset_canvas1,font="Arial")
    projectilebutton.configure(width=10,activebackground="white")
    projectilebutton_window=canvas.create_window(600,250,window=projectilebutton)
    momentumbutton=Button(canvas,text="Momentum",command=reset_canvas2,font="Brown")
    momentumbutton.configure(width=10,activebackground="white")
    momentumbutton_window=canvas.create_window(600,300,window=momentumbutton)
    shmbutton=Button(canvas,text="SHM",command=reset_canvas3,font="Brown")
    shmbutton.configure(width=10,activebackground="white")
    shmbutton_window=canvas.create_window(600,350,window=shmbutton)
    orbitbutton=Button(canvas,text="Orbits",command=reset_canvas4,font="Brown")
    orbitbutton.configure(width=10,activebackground="white")
    orbitbutton_window=canvas.create_window(600,400,window=orbitbutton)
    #CREATING STAMP
    canvas.create_text(5,595,text="© Tim Owen 2016",anchor=SW,font="Brown 8")
#RESETTING EACH CANVAS FOR THE 4 SIMULATION MODULES, USED TO RESET EACH ONE
def reset_canvas1():
    global menupause1
    #INDICATES THAT THE ACTIVE LOOP SHOULD STOP TO CREATE THE MENU
    menupause1='yes'
    #RESETTING EVERYTHING
    canvas.delete("all")
    reset_basevars()
    configure_Pbuttons()
def reset_canvas2():
    global menupause2
    #INDICATES THAT THE ACTIVE LOOP SHOULD STOP TO CREATE THE MENU
    menupause2='yes'
    #RESETTING EVERYTHING
    canvas.delete("all")
    reset_basevars()
    configure_Mbuttons()
def reset_canvas3():
    global menupause3
    #INDICATES THAT THE ACTIVE LOOP SHOULD STOP TO CREATE THE MENU
    menupause3='yes'
    #RESETTING EVERYTHING
    canvas.delete("all")
    __init3__()
def reset_canvas4():
    global menupause4
    #INDICATES THAT THE ACTIVE LOOP SHOULD STOP TO CREATE THE MENU
    menupause4='yes'
    #RESETTING EVERYTHING
    canvas.delete("all")
    reset_basevars()
    __init4__()
#THE SECOND TWO INITIALISING PROCEDURES DONT HAVE BUTTON CONFIGURING PROCEDURES BECAUSE THEY RUN WITHOUT YOU PRESSING START
#PROCEDURE USED TO GO BACK TO THE MAIN MENU
def menu():
    global menupause1,menupause2,menupause3,menupause4
    #MAKE SURE EVERY ACTIVE LOOP IS BROKEN
    menupause1='yes'
    menupause2='yes'
    menupause3='yes'
    menupause4='yes'
    #RESET EVERYTHING AND GO BACK TO THE MAIN MENU
    canvas.delete("all")
    main_menu()
#THIS PROCEDURE READS THE DATA FILE AND STORES THE INFORMATION IN WHICHEVERS MODULES INFORMATION LIST
def data_file():
    global projectilelist,momentumlist,shmlist,orbitlist
    data=open('datafile.txt','r+')
    #LISTS OF INFORMATION
    projectilelist=[]
    momentumlist=[]
    shmlist=[]
    orbitlist=[]
    for p in range(0,33):
        new=data.readline()
        projectilelist+=[new]
    for m in range(0,50):
        new=data.readline()
        momentumlist+=[new]
    for s in range(0,49):
        new=data.readline()
        shmlist+=[new]
    for o in range(0,25):
        new=data.readline()
        orbitlist+=[new]




#----------------------------------------------------------------------------------------------------
#MAIN INTIATING PROCEDURE
def __init4__():
    global Ostop,Oeinput,Oainput,Ovinput,menupause4
    #CREATE TITLE
    canvas.create_text(600,30,text="Orbital Mechanics Simulator",font=("Arial", 15, "bold"))
    #DEFINING AS STRING VARIABLES
    Oeinput=StringVar()
    Oainput=StringVar()
    Ovinput=StringVar()
    #CONFIGURING BUTTONS
    configure_Obuttons()
    create_Olabels()
    #RESTTING THE BASE VARS
    reset_basevars()
    #FOR THE LOOP
    theta=90
    menupause4='no'
    Ostop='no'
    while Ostop!='break' and menupause4!='yes':
        try:
            create_satellite(theta)
            #UPDATES AND ITERATES IT
            canvas.update()
            theta+=1
            canvas.delete('Osatellite')
        except:
            error_message()
            canvas.update()
#------------------------------------------------------------
#END OF MAIN CODE
#------------------------------------------------------------
#THE ORIGIN PROCEDURE IS THE MENU AND CALLS THE WHOLE PROGRAM
main_menu()
window.mainloop()
