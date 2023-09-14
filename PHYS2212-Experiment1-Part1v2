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
# FUNCTION THAT HELPS CREATE THE MODEL KEY
# ==============================================================================
def create_key_entry(key_entry="<b>Key</b>",entry_color=color.black,list_num=0):
    entry = label(pixel_pos=True, box=False, opacity=0, color=entry_color,
                  pos=vec(10,scene.height,0)-(list_num+1)*vec(0,20,0), 
                  text=key_entry, align="left")
                  

# ==============================================================================
# FUNCTION FOR THE ELECTRIC FIELD
# ==============================================================================
def Efield(chargedParticle,observationLocation):   
    r = observationLocation - chargedParticle.pos
    return oofpez * chargedParticle.charge / mag(r)**3 * r # r-hat component form
    

# ==============================================================================
# GRAPHICS - PART 1
# ==============================================================================
#= Scene
scene.background = color.gray(0.75) # make the scene background slightly gray

#= Scale Factors
v_scale = 10 # Vectors
ut_scale = .1 # U-Tape point
e_scale = 1/1.4e7 # Electric field (not to scale with the other vectors)

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
q = sqrt(mag(Fe) / oofpez * separation**2) # Solve for q in Fe = -Fg
print("Charge on each U-Tape:",q,"C")
#== Update utape charge
utape_bottom.charge = q
utape_top.charge = q

#= Number of Electrons Count
electrons_count = q / q_fund
print("Electron deficiency on each U-Tape:", electrons_count, "electrons")

#= Ratio of Deficient Electron to Tape Atoms
# Number of atoms in each tape
tape_atoms = utape_length * utape_width / atom_length**2 # atoms in tape
print("Atoms in tape:",tape_atoms,"atoms")

#= Deficient electrons per tape atom
ratio = electrons_count / tape_atoms
print("Ratio of deficient electron per tape atom:",ratio,"electrons per atom")

#= Electric Field
E = Efield(utape_bottom,utape_top.pos) # Function from Experiment 0
print("Electric field vector is E=", E,"N/C")
print("Magnitude of E is |E|=", mag(E),"N/C")

#= Check Calculations
Fe2 = utape_top.charge * E # Electric Force Formula
print("Electric force vector calclated with the electric field:", Fe2, "N")
print("Magnitude of the electric force calclated with the electric field:", 
      mag(Fe2), "N")

if Fe == Fe2:
    print("Experiment 0 function calculation check: No errors")
else:
    print("Experiment 0 function calculation check: Difference of", Fe2-Fe, "N")


# ==============================================================================
# GRAPHICS - PART 2
# ==============================================================================
#= Force Vector Representation
#== Electric Field <= Slightly offset in z-direction to be visible
E_arrow = arrow(pos=utape_top.pos+vec(0,0,.1e-2), axis=e_scale*E, 
                color=color.yellow)
#== Electric Force
Fe_arrow = arrow(pos=utape_top.pos, axis=v_scale*Fe2, color=color.cyan)
#== Gravitational Force
Fg_arrow = arrow(pos=utape_top.pos, axis=v_scale*Fg, color=color.green)
                 
#= Model Key
create_key_entry() # initializes key
create_key_entry("Electric Force", Fe_arrow.color, 1)
create_key_entry("Electric Field", E_arrow.color, 2)
create_key_entry("Top Tape", utape_top.color, 3)
create_key_entry("Graviational Force", Fg_arrow.color, 4)
create_key_entry("Bottom Tape", utape_bottom.color, 5)

