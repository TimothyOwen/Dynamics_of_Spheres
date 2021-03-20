from tkinter import *
from tkinter import ttk
import time
import random
import math
import projectile
import momentum
import shm
import orbit
#CREATING THE MAIN WINDOW
window=Tk()
window.title("Project")
#-------------------------------------------------------------------------------
#THE CODE CONSISTS OF FIVE PARTS
#-------------------------------------------------------------------------------
#1. UNIVERSAL PROCEDURES
#2. PROJECTILES MODULE
#3. MOMENTUM MODULE
#4. SIMPLE HARMONIC MODULE
#5. ORBITS MODULE
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
    Pstop,Px,Pg,Pangle,PangleDeg,Pv = projectile.reset_basevars()
    Mstop,Mx1,Mx2,Mm1,Mm2,Mv1,Mv2,Me = momentum.reset_basevars()
    Sm,Sk,SA = shm.reset_basevars()
    Odirection,Oe,Oa,Ov = orbit.reset_basevars()
#PAUSING EACH ANIMATION
def pause_run():
    global pause
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
    create_canvas()
    #READING THE DATA FILE INTO A ARRAY
    data_file()
    canvas.create_text(600,200,text="Main Menu",font="Helvetica 20")
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
    canvas.create_text(5,595,text="� Tim Owen 2016",anchor=SW,font="Brown 8")
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
#-------------------------------------------------------------------------------
#PROJECTILE MOTION
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#VARIABLES FOR THE LISTBOX
listbox=''
typeofoption=''
#DECLARING OPTION VARIABLES AS STRINGS
option=StringVar()
Pginput=StringVar()
Pangleinput=StringVar()
Pvinput=StringVar()
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
def create_Plabels():
    text1='g: '+str(round(float(Pg),2))
    text2='Angle: '+str(round(float(PangleDeg),2))
    text3='Velocity: '+str(round(float(Pv),2))
    canvas.create_text(800,60, text=text1, font="15", tag='Plabels')
    canvas.create_text(800,80, text=text2, font="15", tag='Plabels')
    canvas.create_text(800,100, text=text3, font="15", tag='Plabels')
#CONFIGURING MAIN BUTTONS
def configure_Pbuttons():
    global startbutton,pausebutton,resetbutton,getcombogravitybtn,getgravitybtn,getanglebtn,getvelocitybtn
    #CREATE TITLE
    canvas.create_text(800,30,text="Projectile Motion Simulator",font=("Arial", 15, "bold"))
    #CONFIGURING MAIN BUTTONS FOR START,PAUSE,RESET,MENU,BONUS GAME,INFO
    startbutton=Button(canvas, text="START", command=__init1__)
    startbutton.configure(width=10, activebackground="white")
    startbutton_window=canvas.create_window(10,10,anchor=NW,window=startbutton)
    pausebutton=Button(canvas, text="PAUSE", command=pause_run)
    pausebutton.configure(width=10, activebackground="white")
    pausebutton_window=canvas.create_window(10,40,anchor=NW,window=pausebutton)
    resetbutton=Button(canvas, text="RESET", command=reset_canvas1)
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
    create_Plabels()
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
#MATHEMATICAL SOLUTION TO FIND Y CO FROM X CO
def create_Yco(x):
    x+=1
    y=int((math.tan(Pangle))*x-(Pg/(2*(Pv**2)*((math.cos(Pangle))**2)))*(x**2))
    return y
#CREATE BALL WITH COS X,Y
def create_ball(x,y):
    canvas.create_oval(x-10, y-10, x+10, y+10, fill='black', outline='', activefill='white',tags='ball')
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
            error_message()
            pausebutton.config(state=DISABLED)
            resetbutton.config(state=ACTIVE)
            canvas.update()
#----------------------------------------------------------------------------------------------------
#MOMENTUM
#----------------------------------------------------------------------------------------------------
#CREATING THE INFO TEXT
def create_Mtext():
    global menupause2
    menupause2='yes'
    canvas.delete('all')
    back_button=Button(canvas, text="Back", command=reset_canvas2)
    back_button.configure(width=10, activebackground="white")
    back_button_window=canvas.create_window(1150,580,window=back_button)
    Mline=10
    print(momentumlist)
    for p in range(0,50):
        datacontents=(momentumlist[p])[0:-1]
        canvas.create_text(10,Mline,text=datacontents,font=("Arial", 10, "bold"),anchor=NW)
        Mline+=10
