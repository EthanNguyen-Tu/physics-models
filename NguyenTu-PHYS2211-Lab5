GlowScript 3.0 VPython
$## PHYS 2211 Online
## Lab 5: Slinky Drop
## @file NguyenTu_PHYS2211-Lab5.py
## @author Ethan Nguyen-Tu
## @updated 16 April 2023


## =============================================================================
## CALCULATION FUNCTIONS
## =============================================================================
"""
Calculates the spring force acting on an object at the obs end of the spring.

@param obs Objec
@returns Vector of the force of the sprign
"""
def calc_f_spring(obs,source):
    L = obs - source
    L_hat = L / mag(L)
    return - k_s * (mag(L) - L_0 / num_pms) * L_hat

"""
Calculates the center of mass of the given objects.

@param objects Array containing the objects we are calculating the center of mass of
@returns Vector position of the center of mass
"""
def calc_com(objects):
    tot_mass = 0
    weighted_pos = vector(0,0,0)
    for object in objects:
        tot_mass += object.m
        weighted_pos += object.m * object.pos
    return weighted_pos/tot_mass
    
"""
Calculates the final velocity of two objects after an inelastic collision.

@param m1 Scalar mass of object 1 in kg
@param v1 Vector velocity of object 1 in m/s
@param m2 Scalar mass of object 2 in kg
@param v2 Vector velocity of object 2 in m/s
@returns Vector final velocity of the combined objects after the collision in m/s
"""
def inelastic_collision(m1, v1, m2, v2):
    # Calculates the total mass and momentum before collision
    tot_mass = m1 + m2
    tot_momentum = m1 * v1 + m2 * v2

    # Calculates the velocity of the combined objects after the collision
    v_f = tot_momentum / tot_mass

    # Return the final velocity
    return v_f


## =============================================================================
## SYSTEM PROPERTIES, INITIAL CONDITIONS, DATA
## =============================================================================
speed = 100  # How fast to run program

#=== Video Initial Conditions ===
camera_speed = 3.25*300  # Frames per second of the camera recording
t = 0  # seconds
deltat = 0.01666667  # video change in time
t_end = 8.7  # when the video ends

#=== Spring Info ===
tot_spring_m = 0.2155 # Source: Google
spring_coils = 86 # Source: Google
k_s = .87 # Slinky Bottom Point Mass => m * g = -k * s
L_0 = 0.058 # Source: Google

#=== Tracker Initial Conditions ===
# Origin
origin_pos = vector(0, 0, 0)
# Top of Spring
r_spring_top = vector(0.001542206, -0.002467529, 0)
# Bottom of Spring
r_spring_bot = vector(0.04133111, -1.265225, 0)
# Initial Spring Stretched Length
L_i = r_spring_bot - r_spring_top
# Spring at Rest
tot_spring_vel = vector(0, 0, 0)
# Ground Position
ground_pos = vector(0, -1.8, 0)

#=== Spring Into Segments Properties ===
# Number of Smaller Springs the Total Spring is Divided Into
num_pms = 10
k_s = k_s * num_pms
# Length of Each Smaller Spring
segment_len_i = 0.19425 * norm(L_i)

#=== Force Info ===
g = 9.8 * vector(0, -1, 0)  # downward effect of Earth's Gravity near its surface


## =============================================================================
## VISUALIZATION & GRAPH INITIALIZATION
## =============================================================================

#=== Scene ===
# Color of the background (black is default)
scene.background = color.white
# Scale Factor for Visualizations
scale = .25
# Camera Position
scene.camera.pos = (ground_pos - origin_pos) / 2 + vector(0, 0, 15)

#=== Objects ===
# Origin
origin = box(pos=origin_pos, size=scale * vector(1, .05, 0.01), color=color.yellow)
label(pos=origin.pos, size=scale * origin.size / 5, height=10, box=False, text="Origin")
# Ground
ground = box(pos=ground_pos, size=scale * vector(2.5, .05, 0.01), color=vector(0.5, 1, 0.5))
label(pos=ground.pos, size=scale * ground.size / 5, height=10, box=False, text="Ground")
# Create springs segments connected by point masses
springs = []  # array holding spring segments
pms = []  # array holding point masses

