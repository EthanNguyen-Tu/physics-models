GlowScript 3.0 VPython

""" SUMMER 2023 PHYS 2212 EXPERIMENT 4 - Magnetic Braking with Faraday
Simulation of a bar magnet being dropped through a conductive tube with the bar 
magnet modeled as a point dipole and the conductive tube modeled as a stack of 
non-interacting conductive rings.

Surroundings: Aluminum Foil Tube & Earth
System: Magnet

@author Ethan Nguyen-Tu
@date 16 July 2023
"""

#===============================================================================
# PHYSICAL CONSTANTS
#===============================================================================
u0over4pi = 1e-7
resistivity = 2.65e-8   # resistivity of aluminum, in ohm-meters
g = 9.81



#===============================================================================
# GRAPH INITIALIZATION
#===============================================================================
plot = graph(title="Velocity vs Time", xtitle="Time (s)",
             ytitle="Velocity (m/s)")
poscurve = gcurve(color=color.black, width=2)



#===============================================================================
# CREATING THE TUBE OF ALIMUMIM FOIL 
#===============================================================================
#= Tube Geometry
L = 0.305                   # Length of tube (m) | 1 ft
width = 0.009               # Width of foil (m) | 0.9 cm
inner_rad = 0.015           # Inner radius of tube (m) | 3 cm cardboard diameter
rad = width + inner_rad     # radius (center to outer surface)
print(rad)

#= Numerical parameters of the simulation
dy = 0.005                  # vertical thickness of each tube segment
Nlength = round(L/dy)       # total number of tube segments
gridstep = 0.001            # distance between elements of flux surface
deltat = 0.001              # timestep
dropStep = 0.001            # distance used to calculate B gradient
entered = False             # detects when the magnet enters the tube 
exited = False              # detects when the magnet exits the tube


# Creating the tube of aluminum foil as a series of rings stacked along the 
# y-axis, which is perpendicular to the plane of each ring, and passes through
# the center of each ring.
tube = []
for i in range(Nlength):
    thisSegment = extrusion(path=[vector(0,-(i*dy),0),vector(0,-(1+i)*dy,0)], 
                            shape=shapes.circle(radius=rad,thickness=width/rad))
    thisSegment.current = 0     # CW from above defined as positive
    thisSegment.flux = 0
    thisSegment.radius = rad-width
    thisSegment.R = resistivity*(2*pi*thisSegment.radius)/(width*dy)
    tube.append(thisSegment)
print("Tube created")



#===============================================================================
# CREATING THE BAR MAGNET
#===============================================================================
#= Properties of the magnet
mass = 0.023                # mass (kg) 
mu_mag = 3.08005813066      # magnitude of magnetic dipole moment (from lab 3)

#= Visualizing the bar magnet
bar = cylinder(pos=vector(0,0.0,0), axis=vector(0,0.025,0), radius=0.0065)
bar.mu = mu_mag * bar.axis/mag(bar.axis)    # dipole points along magnet's axis
mu_hat = bar.mu/mag(bar.mu)  



#===============================================================================
# INITIAL CONDITIONS
#===============================================================================
bar.vel = vector(0,0,0)
t = 0



#===============================================================================
# Functions
#===============================================================================
'''
Calculates the magnetic field of a bar magnet.

@param mu Vector magnetic dipole moment
@param r Vector position 
'''
def dipoleB(mu, r):
    rmag = mag(r)
    rhat = norm(r)
    B = u0over4pi * ((3 * dot(mu,rhat) * rhat) - mu) / rmag**3
    return B

'''
Calculate dFlux/dt through each ring due to the falling magnet.

@param magnet Cylinder that represents the magnet
@param ring Extrusion ring that represents a segment of the aluminum foil tube
'''
def calculateDFluxDtAnalytic(magnet, ring):
    rad_ring = ring.radius
    distance = ring.pos.y - bar.pos.y
    speed = mag(bar.vel)
    numerator = (3/2) * (4*pi) * u0over4pi * mag(bar.mu) * distance * speed \
                * rad_ring**2
    denominator = (rad_ring**2 + distance**2)**(5/2)
    dFdt = numerator / denominator
    return(dFdt)

'''
Helps create the model key.

@param entry String label of the key entry
@param entry_color Vector color of the entry
@param list_num Integer position of the entry in the key
'''
def create_key_entry(entry="<b>-- Key --</b>", 
                     entry_color=color.black,list_num=0):
    label(pixel_pos=True, box=False, opacity=0, color=entry_color,
          pos=vec(10,scene.height,0)-(list_num+1)*vec(0,20,0), 
          text=entry, align="left")



#===============================================================================
# GRAPHICS
#===============================================================================
#= Scene
scene.background = color.gray(0.75) # make the scene background slightly gray
scene.camera.pos = scene.camera.pos - vector(0,width/(3*rad),
                                             scene.camera.pos.z/3)

#= Model Key
create_key_entry() # initializes key
create_key_entry("Bar Magnet", bar.color, 1)
create_key_entry("Aluminum Foil Tube", color.black, 2)
create_key_entry("Counter-clockwise Current", color.red, 3) # Lenz's Law
create_key_entry("Clockwise Current", color.blue, 4)        # Lenz's Law



#===============================================================================
# SIMULATION LOOP
# (motion prediction and visualization)
#===============================================================================
while bar.pos.y >= -L:  # let the magnet drop out instead of stopping at -L
    rate(1000)          # how fast the simulation runs (larger = faster)
    
    t = t + deltat
    
    if not entered:
        if bar.pos.y <= tube[0].pos.y:
            enterTime = t
            entered = True
    
    if not exited:
        if bar.pos.y <= tube[-1].pos.y:
            exitTime = t
            exited = True
      
    Fgrav = vector(0,-mass*g,0) # gravitational force on the magnet

    #= Calculating the magnetic force from the tube on the magnet
    magF_on_magnet = 0
    for ring in tube:
        
        #== Computing dflux/dT for ring due to falling magnet
        dFluxdt = calculateDFluxDtAnalytic(bar, ring)    
        
        ring.current = -dFluxdt/ring.R # current in the ring
        
        #== Coloring each ring according to current
        if ring.current > 0:
            ring.color = vector(1e-1*abs(ring.current)+0.3,0.3,0.3)
        else:
            ring.color = vector(0.3,0.3,1e-1*abs(ring.current)+0.3)
        
        r_ring = vector(ring.radius,ring.pos.y-bar.pos.y,0) 

        #== "Typical" B-field at each ring
        # The magnetic field is assumed to be axisymmetric
        B_at_ring = dipoleB(bar.mu, r_ring)
        Bhat = B_at_ring/mag(B_at_ring)
        sintheta = mag(cross(mu_hat,Bhat))
        magF_on_ring = abs(2*pi*ring.current*ring.radius*mag(B_at_ring) \
                       *sintheta)

        magF_on_magnet = magF_on_magnet + magF_on_ring
        
    #== Calculating the magnetic force on the magnet 
    Fmagnetic = vector(0,magF_on_magnet,0)

    Fnet = Fgrav + Fmagnetic # Net force on magnet
    
    # Newton's Second Law - Assuming tube stays fixed
    bar.vel = bar.vel + (Fnet/mass) * deltat # Velocity Update Formula
    bar.pos = bar.pos + bar.vel * deltat     # Position Update Formula
    
    # Plotting a graph of velocity vs time for the magnet as it drops
    poscurve.plot(t,bar.vel.y)    
    
print("Time in tube (in seconds): ", exitTime - enterTime)
