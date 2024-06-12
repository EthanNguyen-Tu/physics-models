Web VPython 3.2

""" SUMMER 2023 PHYS 2212 EXPERIMENT 2: Magnetic Field of a Bar Magnet
A computational model of a bar magnet's magnetic field.

@editor Ethan Nguyen-Tu
@date 28 May 2023
"""

# ==============================================================================
# PHYSICAL CONSTANTS
# ==============================================================================
u0over4pi = 1e-7


# ==============================================================================
# CREATING THE MAGNET AT THE ORIGIN
# ==============================================================================
magnet = cylinder(pos=vector(0,0.0,0), axis=vector(0.025,0,0), radius=0.0065)
muhat = magnet.axis/(mag(magnet.axis))

# Magnitude of the magnetic moment
mumag = 3.08005813066
magnet.mu = mumag*muhat


# ==============================================================================
# FUNCTION FOR THE MAGNETIC FIELD
# ==============================================================================
def dipoleB(mu, r):
    rmag = mag(r)
    rhat = norm(r)
    B = u0over4pi * rmag**-3 * ((3 * dot(mu,rhat) * rhat) - mu)
    return B


# ==============================================================================
# FUNCTION THAT HELPS CREATE THE MODEL KEY
# ==============================================================================
def create_key_entry(entry="<b>-- Key --</b>", entry_color=color.black,list_num=0):
    label(pixel_pos=True, box=False, opacity=0, color=entry_color,
          pos=vec(10,scene.height,0)-(list_num+1)*vec(0,20,0), 
          text=entry, align="left")


# ==============================================================================
# GRAPHICS
# ==============================================================================
#= Scene
scene.background = color.gray(0.75) # make the scene background slightly gray


#= VISUALIZING THE MAGNETIC FIELD: ON AXIS AND PERPENDICULAR TO THE AXIS
# Scaling the arrows so they fit on the screen
B_scale = 1000

# How far away from the origin (in meters) the arrows will be placed
distance = 0.2 # Changing shows field at different distances

# Observation locations: two on-axis, four perpendicular to the axis
obs = [vector(distance,0,0),   # on-axis
       vector(-distance,0,0),  # on-axis
       vector(0,distance,0),   # perpendicular
       vector(0,-distance,0),  # perpendicular
       vector(0,0,distance),   # perpendicular
       vector(0,0,-distance)]  # perpendicular

num_arrows = 0
for v in obs:
    B_arrow = dipoleB(magnet.mu, v) # magnetic field arrow
    num_arrows = num_arrows + 1
    if num_arrows < 3: # TWO arrows representing the magnetic field on-axis
        arrow(pos=v, color=color.orange, axis=B_scale*B_arrow)
        print("B_axis"+num_arrows+" = ", B_arrow)
    else: # FOUR arrows representing the magnetic field perpendicular to axis
        arrow(pos=v, color=color.cyan, axis=B_scale*B_arrow)
        print("B_perp"+num_arrows+" = ", B_arrow)


#= VISUALIZING THE MAGNETIC FIELD: 45 DEGREES OFF-AXIS
d_perp = 1.63E-01 # Average d_perp from Experiment Part 2
d = d_perp*sqrt(2)
print("d = ", d)

# Observation location at 45 degrees from the axis
obs_45deg = vector(d_perp,d_perp,0)

# Arrow to represent the magnetic field 45 degrees from the axis
r_45deg = obs_45deg
B_45deg = dipoleB(magnet.mu,r_45deg)
arrow(pos=obs_45deg, color=color.magenta, axis=B_45deg*B_scale)
print("B at 45deg at distance d = ", B_45deg)
print("Magnitude of B at 45deg at distance d = ", B_45deg.mag)


#= Model Key
create_key_entry() # initializes key
create_key_entry("45 Degrees Off-Axis", color.magenta, 1)
create_key_entry("Perpendicular to Axis", color.cyan, 2)
create_key_entry("Magnet", magnet.color, 3)
create_key_entry("On-Axis", color.orange, 4)


#= Scene Rotation
rotation_speed = 0.005
while True:
    rate(50)

    # Rotate the camera around the object
    scene.camera.pos = rotate(scene.camera.pos, angle=rotation_speed, 
                              axis=vector(0, 1, 0))
    scene.camera.axis = rotate(scene.camera.axis, angle=rotation_speed, 
                               axis=vector(0, 1, 0))
