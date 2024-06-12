Web VPython 3.2

""" SUMMER 2023 PHYS 2212 EXPERIMENT 1 - Part 2: Lines of Charge
A computational model of two charged tapes, represented by lines of charges, to 
estimate the amount of charge on each tape necessary to float one above the 
other. The value fo Q found in part 1 is used as the starting point with the 
total charge in each tape evenly distributed across the length of the tape.

@editor Ethan Nguyen-Tu
@date 28 May 2023
"""

# ==============================================================================
# PHYSICAL CONSTANTS
# ==============================================================================
#= Coulomb's Constant
oofpez = 9e9 # One Over Four Pi Epsilon-Zero

#= Gravity Near Earth's Surface
g = 9.81 # m/s^2


# ==============================================================================
# OBSERVED VALUES
# ==============================================================================
#= Tape Length
utape_length = 0.19 # m

#= Distance between the top and bottom tapes
separation = 0.026 # m

#= Mass of one tape (in kg)
# GIVEN: mass of tape is 1 gram per meter of length = 0.001 kg per m length
M = utape_length * 1/1000 # =1.9e-4

diff_factor = 2.12183 # diff charge between part 1 and part 2

#= Estimated net charge on one tape (in C)
Q = diff_factor*1.18321e-8 # sqrt(M * g / oofpez * separation**2)


# ==============================================================================
# FUNCTION FOR THE ELECTRIC FIELD
# ==============================================================================
def Efield(chargedParticle,observationLocation):   
    r = observationLocation - chargedParticle.pos
    return oofpez * chargedParticle.charge / mag(r)**3 * r


# ==============================================================================
# FUNCTION THAT CREATES A LINE OF CHARGE
# ==============================================================================
def lineCharge(startPos, axis, mass, charge, N, color=color.red):
    # Creates a line of N uniform point charges with a given total charge and 
    # mass arranged at equal intervals on a line segment starting at startPos
    # and extending along axis
    line = []
    line.axis = axis
    line.pos = startPos
    spacing = axis/(N-1)   # vector separating adjacent charges
    q = Q/N     # magnitude of each point charge
    m = M/N     # mass of each point charge
    for ii in range(N):
        # There will be N point charges in this tape
        dq = sphere(pos=startPos+(ii*spacing), radius=mag(axis)/N, color=color)
        dq.charge = q
        dq.mass = m
        line.append(dq)
    return(line)
    

# ==============================================================================
# FUNCTION THAT HELPS CREATE THE MODEL KEY
# ==============================================================================
def create_key_entry(key_entry="<b>Key</b>",entry_color=color.black,list_num=0):
    entry = label(pixel_pos=True, box=False, opacity=0, color=entry_color,
                  pos=vec(10,scene.height,0)-(list_num+1)*vec(0,20,0), 
                  text=key_entry, align="left")


# ==============================================================================
# GRAPHICS - PART 1
# ==============================================================================
#= Scene
scene.background = color.gray(0.75) # make the scene background slightly gray

#= Line of Charge
num_points = 31 # How many point charges to make each line of charge

#= Tapes
# Modeled each tape as a point charges collection placed side-by-side in a line.
#== Tape Starting Position
# Centers the tapes in the scene
tape_pos_start=vector(-utape_length/2,-separation/2,0)
#== Tape Above
TopTape = lineCharge(startPos=tape_pos_start+vector(0,separation,0), 
                     axis=vector(.2,0,0), mass=M, charge=Q, 
                     N=num_points, color=color.magenta)
#== Tape Below
BottomTape = lineCharge(startPos=tape_pos_start, 
                        axis=vector(.2,0,0), 
                        mass=M, charge=Q, N=num_points, color=color.red)

#= Vector Arrows' Scale Factors
E_scale = 1/num_points     # arrowscale for electric field vector arrows
F_E_scale = 2*num_points   # arrowscale for electric force arrow
F_G_scale = F_E_scale      # arrowscale for gravity force arrow

#= Location of the F_E and F_G arrows
# Tails of the arrows placed in the middle of TopTape
middleTop = TopTape.pos + 0.5*TopTape.axis
                    

# ==============================================================================
# CALCULATING THE ELECTRIC FIELD AND THE ELECTRIC FORCE
# (E is the electric field at the location of TopTape produced by BottomTape,
# and F_E is the electric force on TopTape due to BottomTape)
# ==============================================================================

# WHAT IS HAPPENING HERE: 
# Each tape is simulated as a line of point charges (dq's). TopTape is the 
# system, BottomTape is part of the surroundings. At the location of each dq in 
# TopTape, there is an electric field produced by the collection of charges that
# make up BottomTape. We will create N arrows for these electric field vectors,
# placing their tails at each dq in TopTape. We will calculate the electric 
# force on TopTape due to BottomTape (F_E_on_top) by adding up the forces from
# each dq in BottomTape as they interact with each dq in TopTape. 

# Important: we ignore interactions between the dq's within each separate tape.

F_E_on_top = vector(0,0,0) # net electric force on TopTape initialized at zero

for dq_top in TopTape:  # iterate through each piece of charge in TopTape
    E_at_dq_top = vector(0,0,0) # initializing the net electric field at dq_top
    E_at_dq_top_arrow = arrow(pos=dq_top.pos, axis=E_scale*E_at_dq_top, 
                              color=color.yellow)
    
    for dq_bottom in BottomTape: # iterate through each charge in BottomTape

        # Calculate E-field at the location of dq_top due to dq_bottom
        dE_at_dq_top_by_dq_bottom = Efield(dq_bottom,dq_top.pos)
        E_at_dq_top = E_at_dq_top + dE_at_dq_top_by_dq_bottom

        # Calculate the electric force on dq_top due to dq_bottom
        F_E_on_dq_top_by_dq_bottom = dq_top.charge*dE_at_dq_top_by_dq_bottom
        F_E_on_top = F_E_on_top + F_E_on_dq_top_by_dq_bottom

    # Create the arrow for the net electric field at dq_top due to BottomTape
    E_at_dq_top_arrow.axis = E_scale*E_at_dq_top/mag(E_at_dq_top)


## =============================================================================
## GRAPHICS - PART 2
## =============================================================================

# We will now create arrows to represent the net electric force on TopTape and 
# the gravitational force on TopTape.

#= Electric force vector
F_E_arrow = arrow(pos=middleTop, axis=F_E_scale*F_E_on_top, color=color.cyan)


#= Gravitational force vector
F_G_arrow = arrow(pos=middleTop, axis=F_G_scale*vector(0,-M*g,0), 
                  color=color.green)

#= Model Key
create_key_entry() # initializes key
create_key_entry("Electric Force", F_E_arrow.color, 1)
create_key_entry("Electric Field", E_at_dq_top_arrow.color, 2)
create_key_entry("Top Tape", color.magenta, 3)
create_key_entry("Graviational Force", F_G_arrow.color, 4)
create_key_entry("Bottom Tape", color.red, 5)

print("Magnitude of electric force:", mag(F_E_on_top))
print("Magnitude of gravitational force:", M*g)
print("The charge on each U-Tape is manually estimated to be", Q, 
      "C, which is",diff_factor,"times more that the estimated charge for each",
      "U-Tape in Part 1.")
      
