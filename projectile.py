def reset_basevars():
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
    return Pstop,Px,Pg,Pangle,PangleDeg,Pv