#CREATING THE LABELS FOR THE MASS,VELOCITIES,COR EACH ITERATION
def create_Mlabels():
    canvas.delete('Mlabels')
    text1='Velocity 1: '+str(round(Mv1,2))
    text2='Velocity 2: '+str(round(Mv2,2))
    text3='Mass 1: '+str(round(Mm1,2))
    text4='Mass 2: '+str(round(Mm2,2))
    text5='C.O.R: '+str(round(Me,2))
    canvas.create_text(800,40, text=text1, font="15", tag='Mlabels')
    canvas.create_text(800,60, text=text2, font="15", tag='Mlabels')
    canvas.create_text(800,80, text=text3, font="15", tag='Mlabels')
    canvas.create_text(800,100, text=text4, font="15", tag='Mlabels')
    canvas.create_text(800,120, text=text5, font="15", tag='Mlabels')
#CONFIGURING MAIN BUTTONS AGAIN
def configure_Mbuttons():
    global startbutton,pausebutton,resetbutton,getmassAbtn,getmassBbtn,getvelocityAbtn,getvelocityBbtn,getcorbtn
    #CREATE TITLE
    canvas.create_text(800,19,text="Momentum Simulator",font=("Helvetica 15 bold"))
    #CREATE BUTTONS
    startbutton=Button(canvas,text="START",command=__init2__)
    startbutton.configure(width=10,activebackground="white")
    startbutton_window=canvas.create_window(10,10,anchor=NW,window=startbutton)
    pausebutton=Button(canvas,text="PAUSE",command=pause_run)
    pausebutton.configure(width=10,activebackground="white")
    pausebutton_window=canvas.create_window(10,40,anchor=NW,window=pausebutton)
    resetbutton=Button(canvas,text="RESET",command=reset_canvas2)
    resetbutton.configure(width=10,activebackground="white")
    resetbutton_window=canvas.create_window(10,70,anchor=NW,window=resetbutton)
    menubutton=Button(canvas,text="MENU",command=menu)
    menubutton.configure(width=10,activebackground="white")
    menubutton_window=canvas.create_window(1100,10,anchor=NW,window=menubutton)
    #CREATE THE INFO BUTTON
    databutton=Button(canvas,text="Information",command=create_Mtext)
    databutton.configure(width=10, activebackground="white")
    databutton_window=canvas.create_window(1150,580,window=databutton)
    #CONFIGURING THESE ENTRYBOXES
    massAbox=ttk.Entry(window, textvariable=massAinput)
    massAbox.configure(width=10)
    massAbox_window=canvas.create_window(100,10,anchor=NW,window=massAbox)
    getmassAbtn=Button(canvas, text='MASS 1', command=get_massA)
    getmassAbtn.configure(width=9, activebackground="white")
    getmassAbtn_window=canvas.create_window(100,40,anchor=NW,window=getmassAbtn)
    massBbox=ttk.Entry(window, textvariable=massBinput)
    massBbox.configure(width=10)
    massBbox_window=canvas.create_window(200,10,anchor=NW,window=massBbox)
    getmassBbtn=Button(canvas, text='MASS 2', command=get_massB)
    getmassBbtn.configure(width=9, activebackground="white")
    getmassBbtn_window=canvas.create_window(200,40,anchor=NW,window=getmassBbtn)
    velocityAbox=ttk.Entry(window, textvariable=velocityAinput)
    velocityAbox.configure(width=10)
    velocityAbox_window=canvas.create_window(300,10,anchor=NW,window=velocityAbox)
    getvelocityAbtn=Button(canvas, text='VELOCITY 1', command=get_velocityA)
    getvelocityAbtn.configure(width=9, activebackground="white")
    getvelocityAbtn_window=canvas.create_window(300,40,anchor=NW,window=getvelocityAbtn)
    velocityBbox=ttk.Entry(window, textvariable=velocityBinput)
    velocityBbox.configure(width=10)
    velocityBbox_window=canvas.create_window(400,10,anchor=NW,window=velocityBbox)
    getvelocityBbtn=Button(canvas, text='VELOCITY 2', command=get_velocityB)
    getvelocityBbtn.configure(width=9, activebackground="white")
    getvelocityBbtn_window=canvas.create_window(400,40,anchor=NW,window=getvelocityBbtn)
    corbox=ttk.Entry(window, textvariable=corinput)
    corbox.configure(width=10)
    corbox_window=canvas.create_window(500,10,anchor=NW,window=corbox)
    getcorbtn=Button(canvas, text='COEFFICIENT', command=get_cor)
    getcorbtn.configure(width=9, activebackground="white")
    getcorbtn_window=canvas.create_window(500,40,anchor=NW,window=getcorbtn)
    #CREATING THE LABELS
    create_Mlabels()
