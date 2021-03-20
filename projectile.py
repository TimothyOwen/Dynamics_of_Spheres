#-------------------------------------------------------------------------------
#PROJECTILE MOTION
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#IMPORTING EXTERNAL MODULES
from tkinter import *
from tkinter import ttk
import time
import random
import math
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#CREATING THE TEXT FOR THE INFORMATION BUTTON
def create_Ptext():
    global menupause1
    #BREAKS THE ACTIVE LOOP AND CLEARS EVERYTHING
    menupause1='yes'
    canvas.delete('all')
    #CREATES THE BACK BUTTON
    back_button=Button(canvas, text="Back", command=reset_canvas1)
    back_button.configure(width=10, activebackground="white")
    back_button_window=canvas.create_window(1150,580,window=back_button)
    #INDENT FOR THE WRITING
    Pline=10
    #LOOP TO MAKE THE TEXT ON THE INFORMATION MODULE
    for p in range(0,33):
        datacontents=(projectilelist[p])[0:-1]
        canvas.create_text(10,Pline,text=datacontents,font=("Arial", 10, "bold"),anchor=NW)
        Pline+=10
#CREATING LABELS
def create_Plabels(canvas, Pg, PangleDeg, Pv):
    text1='g: '+str(round(float(Pg),2))
    text2='Angle: '+str(round(float(PangleDeg),2))
    text3='Velocity: '+str(round(float(Pv),2))
    canvas.create_text(800,60, text=text1, font="15", tag='Plabels')
    canvas.create_text(800,80, text=text2, font="15", tag='Plabels')
    canvas.create_text(800,100, text=text3, font="15", tag='Plabels')
#CONFIGURING MAIN BUTTONS
def configure_Pbuttons(mainCanvas, mainWindow, option, Pginput, Pangleinput, Pvinput):
    global canvas,window,startbutton,pausebutton,resetbutton,getcombogravitybtn,getgravitybtn,getanglebtn,getvelocitybtn
    canvas = mainCanvas
    window = mainWindow
    #CREATE TITLE
    canvas.create_text(800,30,text="Projectile Motion Simulator",font=("Arial", 15, "bold"))
    #CONFIGURING MAIN BUTTONS FOR START,PAUSE,RESET,MENU,BONUS GAME,INFO
    startbutton=Button(canvas, text="START", command=__init1__)
    startbutton.configure(width=10, activebackground="white")
    startbutton_window=canvas.create_window(10,10,anchor=NW,window=startbutton)
    pausebutton=Button(canvas, text="PAUSE", command=pause_run)
    pausebutton.configure(width=10, activebackground="white")
    pausebutton_window=canvas.create_window(10,40,anchor=NW,window=pausebutton)
    resetbutton=Button(canvas, text="RESET", command=reset_canvasCommand)
    resetbutton.configure(width=10, activebackground="white")
    resetbutton_window=canvas.create_window(10,70,anchor=NW,window=resetbutton)
    menubutton=Button(canvas, text="MENU", command=menu)
    menubutton.configure(width=10, activebackground="white")
    menubutton_window=canvas.create_window(1100,10,anchor=NW,window=menubutton)
    #CREATE THE INFO BUTTON
    databutton=Button(canvas,text="Information",command=create_Ptext)
    databutton.configure(width=10, activebackground="white")
    databutton_window=canvas.create_window(1150,580,window=databutton)
    #CONFIGURING COMBOBOX AND CORRESPONDING BUTTON
    combobox=ttk.Combobox(canvas, textvariable=option, value='k')
    combobox.configure(width=10)
    combobox_window=canvas.create_window(100,10,anchor=NW,window=combobox)
    combobox['value']=('Earth','Pluto','Jupiter')
    getcombogravitybtn=Button(canvas, text='CHOOSE g', command=get_goption)
    getcombogravitybtn.configure(width=10, activebackground="white")
    getcombogravitybtn_window=canvas.create_window(100,40,anchor=NW,window=getcombogravitybtn)
    #CONFIGURIN ENTRY BOXES AND CORRESPONDING BUTTONS
    gravitybox=ttk.Entry(window, textvariable=Pginput)
    gravitybox.configure(width=10)
    gravitybox_window=canvas.create_window(200,10,anchor=NW,window=gravitybox)
    getgravitybtn=Button(canvas, text='GRAVITY', command=get_Pg)
    getgravitybtn.configure(width=10, activebackground="white")
    getgravitybtn_window=canvas.create_window(200,40,anchor=NW,window=getgravitybtn)
    anglebox=ttk.Entry(window, textvariable=Pangleinput)
    anglebox.configure(width=10)
    anglebox_window=canvas.create_window(300,10,anchor=NW,window=anglebox)
    getanglebtn=Button(canvas, text='ANGLE', command=get_Pangle)
    getanglebtn.configure(width=10, activebackground="white")
    getanglebtn_window=canvas.create_window(300,40,anchor=NW,window=getanglebtn)
    velocitybox=ttk.Entry(window, textvariable=Pvinput)
    velocitybox.configure(width=10)
    velocitybox_window=canvas.create_window(400,10,anchor=NW,window=velocitybox)
    getvelocitybtn=Button(canvas, text='VELOCITY', command=get_Pv)
    getvelocitybtn.configure(width=10, activebackground="white")
    getvelocitybtn_window=canvas.create_window(400,40,anchor=NW,window=getvelocitybtn)
    #DISABLING THE PAUSE BUTTON
    pausebutton.config(state=DISABLED)
    reset_basevars()
    create_Plabels(canvas, Pg, PangleDeg, Pv)
