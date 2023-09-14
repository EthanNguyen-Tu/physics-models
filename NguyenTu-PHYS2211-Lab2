GlowScript 3.0 VPython
## PHYS 2211 Online
## Lab 2: Motion of a Falling Object
## @file NguyenTu-PHYS2211-Lab2.py
## @student Ethan Nguyen-Tu
## @updated 2023-02-5 EAM


## =====================================
## VISUALIZATION & GRAPH INITIALIZATION
## =====================================

scene.background = color.white

visualScale = .3 # scalar for size of visuals
# Visualization (object, trail, origin)
ball = sphere(color=color.blue, radius=0.22*visualScale)
trail = curve(color=color.green, radius=0.02*visualScale)
origin = sphere(pos=vector(0,0,0), color=color.yellow, radius=0.04*visualScale)

# Arrows to represent vector quantities in the visualization window
gravArrow = arrow(pos=ball.pos, axis=vector(0,0,0), color=color.orange)
dragArrow = arrow(pos=ball.pos, axis=vector(0,0,0), color=color.cyan)

# Graphing (if needed, you can add more plot and curve lines)
plot = graph(title="Position vs Time", xtitle="Time (s)", ytitle="Position (m)")
poscurve = gcurve(color=color.green, width=4)
plot = graph(title="Velocity vs Time", xtitle="Time (s)", ytitle="Velocity (m/s)")
velcurve = gcurve(color=color.green, width=4)


## =======================================
## SYSTEM PROPERTIES & INITIAL CONDITIONS 
## =======================================

# System Mass
ball.m = 0.005 # approximate kg mass of standard A4 printer paper

# Initial Conditions
ball.pos = vector(0,0.000648,0)
ball.vel = vector(0,0,0)
#ball.vel = vector(0,-1,0) # What if? V_i = -1

# Time
t = 0             # where the clock starts
deltat = 0.016700 # size of each timestep


# Interactions
# Magnitude of the acceleration due to gravity near Earth's surface
g = 9.8

# Unit vector for the positive y axis (pointing up)
jhat = vector(0,1,0)

# Proportionality constant for the magnitude of the drag force
#b = 0    # gravity only, no air resistance
b = 0.002 # gravity & air resistance (drag)
# b chosen to align the prediction with the final recorded observation


## ======================================
## CALCULATION LOOP
## (motion prediction and visualization)
## ======================================

while t < 0.267000: #1.5: # time of last observation
    # Controls how fast the program runs (larger number runs faster)
    rate(20)
    
    # Net Force on the Paper Ball Calculation
    Fgrav = vector(0,-ball.m*g,0) # F_Gravity (mg (-jhat))
    Fdrag = vector(0,b*mag(ball.vel)**2,0) # F_Drag (proportional to square of speed)
    Fnet = Fgrav + Fdrag

    # Apply the Momentum Principle (Newton's 2nd Law)
    # Update the object's velocity
    ball.vel = ball.vel + Fnet/ball.m*deltat
    # Update the object's position
    ball.pos = ball.pos + ball.vel*deltat
    
    # Advances the clock
    t = t + deltat
    # Updates the object's track
    trail.append(pos=ball.pos)

    # Plots position and velocity as a function of time
    poscurve.plot(t,ball.pos.y)
    velcurve.plot(t,ball.vel.y)

    # Draws arrows to represent forces
    arrowscale = 50 * visualScale # scalar for vector arrows' size
    gravArrow.pos = ball.pos
    gravArrow.axis = Fgrav * arrowscale
    dragArrow.pos = ball.pos
    dragArrow.axis = Fdrag * arrowscale

    # Displays the time, y position, and y velocity values to the console
    print(t + " , " + ball.pos.y + " , " + ball.vel.y)

print("FIN")
