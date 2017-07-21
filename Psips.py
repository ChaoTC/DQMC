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
		return str(self.x) + ", " + str(self.y) + ", " + str(self.z)

def PsipH(object):

	elecFactor = 1837

	def __init__(self,px, py, pz, ex, ey, ez):
		self.px = px
		self.py = py
		self.pz = pz
		self.ex = ex
		self.ey = ey
		self.ez = ez

	def move(self, pstep, pradial, pazimuthal, estep, eradial, eazimuthal):
		self.px+=(pstep*math.cos(pradial)*math.sin(pazimuthal))
		self.py+=(pstep*math.sin(pradial)*math.sin(pazimuthal))
		self.pz+=(pstep*math.cos(pazimuthal))
		self.ex+=(estep*math.cos(eradial)*math.sin(eazimuthal))
		self.ey+=(estep*math.sin(eradial)*math.sin(eazimuthal))
		self.ez+=(estep*math.cos(eazimuthal))

	def replicate(self):
		return PsipH(self.px,self.py,self.pz,self.ex,self.ey,self.ez)
