#DISABLING BUTTONS SO THEY CANT BE PRESSED WHEN ANIMATION IS ACTIVE
def disable_Pbuttons():
    startbutton.config(state=DISABLED)
    pausebutton.config(state=DISABLED)
    getgravitybtn.config(state=DISABLED)
    getanglebtn.config(state=DISABLED)
    getvelocitybtn.config(state=DISABLED)
    getcombogravitybtn.config(state=DISABLED)
#FINDING THE G OPTION THAT HAS BEEN SELECTED IN THE COMBO BOX
def get_goption():
    global typeofoption
    canvas.delete("getgravitybtn")
    canvas.update()
    typeofoption=option.get()
    configure_option()
#AND CONFIGURING IT
def configure_option():
    global Pg
    if typeofoption=='Earth':
        Pg=9.81
    if typeofoption=='Jupiter':
        Pg=26.0
    if typeofoption=='Pluto':
        Pg=0.61
    #DELETING OLD LABEL AND UPDATING IT
    canvas.delete('Plabels')
    create_Plabels()
    canvas.update
#GETTING ENTRY BOX INPUTS
def get_Pg():
    global Pg,Pstop
    try:
        Pg=Pginput.get()
        Pg=float(Pg)
        if Pg<0:
            #VALIDATING G
            error_message()
            canvas.update()
            disable_Pbuttons()
            Pstop='break'
        canvas.delete('Plabels')
        create_Plabels()
        canvas.update()
    except:
        #IF GETTING IT FAILS DO THIS
        error_message()
        disable_Pbuttons()
        canvas.update()
        getgravitybtn.config(state=DISABLED)
def get_Pangle():
    global Pangle,PangleDeg,Pstop
    try:
        Pangle=Pangleinput.get()
        PangleDeg=float(Pangle)
        if PangleDeg<0 or PangleDeg>90:
            #VALIDATING ANGLE
            error_message()
            canvas.update()
            disable_Pbuttons()
            Pstop='break'
        Pangle=float((float(Pangle)/360)*2*3.1415)
        canvas.delete('Plabels')
        create_Plabels()
        canvas.update()
    except:
        #IF GETTING IT FAILS DO THIS
        error_message()
        disable_Pbuttons()
        canvas.update()
        getanglebtn.config(state=DISABLED)
def get_Pv():
    global Pv,Pstop
    try:
        Pv=Pvinput.get()
        Pv=float(Pv)
        if Pv<=0:
            #VALIDATING V
            error_message()
            canvas.update()
            disable_Pbuttons()
            Pstop='break'
        canvas.delete('Plabels')
        create_Plabels()
        canvas.update()
    except:
        #IF GETTING IT FAILS DO THIS
        error_message()
        disable_Pbuttons()
        canvas.update()
        getvelocitybtn.config(state=DISABLED)
def reset_basevars():
    global Pstop,Px,Pg,Pangle,PangleDeg,Pv
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
#MATHEMATICAL SOLUTION TO FIND Y CO FROM X CO
def create_Yco(x):
    x+=1
    y=int((math.tan(Pangle))*x-(Pg/(2*(Pv**2)*((math.cos(Pangle))**2)))*(x**2))
    return y