#DISABLING ALL BUTTONS EXCEPT FOR MENU, RESET AND INFO AFTER A ERROR MESSAGE
def disable_Mbuttons():
    startbutton.config(state=DISABLED)
    pausebutton.config(state=DISABLED)
    getmassAbtn.config(state=DISABLED)
    getmassBbtn.config(state=DISABLED)
    getvelocityAbtn.config(state=DISABLED)
    getvelocityBbtn.config(state=DISABLED)
    getcorbtn.config(state=DISABLED)
#ENTRY BOX VARIABLES
massAinput=StringVar()
massBinput=StringVar()
velocityAinput=StringVar()
velocityBinput=StringVar()
corinput=StringVar()
#ENTRY BOX PROCEDURES
def get_massA():
    global Mm1,Mstop
    try:
        Mm1=float(massAinput.get())
        #VALIDATING THE RANGE OF THE MASS
        if Mm1<=0:
            error_message()
            canvas.update()
            disable_Mbuttons()
            Mstop='break'
        canvas.delete('Mlabels')
        create_Mlabels()
        canvas.update()
    except:
        error_message()
        canvas.update()
        disable_Mbuttons()
        Mstop='break'
def get_massB():
    global Mm2,Mstop
    try:
        Mm2=float(massBinput.get())
        #VALIDATING THE RANGE OF THE MASS
        if Mm2<=0:
            error_message()
            canvas.update()
            disable_Mbuttons()
            Mstop='break'
        canvas.delete('Mlabels')
        create_Mlabels()    
        canvas.update()
    except:
        error_message()
        canvas.update()
        disable_Mbuttons()
        Mstop='break'
def get_velocityA():
    global Mv1,Mstop
    try:
        Mv1=float(velocityAinput.get())
        #VALIDATING THE RANGE OF THE VELOCITY
        if Mv1<-10 or Mv1>10:
            error_message()
            canvas.update()
            disable_Mbuttons()
            Mstop='break'
        canvas.delete('Mlabels')
        create_Mlabels()
        canvas.update()
    except:
        error_message()
        canvas.update()
        disable_Mbuttons()
        Mstop='break'
def get_velocityB():
    global Mv2,Mstop
    try:
        Mv2=float(velocityBinput.get())
        #VALIDATING THE RANGE OF THE VELOCITY
        if Mv2<-10 or Mv2>10:
            error_message()
            canvas.update()
            disable_Mbuttons()
            Mstop='break'
        canvas.delete('Mlabels')
        create_Mlabels()
        canvas.update()
    except:
        error_message()
        canvas.update()
        disable_Mbuttons()
        Mstop='break'
def get_cor():
    global Me,Mstop
    try:
        Me=float(corinput.get())
        #VALIDATING THE RANGE OF THE COR
        if Me<0 or Me>1:
            error_message()
            canvas.update()
            disable_Mbuttons()
            Mstop='break'
        canvas.delete('Mlabels')
        create_Mlabels()
        canvas.update
    except:
        error_message()
        canvas.update()
        disable_Mbuttons()
        Mstop='break'
#CREATING EACH BALL WITH A CERTAIN VELOCITY
def create_ballA(velocity):
    global Mx1,Mv1
    canvas.create_oval(Mx1-20,480,Mx1+20,520, fill='black', tags='balla')
    Mx1=Mx1+velocity
    if Mx1<20 or Mx1>1180:
        Mx1=Mx1-velocity
        Mv1=-Mv1
        create_ballA(Mv1) 
def create_ballB(velocity):
    global Mx2,Mv2
    canvas.create_oval(Mx2-20,480,Mx2+20,520, fill='black', tags='ballb')
    Mx2=Mx2+velocity
    #THIS IS TO CHECK THEY DONT COLLIDE WITH THE WALLS
    if Mx2<20 or Mx2>1180:
        Mx2=Mx2-velocity
        Mv2=-Mv2
        create_ballB(Mv2)        
#CHECKING IF A COLLISION HAS OCCURED
def collision_system():
    #CHECKING IF THE BALLS ARE WITHIN TWO RADII OF EACH OTHER
    if (((Mx2-Mx1)**2)**(1/2))<=40:
        #CALCULATING THE VELOCITIES AFTERWARDS
        restitution_calculator()
        create_ballA(Mv1)
        create_ballB(Mv2)
