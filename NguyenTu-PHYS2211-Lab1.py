GlowScript 3.0 VPython
## PHYS 2211 Online
## Lab 1: Constant Velocity
## @file NguyenTu-PHYS2211-Lab1.py
## @student Ethan Nguyen-Tu
## @updated 2021-01-29


## =====================================
## VISUALIZATION & GRAPH INITIALIZATION
## =====================================

scene.background = color.white # Makes Background White

# Visualization (object, trail, origin)
ball = sphere(color=color.blue, radius=0.022)
trail = curve(color=color.green, radius=0.002)
origin = sphere(pos=vector(0,0,0), color=color.yellow, radius=0.01)

# Graphs:
# Positon-Time Graph
plot = graph(title="Position vs Time", xtitle="Time (s)", ytitle="Position (m)")
poscurve = gcurve(color=color.green, width=4)
# Velociy-Time Graph
plot = graph(title="Velocity vs Time", xtitle="Time (s)", ytitle="Velocity (m/s)")
velcurve = gcurve(color=color.green, width=4)


## =======================================
## SYSTEM PROPERTIES & INITIAL CONDITIONS 
## =======================================

# System Mass
ball.m = 0.022680

# Initial Conditions
ball.pos = vector(0,-0.001739,0)
ball.vel = vector(0,-0.409877,0) 
# Observed's Avg. Veloctiy = 0.409877
# Observed's Initial Velocity = 0.380068

# Time
t = 0               # where the clock starts
deltat = 0.016667   # size of each timestep


## ======================================
## CALCULATION LOOP
## (motion prediction and visualization)
## ======================================

while t < 0.616667:
    rate(100) # How Fast the Program Runs (Larger = Faster)
    
    Fnet = vector(0,0,0) # Net Force
    
    # Apply the Momentum Principle & Newton's 2nd Law
    # F = ma ; a = delta(v)/delta(t)
    # Fnet = delta(p)/delta(t) ; p = mv
    
    # Updates the object's velocity
    ball.vel = ball.vel + (Fnet*deltat)/ball.m
    # Updates the object's position
    ball.pos = ball.pos + ball.vel*deltat
    
    # Advance the clock
    t = t + deltat
    # Update the object's track
    trail.append(pos=ball.pos)
    
    # Plot position and velocity as a function of time
    poscurve.plot(t,ball.pos.y)
    velcurve.plot(t,ball.vel.y)
    
    # Displays the time, position, and velcoity values to the console
    # Formatted for easy transfer to Google Sheets
    print(t + " , " + ball.pos.y + " , " + ball.vel.y)
    
print("All done!")

    # Format for easy reading:
    #print("Time:" + t + "\nPosition:" + t,ball.pos.y 
    #      + "\nVelocity:" + t,ball.vel.y + "\n")
