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