#CALCULATING THE VELOCITIES AFTER A COLLISION
def restitution_calculator():
    global Mv1,Mv2
    initialv1=Mv1
    Mv1=(Mm1*Mv1+Mm2*Mv2+Mm2*Me*(Mv2-Mv1))/(Mm1+Mm2)
    Mv2=(Mm1*initialv1+Mm2*Mv2+Mm1*Me*(initialv1-Mv2))/(Mm1+Mm2)
#-------------------------------------------------------------------------------
#THE INITIALISING PROCEDURE STARTED WHEN THE USER CLICKS THE MOMENTUM START BUTTON
def __init2__():
    global pause,menupause2,Mstop
    #DISABLE ALL ACTION BUTTONS
    disable_Mbuttons()
    #ENABLING THE PAUSE BUTTON
    pausebutton.config(state=ACTIVE)
    #DISABLING THE RESET BUTTON SO IT CAN NOT BE PRESSED WHEN YOU PRESS START THEN PAUSE THEN START 
    resetbutton.config(state=DISABLED)
    pause='no'
    menupause2='no'
    #MENUPAUSE AND PAUSE ARE USED BECAUSE IF ITS PAUSED YOU WANT TO SEE THE BALLS
    #BUT NOT IF THE MENU BUTTON IS PRESSED
    while Mx1>=0 and Mx1<=1200 and Mx2>=0 and Mx2<=1200 and menupause2!='yes' and Mstop!='break':
        try:
            create_ballA(Mv1)
            create_ballB(Mv2)
            create_Mlabels()
            if pause=='yes':
                startbutton.config(state=ACTIVE)
                resetbutton.config(state=ACTIVE)
                pausebutton.config(state=DISABLED)
                break
            collision_system()
            canvas.update()
            canvas.delete('balla')
            canvas.delete('ballb')
        except:
            error_message()
            disable_Mbuttons()
            resetbutton.config(state=ACTIVE)
            Mstop='break'
#----------------------------------------------------------------------------------------------------
#SIMPLE HARMONIC MOTION
#----------------------------------------------------------------------------------------------------
#CREATE THE INFO TEXT
def create_Stext():
    global menupause3
    menupause3='yes'
    canvas.delete('all')
    back_button=Button(canvas, text="Back", command=reset_canvas3)
    back_button.configure(width=10, activebackground="white")
    back_button_window=canvas.create_window(1150,580,window=back_button)
    Sline=10
    for s in range(0,49):
        datacontents=(shmlist[s])[0:-1]
        canvas.create_text(10,Sline,text=datacontents,font=("Arial", 10, "bold"),anchor=NW)
        Sline+=10
#GET THE VALUES OF THE SLIDER
def getmass(scale):
    global Sm
    Sm=float(scale)
def getk(scale):
    global Sk
    Sk=float(scale)
def getamplitude(scale):
    global SA
    SA=float(scale)
