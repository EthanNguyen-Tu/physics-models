GlowScript 3.2 VPython
## PHYS 2211
## Lab 3: Black Hole - Part 2
## @file NguyenTu-PHYS2211-Lab3-P2.py
## @editor Ethan Nguyen-Tu
## @updated 5 March 2023


## =====================================
## VISUALIZATION & GRAPH INITIALIZATION
## =====================================

# White background so the black hole is visible
scene.background = color.white

# Visualization (object, trail, origin)
bh = sphere(pos=vec(0,0,0), color=color.black, radius=2e8)
planet = sphere(pos=vec(1e10,0,0), color=color.cyan, radius=1e8)
trailplanet = curve(color=color.cyan)
ship = sphere(pos=vec(planet.pos.x,planet.radius,0), color=color.magenta, radius=3e7)
trailship = curve(color=color.magenta)


## =======================================
## SYSTEM PROPERTIES & INITIAL CONDITIONS 
## =======================================

# Mass of the black hole 
bh.m = 1.4366e34 # From Part 1

G = 6.7e-11       # gravitational constant
planet.m = 9e28   # mass of planet
ship.m = 7e10     # mass of spaceship
deltat = 1        # deltat (in seconds)
t=0               # initial time

# Max time to run simulation: Time for one orbit of planet around black hole
tmax = 1.77898 * 60 * 60 # hr * min/hr * sec/min = sec


# Initial conditions for the planet 
planet_speed = sqrt(G * bh.m / mag(planet.pos))
planet.vel = vec(0,planet_speed,0)
print("Planet's orbital speed:", planet_speed, "m/s")
print("Planet's orbital period:", (2*pi*mag(planet.pos)/planet_speed)/(60*60), "hrs")
print("---")

# Initial conditions for the spaceship
# Note: Spaceship cannot move faster than the speed of light (299,792,458 m/s)
ship_speed_x = -3.94526e7 # Trial & Error Starting at e6
ship_speed_y = 1.70000e6
ship.vel = vec(ship_speed_x, ship_speed_y, 0) # Initial ship velocity

# Uncomment below 2 lines to have spaceship orbit the black hole
#ship.vel = vec(-3e6, planet_speed, 0) # ship_speed_x = -3e6 & ship_speed_y = planet_speed
#tmax *= 2


## =================
## CALCULATION LOOP
## =================
lowest_r_bh2sh = mag(planet.pos - bh.pos) # lowest distance from black hole to ship

while t < tmax:
    rate(2500)

    #** Net force on the planet:
    # 1) F_grav on the planet by the black hole
    r_bh_to_planet = planet.pos - bh.pos # Observed position - Source position
    r_mag_bh2pl = mag(r_bh_to_planet)
    r_hat_bh2pl = r_bh_to_planet / r_mag_bh2pl # Definition of vector
    # Gravity formula: (-G * m_1 * m_2) / (r_mag^2) * r_hat
    F_bh_ON_planet = ((-G * bh.m * planet.m) / r_mag_bh2pl**2) * r_hat_bh2pl
                     
    # 2) F_grav on the planet by the spaceship
    r_ship_to_planet = planet.pos - ship.pos
    r_mag_sh2pl = mag(r_ship_to_planet)
    r_hat_sh2pl = r_ship_to_planet / r_mag_sh2pl
    
    F_ship_ON_planet = ((-G * ship.m * planet.m) / r_mag_sh2pl**2) * r_hat_sh2pl
    
    # 3) F_net on the planet
    Fnet_ON_planet = F_bh_ON_planet + F_ship_ON_planet
    
    
    #** Net force on the spaceship:
    # 1) F_grav on the spaceship by the black hole
    r_bh_to_ship = ship.pos - bh.pos
    r_mag_bh2sh = mag(r_bh_to_ship)
    r_hat_bh2sh = r_bh_to_ship / r_mag_bh2sh
    
    F_bh_ON_ship = ((-G * bh.m * ship.m) / r_mag_bh2sh**2) * r_hat_bh2sh
    
    # 2) F_grav on the spaceship by the planet
    r_planet_to_ship = ship.pos - planet.pos
    r_mag_pl2sh = mag(r_planet_to_ship)
    r_hat_pl2sh = r_planet_to_ship / r_mag_pl2sh
    
    F_planet_ON_ship = ((-G * planet.m * ship.m) / r_mag_pl2sh**2) * r_hat_pl2sh
    
    # 3) F_net on the spaceship
    Fnet_ON_ship = F_bh_ON_ship + F_planet_ON_ship


    #** MAKING THINGS MOVE: Apply Newton's 2nd law & the position update formula
    # Planet velocity & position update
    planet.vel = planet.vel + (Fnet_ON_planet / planet.m) * deltat
    planet.pos = planet.pos + planet.vel * deltat
    # Ship velocity & position update
    ship.vel = ship.vel + (Fnet_ON_ship / ship.m) * deltat
    ship.pos = ship.pos + ship.vel * deltat


    #** Break conditions (in case of a crash)
    if mag(r_bh_to_ship) < bh.radius:
        print("Oh no, you got sucked into the black hole!")
        break
    if mag(r_ship_to_planet) < planet.radius:
        print("Oh no, you crashed into the planet!")
        break

    trailplanet.append(pos = planet.pos) # Planet is cyan
    trailship.append(pos = ship.pos)     # Spaceship is magenta
    
    t = t + deltat
    
    #** Updates shortest distance from the center of the black hole to the ship
    if mag(r_bh_to_ship) < lowest_r_bh2sh:
        lowest_r_bh2sh = mag(r_bh_to_ship)
    
# --- Console Output ---
print("--- Results ---")
print("Calculations finished after ",t/60,"minutes.")
print("The ship is now", mag(ship.pos)-bh.radius, "m away from the event horizon of the black hole.")
print("The closest the ship was to the center of the black hole is",lowest_r_bh2sh,"m.")
print("The ship's initial velocity is",mag(ship.vel),"m/s.")
