import math

class ZeroPotential(object):
	
	def calculatePotential(self, psip):
		return 1

class ParticleInABoxPotential1D(object):

	def __init__(self, length):
		self.length = length

	def calculatePotential(self, psip):
		x = psip.x
		if x < (self.length/2) and x >= -(self.length/2):
			return 0
		else:
			#float("inf") has some weird properties, but this is a good enough approximation
			return 99999999999999999999999999 

class HarmonicOscillatorPotential1D(object):

	def calculatePotential(self, psip):
		x = psip.x
		return .5*(x**2)

class ParticleInABoxPotential2D(object):

	def __init__(self, length):
		self.length = length

	def calculatePotential(self, psip):
		x = psip.x
		y = psip.y
		if x < (self.length/2) and x >= -(self.length/2) and y < (self.length/2) and y >= -(self.length/2):
			return 0
		else:
			#float("inf") has some weird properties, but this is a good enough approximation
			return 99999999999999999999999999 

class HarmonicOscillatorPotential2D(object):

	def calculatePotential(self, psip):
		x = psip.x
		y = psip.y
		return (.5*(x**2))+(.5*(y**2))

# class BoxWithAWall2D(object):

# 	def __init__(self, xLength, yLength):
# 		self.xLength = xLength
# 		self.yLength = yLength

	# def calculatePotential(self, psip):
	# 	x = psip.x
	# 	y = psip.y
	# 	if ((x < 0 and x >= -(self.xLength/2)) or (x < (self.xLength/2) and x >= (self.xLength/50))) and y < (self.yLength/2) and y >= -(self.yLength/2):
	# 		return 0
	# 	elif (x < self.xLength/50 and x >= 0) and and y < (self.yLength/2) and y >= -(self.yLength/2):
	# 		return 1000
	# 	else:
	# 		return 1000000


class ParticleInABoxPotential3D(object):

	def __init__(self, length):
		self.length = length

	def calculatePotential(self, psip):
		x = psip.x
		y = psip.y
		z = psip.z
		if x < (self.length/2) and x >= -(self.length/2) and y < (self.length/2) and y >= -(self.length/2) and z < (self.length/2) and z >= -(self.length/2):
			return 0
		else:
			#float("inf") has some weird properties, but this is a good enough approximation
			return 99999999999999999999999999 

class HarmonicOscillatorPotential3D(object):

	def calculatePotential(self, psip):
		x = psip.x
		y = psip.y
		z = psip.z
		return (.5*(x**2))+(.5*(y**2))+(.5*(z**2))

class HydrogenicPotential(object):

	eps0 = 8.854188E-12		#Permittivity of Vacuus	(F/m)
	eCharge = 1.602E-19		#Elementary Charge (C)


	def calculatePotential(self, psip):
		radius = psip.radius()
		return -((self.eCharge**2)/(4*math.pi*self.eps0*abs(radius)))













