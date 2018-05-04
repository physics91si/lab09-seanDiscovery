# Physics 91SI
# Spring 2018
# Lab 8

# Modules you won't need
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Modules you will need
import numpy as np
import particle

# TODO: Implement this function
def init_molecule():
    """Create Particles p1 and p2 inside boundaries and return a molecule
    connecting them"""
    position1 = np.array([0.2, 0.1]) #np.random.rand(2)
    position2 = np.array([0.8, 0.8]) #np.random.rand(2) 
    M1 = 1.0
    M2 = 2.0 
    k = 1.0 
    equil_length = 0.5 
    molecule = particle.Molecule(position1, position2, M1, M2, k, equil_length)
    return molecule

# TODO: Implement this function
def time_step(dt, mol):
    """Sets new positions and velocities of the particles attached to mol"""
    #p1 = mol.p1 
    #p2 = mol.p2 
    #print(p1.pos, p2.pos) 

    # update velocity 
    v_1_update = mol.p1.vel + dt*mol.get_force()/mol.p1.m
    v_2_update = mol.p2.vel - dt*mol.get_force()/mol.p2.m 
    mol.p1.vel = v_1_update
    mol.p2.vel = v_2_update

    # update position 
    position_1_update = mol.p1.pos + mol.p1.vel*dt
    position_2_update = mol.p2.pos + mol.p2.vel*dt
    mol.p1.pos = position_1_update 
    mol.p2.pos = position_2_update

    #print(p1.pos, p2.pos) 

#############################################
# The rest of the file is already implemented
#############################################

def run_dynamics(n, dt, xlim=(0, 1), ylim=(0, 1)):
    """Calculate each successive time step and animate it"""
    mol = init_molecule()

    # Animation stuff
    fig, ax = plt.subplots()
    line, = ax.plot((mol.p1.pos[0], mol.p2.pos[0]), (mol.p1.pos[1], mol.p2.pos[1]), '-o')
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    plt.title('Dynamics simulation')
    dynamic_ani = animation.FuncAnimation(fig, update_anim, n,
            fargs=(dt, mol,line), interval=50, blit=False)
    plt.show()

def update_anim(i,dt, mol, line):
    """Update and draw the molecule. Called by FuncAnimation"""
    time_step(dt, mol)
    print("Molecule 1 ", mol.p1.pos)
    print("molecule 2 ", mol.p2.pos) 
    line.set_data([(mol.p1.pos[0], mol.p2.pos[0]),
                   (mol.p1.pos[1], mol.p2.pos[1])])
    return line,

if __name__ == '__main__':
    # Set the number of iterations and time step size
    n = 10
    dt = .1
    run_dynamics(n, dt)