#CREATE BALL WITH COS X,Y
def create_ball(x,y):
    canvas.create_oval(x-10, y-10, x+10, y+10, fill='black', outline='', activefill='white',tags='ball')
#PAUSING EACH ANIMATION
def pause_run():
    global pause
    #IF PAUSE IS EQUAL TO YES IT SHOULD CAUSE EACH ACTIVE LOOP TO PAUSE
    pause='yes'
def error_message(canvas):
    canvas.create_text(600,300,text='# AN ERROR HAS OCCURED: THE DATA INPUTTED COULD BE INVALID, BE OUT OF RANGE, OR THE ANIMATION IS OUT OF DISPLAY RANGE: PLEASE RESET THE MODULE AND INPUT NEW DATA #',fill='red',font=("Arial", 8, "bold"),tags='error')
    canvas.update()
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
def reset_canvasCommand():
    reset_canvas1()
#-------------------------------------------------------------------------------
#THE INITIALISING PROCEDURE STARTED WHEN THE USER CLICKS THE PROJECTILE START BUTTON
def __init1__():
    global pause,menupause1,Pstop,Px
    #DISABLING THE BUTTONS AFTER START IS PRESSED
    disable_Pbuttons()
    resetbutton.config(state=DISABLED)
    #ENABLING THE PAUSE BUTTON
    pausebutton.config(state=ACTIVE)
    #MAKING SURE ITS NOT PAUSED AND BROKEN
    pause='no'
    menupause1='no'
    Pstop='no'
    #MENU PAUSED IS USED SO THE BALL IS NOT CREATED ON THE MENU WINDOW
    #THIS IS THE ACTIVE LOOP
    while Pstop!='break':
        try:
            #SO NO BALLS ARE CREATED ON THE MAIN MENU
            if menupause1=='yes':
                Pstop='break'
            #FINDING COORDINATES AND PUTTING THEM IN FRIENDLY VARIABLES
            x1=Px
            y1=600-create_Yco(x1)
            #THE AMOUND THAT IS ADDED IS THE RESOLUTION OF THE ANIMATION
            x2=x1+2
            y2=600-create_Yco(x2)
            #TO MAKE IT LOOK LIKE ITS PAUSED
            if pause=='yes':
                #START BUTTON AND RESET BUTTON ACTIVATED AGAIN
                startbutton.config(state=ACTIVE)
                resetbutton.config(state=ACTIVE)
                #PAUSE BUTTON DISABLED
                pausebutton.config(state=DISABLED)
                #LABELS BALL AND LINE ADDED
                create_Plabels()
                create_ball(x2,y2)
                canvas.create_line(x1, y1, x2, y2)
                canvas.update()
                #BREAKING FROM THE LOOP
                Pstop='break'
            if  x2>=1200:
                #CREATING THE LABELS
                create_Plabels()
                #THIS IS SO THAT BALLS ARE NOT CREATED OUTSIDE THE X FRAME
                error_message()
                pausebutton.config(state=DISABLED)
                resetbutton.config(state=ACTIVE)
                Pstop='break'
            if y2>600 or y2<0:
                #CREATING THE LABELS
                create_Plabels()
                #THIS IS SO THAT BALLS ARE NOT CREATED OUTSIDE THE Y FRAME
                error_message()
                pausebutton.config(state=DISABLED)
                resetbutton.config(state=ACTIVE)
                Pstop='break'
            if Pstop=='no':
                #THIS IS WHAT HAPPENS MOST TIMES
                #CREATING THE LABELS, BALL AND LINE
                create_Plabels()
                create_ball(x2, y2)
                canvas.create_line(x1, y1, x2, y2)
                #CANVAS UPDATED
                canvas.update()
                #FRAMES MUST BE DELETED SO THAT THEY CAN BE UPDATED
                canvas.delete('ball')
                canvas.delete('Plabels')
            #X COORDINATE IS ITERATED BY 2 AND TIME IS WAITED SO SPEED IS APPROPRIATE
            Px=x2
            time.sleep(0.01)
        except:
            #IF AN UNFORESEEN ERROR OCCURS THIS IS DONE
            error_message(canvas)
            pausebutton.config(state=DISABLED)
            resetbutton.config(state=ACTIVE)
            canvas.update()
