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