#----------------------------------------------------------------------------------------------------
#SHM INITIALISER
def __init3__():
    global menupause3
    menupause3='no'
    reset_basevars()
    #CREATE TITLE
    canvas.create_text(600,30,text="Simple Harmonic Motion Simulator",font=("Arial", 15, "bold"))
    #PHYSICAL VARIABLES
    originxmass=500
    originymass=300
    time=0
    #CREATE THE INFO BUTTON
    databutton=Button(canvas,text="Information",command=create_Stext)
    databutton.configure(width=10, activebackground="white")
    databutton_window=canvas.create_window(1150,580,window=databutton)
    #CREATE THE MENU BUTTON
    menubutton=Button(canvas,text="MENU",command=menu)
    menubutton.configure(width=10,activebackground="white")
    menubutton_window=canvas.create_window(1100,10,anchor=NW,window=menubutton)
    #CREATE THE SLIDERS
    massbar=ttk.Scale(window,from_=1,to=10,orient="vertical",command=getmass)
    canvas.create_window((700,150), window=massbar)
    kbar=ttk.Scale(window,from_=0.1,to=5,orient="vertical",command=getk)
    canvas.create_window((850,150), window=kbar)
    amplitudebar=ttk.Scale(window,from_=100,to=280,orient="vertical",command=getamplitude)
    canvas.create_window((1000,150), window=amplitudebar)
    canvas.create_text(700,85,text="Mass",font="Arial")
    canvas.create_text(850,85,text="Spring constant",font="Arial")
    canvas.create_text(1000,85,text="Amplitude",font="Arial")
    #CONTINUITY VARIABLE
    Sstop='no'
    #WORK OUT THE TOP OF THE SPRING AND PUT A BOBBLE
    maximum=originymass
    canvas.create_rectangle(originxmass-10,maximum-10,originxmass+10,maximum+10,fill='black')
    while Sstop=='no' and menupause3!='yes':
        #DISPLACEMENT AND ANGLE
        y=originymass+SA*math.sin(math.radians((Sk/Sm)**(1/2)*time))
        Stheta=math.degrees(math.radians((Sk/Sm)**(1/2)*time))
        Stheta=Stheta%360
        #CIRCLE
        canvas.create_arc(150,150,250,250,start=90-Stheta,extent=Stheta,tags='SHM')
        canvas.create_arc(150,150,250,250,start=(90-(360-Stheta))+(360-Stheta),extent=360-Stheta,tags='SHM')
        #AXI
        canvas.create_line(130,200,270,200,tags='SHM')
        canvas.create_line(200,130,200,270,tags='SHM')
        #LABELS
        canvas.create_text(300,200,text=('Position'),tags='SHM',font="Arial")
        canvas.create_text(200,120,text=('Velocity'),tags='SHM',font="Arial")
        #VARIABLES
        canvas.create_text(700,300,text=('=',str(round(Sm,2))),tags='SHM',font="Arial 20")
        canvas.create_text(850,300,text=('=',str(round(Sk,2))),tags='SHM',font="Arial 20")
        canvas.create_text(1000,300,text=('=',str(round(SA,2))),tags='SHM',font="Arial 20")
        #THE MASS AND SPRING
        canvas.create_oval(originxmass-20,y-20,originxmass+20,y+20,tags='SHM',fill='Black')
        canvas.create_line(originxmass,maximum,originxmass,y-20,dash=(4,4),tags='SHM')
        canvas.create_line(originxmass-40,originymass,originxmass+40,originymass,dash=(4,4),tags='SHM')
        canvas.create_text(100,120,text=('Angle='+str(int(Stheta))),tags='SHM',font="Arial")
        canvas.update()
        canvas.delete('SHM')
        time+=0.5
#----------------------------------------------------------------------------------------------------
#ORBITS
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#CREATING TEXT
def create_Otext():
    global menupause4
    menupause4='yes'
    canvas.delete('all')
    back_button=Button(canvas, text="Back", command=reset_canvas4)
    back_button.configure(width=10, activebackground="white")
    back_button_window=canvas.create_window(1150,580,window=back_button)
    Oline=10
    for o in range(0,25):
        datacontents=(orbitlist[o])[0:-1]
        canvas.create_text(10,Oline,text=datacontents,font=("Arial", 10, "bold"),anchor=NW)
        Oline+=20
#CREATE THE LABELS
def create_Olabels():
    global Oe,Oa,Ov
    canvas.create_text(40,90,text='='+str(round(Oe,3)),tags='Olabels',font="Arial 15")
    canvas.create_text(140,90,text='='+str(round(Oa,3)),tags='Olabels',font="Arial 15")
    canvas.create_text(240,90,text='='+str(round(Ov,3)),tags='Olabels',font="Arial 15")
#CREATING THE BUTTONS
def configure_Obuttons():
    #ENTRY BOXES FOR e,r,v
    ebox=ttk.Entry(window, textvariable=Oeinput)
    ebox.configure(width=11)
    ebox_window=canvas.create_window(10,10,anchor=NW,window=ebox)
    getebtn=Button(canvas, text='Eccentricity', command=get_oe)
    getebtn.configure(width=10, activebackground="white")
    getebtn_window=canvas.create_window(10,40,anchor=NW,window=getebtn)
    abox=ttk.Entry(window, textvariable=Oainput)
    abox.configure(width=11)
    abox_window=canvas.create_window(110,10,anchor=NW,window=abox)
    getabtn=Button(canvas, text='Semi-Major', command=get_oa)
    getabtn.configure(width=10, activebackground="white")
    getabtn_window=canvas.create_window(110,40,anchor=NW,window=getabtn)
    vbox=ttk.Entry(window, textvariable=Ovinput)
    vbox.configure(width=11)
    vbox_window=canvas.create_window(210,10,anchor=NW,window=vbox)
    getvbtn=Button(canvas, text='Speed', command=get_ov)
    getvbtn.configure(width=10, activebackground="white")
    getvbtn_window=canvas.create_window(210,40,anchor=NW,window=getvbtn)
    #CREATE THE INFO BUTTON
    databutton=Button(canvas,text="Information",command=create_Otext)
    databutton.configure(width=10, activebackground="white")
    databutton_window=canvas.create_window(1100,560,anchor=NW,window=databutton)
    #CREATE THE MENU BUTTON
    menubutton=Button(canvas,text="MENU",command=menu)
    menubutton.configure(width=10,activebackground="white")
    menubutton_window=canvas.create_window(1100,10,anchor=NW,window=menubutton)
    #CREATE THE RESET BUTTON
    resetbutton=Button(canvas,text="RESET",command=reset_canvas4)
    resetbutton.configure(width=10,activebackground="white")
    resetbutton_window=canvas.create_window(1000,10,anchor=NW,window=resetbutton)
