GlowScript 3.0 VPython
## PHYS 2211 Online
## Lab 4: Oscillations
## @file NguyenTu_PHYS2211-Lab4.py
## @editor Ethan Nguyen-TuIn
## @updated 2 April 2023


## =====================================
## VISUALIZATION & GRAPH INITIALIZATION
## =====================================

scene.background = color.white

# Visualization (object, trail, origin/attachment point)
ball = sphere(radius=0.03, color=color.blue) 
trail = curve(color=ball.color)
origin = sphere(pos=vector(0,0,0), color=color.yellow, radius=0.015)  

# Creating the spring
spring = helix(color=color.cyan, thickness=0.006, coils=40, radius=0.015)
spring.pos = origin.pos

# Graphing
xplot = graph(title="x-position vs time", xtitle="time (s)", ytitle="x-position (m)")
xposcurve = gcurve(color=color.blue, width=4, label="model")
xpos2curve = gcurve(color=color.red, width=4, label="experiment")

yplot = graph(title="y-position vs time", xtitle="time (s)", ytitle="y-position (m)")
yposcurve = gcurve(color=color.blue, width=4, label="model")
ypos2curve = gcurve(color=color.red, width=4, label="experiment")

eplot = graph(title="Change in Energy vs Time", xtitle="Time (s)", ytitle="Change in Energy (J)") 
dKcurve = gcurve(color=color.blue, width=4, label="deltaK")
dUgcurve = gcurve(color=color.red, width=4, label="deltaUgrav")
dUscurve = gcurve(color=color.green, width=4, label="deltaUspring")
dEcurve = gcurve(color=color.orange, width=4, label="deltaE")

# Create object to visualize motion from video analysis
ball2 = sphere(radius=0.025, color=color.red) 



## ============================================
## SYSTEM PROPERTIES, INITIAL CONDITIONS, DATA 
## ============================================

# Import position data to visualize motion meaurements from video analysis
X = []
Y = []
obs = read_local_file(scene.title_anchor).text; 
for line in obs.split('\n'):
    if line != '':
        line = line.split(',')
        X.append(float(line[0]))
        Y.append(float(line[1]))
idx = 0  #variable used to select data from list.
cnt = 0 #variable to keep track of predictions made between each measurement

# System mass
ball.m = 0.402 # given in kg

#Initial Conditions
ball.pos = vector(-0.116,-0.640,0) # no z-coordinate movement
ball.vel = vector(0,0,0) # starts at rest

# Timing
t = 0
deltat = 1/210 # video change in time



## ========================================
## INTERACTION CONSTANTS, SPRING, ENERGIES
## ========================================

# Constant to calculate gravitational force near Earth's surface
g = 9.8

# Spring constant <= formula: 4 * π**2 * m / T**2
k_s = 6.83 # given

# Relaxed length of spring <= formula: mg = k(|L| - L0)
L0 = 0.123 # given

# Specifies the vector L (describes spring length and orientation)
L = ball.pos - spring.pos
Lhat = L / mag(L) # vector definition rearrangement: vector = magnitude * direction
s = mag(L) - L0   # spring stretch/compression

K = 0.5 * ball.m * mag(ball.vel)**2 # kinetic energy 
Ug = ball.m * g * ball.pos.y        # gravitational potential energy 
Us = 0.5 * k_s * s**2               # spring potential energy 
E = K + Ug + Us                     # total energy



## ===============================================================
## CALCULATION LOOP
## (motion prediction and visualization)
## (compare with measurements; check and verify energy principle)
## ===============================================================

while t < 9.5:         

    # Define initial energies
    K_i = K
    Ug_i = Ug
    Us_i = Us
    E_i = E
    
    # Calculate gravitational force
    Fgrav = ball.m * g * vector(0,-1,0)
    
    # Calculate spring force on mass by spring
    Fspring = -k_s * s * Lhat

    # Calculate the net force
    Fnet = Fgrav + Fspring

    # Apply the Momentum Principle (Newton's 2nd Law)
    # Update the object's velocity
    ball.vel = ball.vel + Fnet/ball.m * deltat # velocity update formula
    # Update the object's position
    ball.pos = ball.pos + ball.vel * deltat # position update for nonconstant force
    
    # Update the spring
    L = ball.pos - spring.pos
    Lhat = L / mag(L) # vector definition rearrangement: vector = magnitude * direction
    s = mag(L) - L0 # spring stretch/compression

    spring.axis = L
    trail.append(pos=ball.pos)

    # Calculate energy changes
    K = 0.5 * ball.m * mag(ball.vel)**2
    deltaK = K - K_i # delta/change = final - initial
    Ug = ball.m * g * ball.pos.y
    deltaUg = Ug - Ug_i
    Us = 0.5 * k_s * s**2
    deltaUs = Us - Us_i
    E = K + Ug + Us
    deltaE = E - E_i

    # Specify energy changes for plotting
    dKcurve.plot(t,deltaK)      # blue
    dUgcurve.plot(t,deltaUg)    # red
    dUscurve.plot(t,deltaUs)    # green
    dEcurve.plot(t,deltaE)      # orange
    
    # Plotting x position vs time, and y position vs time
    xposcurve.plot(t,ball.pos.x)
    yposcurve.plot(t,ball.pos.y)
    
    # Compare video analysis measurements to computational model prediction
    cnt=cnt+1
    while cnt > 19:
        idx = idx+1
        ball2.pos = vector(X[idx],Y[idx],0)
        xpos2curve.plot(t,ball2.pos.x)
        ypos2curve.plot(t,ball2.pos.y)
        cnt = 0

    # Update time
    t = t + deltat
    rate(500)

print("All done!")
