Web VPython 3.2
""" SUMMER 2023 PHYS 2212 EXPERIMENT 0
Calculating and Displaying the Electric Field of a Single Charged Particle

@author Ethan Nguyen-Tu
@date 21 May 2023
"""

#= CONTANTS
oofpez = 9e9 # One Over Four Pi Epsilon-Zero
qproton = 1.6e-19 # Charge of a Proton
#print(oofpez) # Typed correctly check

ef_scalefactor = 1/1.6e20 # Electric field representation scale factor


#= VARIABLES & INITIAL VALUES
# Location of Observation
obslocation = vec(3.1e-10, -2.1e-10,0) # Where to find the Electric Field


#= GRAPHICS

#== Objects
#=== Background
scene.background = color.white

#=== Positively Charged Proton
particle = sphere(pos=vec(1e-10,0,0), radius=2e-11) # Proton
particle.charge = -qproton # Charge
particle.color = color.red if particle.charge > 0 else color.blue

#=== Locaiton of Observation
#obslocation_rep = sphere(pos=obslocation, radius=1e-11, color=color.yellow)


#= FUNCTIONS
"""
Calculates the relative position vector.

For calculating the electric field at an observation location, the relative 
position vector always points from the source particle (the initial location) 
to the observation location (the final location).

@param particle Vector particle location
@returns Vector relative position
"""
def calc_r(obs, source):
    return obs - source
    
"""
Calculates the magnitude of a 3-coordinates vector with the equation for the 
magnitude of a 3-coordinates vector.

@param r Vector relative position that has 3 coordinates
@returns Scalar magnititude of the passed in R vector
"""
def calc_r_mag(r):
    return sqrt(r.x**2 + r.y**2 + r.z**2)

"""
Calculates the directional unit vector of the relative position vector through 
rearranging the definition for a vector, vector = magnitude * direction, to get 
direction = vector / magnitude.

@param r Vector relative position that has 3 coordinates
@returns Vector unit vector of the relative position vector
"""
def calc_r_hat(r):
    return r / calc_r_mag(r)

def Efield(chargedParticle, observationLocation):
    q = chargedParticle.charge
    r = observationLocation - chargedParticle.pos
    E = oofpez * q / calc_r_mag(r)**2 * calc_r_hat(r)
    return E


#= CALCULATIONS

#== Relative Position Vector
# Vector
r = calc_r(obslocation, particle.pos)
print("The relative position vector is r=", r)

# Arrow Representation
ra = arrow(pos=particle.pos, axis=r, color=color.green)

# Magnitude
rmag = calc_r_mag(r)
print("The magnitude of r is |r|=", rmag)

# Direction
rhat = calc_r_hat(r)
print("The unit vector is rhat=", rhat)

#== Electric Field Vector
# Vector
E = oofpez * particle.charge / rmag**2 * rhat
print("The electric field vector is E=", E)

# Arrow Representation
print("The magnitude of E is |E|=", calc_r_mag(E))
ea = arrow(pos=obslocation, axis=ef_scalefactor*E, color=color.orange)

# Additional Observation Locations
obslocations_newdirections = [vec(0,1,0), vec(0,-1,0), vec(1,0,0),
                              vec(-1,0,0), vec(0,0,1), vec(0,0,-1)]

for direction in obslocations_newdirections:
    new_pos = particle.pos + (3e-10 * direction)
    new_E = Efield(particle, new_pos)
    
    # New Arrow Representation
    new_ea = arrow(pos=new_pos, axis=ef_scalefactor*new_E, color=color.orange)

