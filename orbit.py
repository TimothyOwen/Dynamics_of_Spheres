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
#RESET CANVAS
def reset_canvas4():
    global menupause4
    #INDICATES THAT THE ACTIVE LOOP SHOULD STOP TO CREATE THE MENU
    menupause4='yes'
    #RESETTING EVERYTHING
    canvas.delete("all")
    reset_basevars()
    __init4__()
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