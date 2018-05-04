# Physics 91SI
# Spring 2018
# Lab 8

import numpy as np

class Particle(object):
    """Stores information about a particle with mass, position, and velocity."""
    
    def __init__(self, Position, M):
        """Create a particle with Position (numpy array of len 2) and mass."""
        self.pos = Position   # Set position
        self.m = M  # Sets mass
        # Initial velocity and acceleration set to be zero
        self.vel = np.zeros((2,))
        self.acc = np.zeros((2,))

class Molecule(Particle): 
	""" 
	Constructs an instance of a Molecule object, using the Particle class defined above. 
	The function get_displ returns the displacement between the particle 1 and particle 2: 
		get_displ = p1.pos - p2.pos. 
	The function get_force returns the force on particle 1 from particle 2, calculated from 
	Hooke's law. 
	"""

	def __init__(self, position1, position2, M1, M2, k, equil_length):
		"""Construct two particles from Particle class, spring constant, and bond equilibrium length """
		self.p1 = Particle(position1, M1)
		self.p2 = Particle(position2, M2)
		self.k = k 
		self.eq_length = equil_length 

	def get_displ(self):
		# returns displacement between two particles 
		return self.p1.pos - self.p2.pos 

	def get_force(self):
		# obtain angle of displacement vector from displacement function 
		delta = self.get_displ()
		theta = np.arctan2(delta[1], delta[0])
		
		# project the equilibrium length vector onto x, y axes 
		equil_vector = np.zeros(2)
		equil_vector[1] = self.eq_length*np.sin(theta)
		equil_vector[0] = self.eq_length*np.cos(theta)

		# compute the force 
		return -self.k*(delta - equil_vector)
