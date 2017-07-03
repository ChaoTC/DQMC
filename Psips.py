import math

class Psip1D(object):

	#Initializes a Psip1D at the specified coordinate
	def __init__(self, x):
		self.x = x

	#Increments the x variable by the specified amount
	def move(self, step):
		self.x += step

	#Returns a new Psip1D instance at the same coordinate
	def replicate(self):
		return Psip1D(self.x)

class Psip2D(object):

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def move(self, step, angle):
		self.x += (step * math.cos(angle))
		self.y += (step * math.sin(angle))

	def replicate(self):
		return Psip2D(self.x,self.y)

	def __str__(self):
		return str(self.x) + ", " + str(self.y)

class Psip3D(object):
	def __init__(self,x,y,z):
		self.x=x
		self.y=y
		self.z=z

	def move(self,step,radial,azimuthal):
		self.x+=(step*math.cos(radial)*math.sin(azimuthal))
		self.y+=(step*math.sin(radial)*math.sin(azimuthal))
		self.z+=(step*math.cos(azimuthal))

	def replicate(self):
		return Psip3D(self.x,self.y,self.z)

	def __str__(self):
		return str(self.x) + ", " + str(self.y) + ", " str(self.z)