#GETTING THE ECCENTRICITY
def get_oe():
    global Oe,Ostop
    try:
        Oe=float(Oeinput.get())
        if Oe<0 or Oe>1:
            error_message()
            canvas.update()
            Ostop='break'
        canvas.delete('Olabels')
        create_Olabels()
        canvas.update()
    except:
        Ostop='break'
        create_Olabels()
        error_message()
        canvas.update()
        canvas.delete('error')  
#GETTING THE RADIUS
def get_oa():
    global Oa,Ostop
    try:
        Oa=float(Oainput.get())
        if Oa<10 or Oa>300:
            error_message()
            canvas.update()
            Ostop='break'
        canvas.delete('Olabels')
        create_Olabels()
        canvas.update()
    except:
        Ostop='break'
        create_Olabels()
        error_message()
        canvas.update()
        canvas.delete('error')
#GETTING THE VELOCITY
def get_ov():
    global Ov,Ostop
    try:
        Ov=float(Ovinput.get())
        if Ov<0 or Ov>32:
            error_message()
            canvas.update()
            Ostop='break'
        canvas.delete('Olabels')
        create_Olabels
        canvas.update()
    except:
        Ostop='break'
        create_Olabels()
        error_message()
        canvas.update()
        canvas.delete('error')
#PROCEDURE TO CREATE SATELLITE
def create_satellite(theta):
    #theta is the starting angle, the direction is 1 or -1, 
    global r
    #CREATING ORIGIN
    canvas.create_oval(596,296,604,304, fill='black', tags='Osatellite')
    #SWITCHES THE DIRECTION OF THE SATELLITE IF STATED AND CHECKS BY FINDING THE MOD
    Odirection=Ov/(((Ov)**2)**(1/2))
    if Odirection==-1:
        theta=-theta
    #FIND THE DISTANCE TO THE SATELLITE FOR THE NEW ANGLE
    r=orbitalequation(theta,Oe,Oa)
    #CONVERTS THIS TO CARTESIAN COORDINATES TO BE DISPLAYED
    x,y=polartocartesian(r,theta)
    #CENTERS THEM
    x=x+600
    y=y+300
    #CREATES THE SATELLITE AND UPDATES
    canvas.create_oval(x-10,y-10,x+10,y+10, fill='black', tags='Osatellite')
    canvas.update()
    #FINDS THE DELAY THAT THE SYSTEM SHOULD WAIT
    delay=find_delay(r)
    #SLEEPS THAT DELAY
    time.sleep(delay)
#ORBITAL EQUATION TO FIND DISTANCE FROM GIVEN ANGLE
def orbitalequation(theta,e,a):
    #THE EQUATION TAKES THE ANGLE, ECCENTRICITY AND SEMI MAJOR AXIS TO FIND THE DISTANCE TO THE SATELLITE
    r=a*(1-e**2)/(1+e*math.cos(math.radians(theta)))
    return r
#FINDING DELAY TO CREATE ILLUSION OF A REAL ORBIT
def find_delay(r):
    global diminisher,Ov
    diminisher=31104000*Ov
    delay=r**2/diminisher
    delay*=100
    return delay
#SELF DEFINING
def cartesiantopolar(x,y):
    r=(x**2+y**2)**(1/2)
    theta=math.degrees(math.atan(y/x))
    return r,theta
#SELF DEFINING
def polartocartesian(r,theta):
    x=int(math.ceil(r*math.cos(math.radians(theta))))
    y=int(math.ceil(r*math.sin(math.radians(theta))))
    return x,y
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