for i in range(num_pms):
    # Create Springs
    spring = helix(radius=scale * 0.02, coils=spring_coils / num_pms, color=color.blue)
    springs.append(spring)
    # Create Point Masses
    pm = sphere(radius=scale * 0.04, color=color.magenta)
    pms.append(pm)

pms[0].color = color.cyan  # Top of Slinky
pms[-1].color = color.red  # Bottom of Slinky

#=== Center of Mass ===
com = sphere(radius=scale * 0.06, color=color.green)

#=== Graphs ===
# y-position graph
yplot = graph(title="y-position vs time", xtitle="time (s)", ytitle="y-position (m)")
yposcurve = gcurve(color=color.blue, width=4, label="Slinky Top")
ypos2curve = gcurve(color=color.green, width=4, label="Center of Mass")
ypos3curve = gcurve(color=color.red, width=4, label="Slinky Bottom")


## =============================================================================
## CALCULATION LOOP
## =============================================================================

#= Assign Initial Conditions
#== Weighting Factors
initial_seg_length = .19425
a1 = .9

pms[0].pos = r_spring_top  # Top of Slinky
pms[1].pos = initial_seg_length * norm(L_i)
pms[-1].pos = r_spring_bot  # Bottom of Slinky

for i in range(num_pms):
    pms[i].m = tot_spring_m / num_pms
    pms[i].vel = tot_spring_vel  # initially at rest
    if i > 1:
        pms[i].pos = pms[i-1].pos + (pms[i-1].pos-pms[i-2].pos) * a1
    springs[i].pos = pms[i].pos
    springs[i].axis = pms[i - 1].pos - pms[i].pos

#= Calculate center of mass
com.pos = calc_com(pms)

#= Calculation Loop
while t < t_end:
    rate(speed)
    for i in range(num_pms):
        #=== Calculate Forces ===
        # Force due to gravity
        #if pms[i].pos.y > ground_pos.y:
        F_grav = pms[i].m * g
        #else:
            # Contact Force Negates Gravity When Spring Touches Ground
           # F_grav = vector(0, 0, 0)
        # Force due to spring
        F_spring_above = calc_f_spring(pms[i].pos, pms[i - 1].pos)
        if i != num_pms - 1:
            F_spring_below = calc_f_spring(pms[i].pos, pms[i + 1].pos)
        # Total Force
        F_net = (F_grav + F_spring_above + F_spring_below) / camera_speed


        #=== Momentum Principle (Newton's 2nd Law) ===
        # Update velocity and position of point mass
        pms[i].vel += F_net / pms[i].m * deltat

        # Check hits other point mass in spring
        if i != (num_pms - 1) and (pms[i].pos.y + pms[i].vel.y * deltat) <= (
                pms[i + 1].pos.y + L_0 / (num_pms + 1)):
            pms[i].vel = inelastic_collision(pms[i].m,pms[i].vel,pms[i+1].m,pms[i+1].vel)
            pms[i+1].vel = pms[i].vel
        else:
            pms[i].pos += pms[i].vel * deltat

        # Check hits ground
        if pms[i].pos.y <= ground_pos.y:
            pms[i].pos.y = ground_pos.y

    # Update Center of Mass
    prev_com_pos = com.pos
    com.pos = calc_com(pms)
    com.vel = (com.pos-prev_com_pos)/deltat
    
    # Update spring positions
    for i in range(num_pms):
        springs[i].pos = pms[i].pos
        springs[i].axis = pms[i - 1].pos - pms[i].pos
        
    #=== Graphs ===
    # Plot y position v time
    yposcurve.plot(t, pms[0].pos.y)
    ypos2curve.plot(t, com.pos.y)
    ypos3curve.plot(t, pms[-1].pos.y)


    # Update Time
    t += deltat
