Web VPython 3.2

""" SUMMER 2023 PHYS 2212 EXPERIMENT 1 - Part 1: Single Point Charge
A computational model of two charged tapes exerting an electric force on each 
other and experiencing a gravitational force. The charges on each tape are
modeled as a single point charge located in the center of the tape.

Goal: Use this model to estimate the amount of charge on each tape necessary to 
float one tape above the other.

@author Ethan Nguyen-Tu
@date 28 May 2023
"""

# ==============================================================================
# CONSTANTS
# ==============================================================================
#= Coulomb's Constant
oofpez = 9e9 # One Over Four Pi Epsilon-Zero

#= Fundamental Charge
q_fund = 1.6e-19 # C

#= Length of an atom
atom_length = 1e-10 # m (Given in Lab Instructions)

#= Gravity Near Earth's Surface
g = 9.81 # m/s^2 | acceleration due to gravity near the surface of the earth


# ==============================================================================
# Variables and Initial Values
# ==============================================================================
#= U-Tape
utape_length = 0.19
utape_width = 0.019

separation = 0.026 # distance between the two repelling u-tapes


# ==============================================================================
# CALCULATIONS
# ==============================================================================
#= U-Tape Mass
# GIVEN: mass of tape is 1 gram per meter of length = 0.001 kg per m length
utape_mass = utape_length * 1/1000
print("Mass of each U-Tapes:",utape_mass,"kg")

#= Gravitational Force on Top U-Tape
Fg = utape_mass * g * vec(0,-1,0)
print("Gravitational force acting on the top U-Tape:",Fg,"N")

#= Electric Force on Top U-Tape
Fe = -Fg # Top U-Tape is floating above Bottom U-Tape => Force Equilibrium
print("Electric force acting on the top U-Tape:",Fe,"N")

#= Charge of Both U-Tapes
# Assuming each U-Tape has the same charge (q)
q = sqrt(mag(Fe) / oofpez * separation**2)
print("Charge on each U-Tape:",q,"C")

#= Number of Electrons Count
count_electrons = q / q_fund
print("Electron deficiency on each U-Tape:", count_electrons, "electrons")

#= Ratio of Deficient Electron to Tape Atoms
# Number of atoms in each tape
tape_atoms = utape_length * utape_width / atom_length**2 # atoms in tape
print("Atoms in tape:",tape_atoms,"atoms")

#= Deficient electrons per tape atom
ratio = count_electrons / tape_atoms
print("Ratio of deficient electron per tape atom:",ratio,"electrons per atom")


# ==============================================================================
# FUNCTION THAT HELPS CREATE THE MODEL KEY
# ==============================================================================
def create_key_entry(key_entry="<b>Key</b>",entry_color=color.black,list_num=0):
    entry = label(pixel_pos=True, box=False, opacity=0, color=entry_color,
                  pos=vec(10,scene.height,0)-(list_num+1)*vec(0,20,0), 
                  text=key_entry, align="left")


# ==============================================================================
# GRAPHICS
# ==============================================================================
#= Scene
scene.background = color.gray(0.75) # make the scene background slightly gray

#= Scale Factors
v_scale = 10 # Vectors
ut_scale = .1 # U-Tape point

#= U-Tapes
#== Tape Starting Position
# Separation distance halved to center everything in scene
tape_pos_start = vec(0,-separation/2,0)
#== Bottom Held U-Tape
utape_bottom = sphere(pos=tape_pos_start, radius=ut_scale*separation,
                      color=color.red)
#== Top U-Tape
utape_top = sphere(pos=tape_pos_start+vec(0,separation,0),
                   radius=ut_scale*separation, color=color.magenta)

#= Force Vector Representation
#== Electric Force
Fe_arrow = arrow(pos=utape_top.pos, axis=v_scale*Fe, color=color.cyan)
#== Gravitational Force
Fg_arrow = arrow(pos=utape_top.pos, axis=v_scale*Fg, color=color.green)
                 
#= Model Key
create_key_entry() # initializes key
create_key_entry("Electric Force", color.cyan, 1)
create_key_entry("Top Tape", color.magenta, 2)
create_key_entry("Graviational Force", color.green, 3)
create_key_entry("Bottom Tape", color.red, 4)

