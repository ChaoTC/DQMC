from Psips import *

class Population1D(object):

	@staticmethod
	def initPopulation(size, steps, length):
		xStep = length/steps
		population = []
		for x in range(steps):
			xCoordinate = (x * xStep) - (length/2)
			copiesAtCoordinate = size/steps
			for y in range(copiesAtCoordinate):
				population.append(Psip1D(xCoordinate))
		return population

class Population2D(object):

	@staticmethod
	def initPopulation(size, xSteps, ySteps, xLength, yLength):
		xStep = xLength/xSteps
		yStep = yLength/ySteps
		population = []
		for x in range(xSteps):
			for y in range(ySteps):
				xCoordinate = (x * xStep) - (xLength/2)
				yCoordinate = (y * yStep) - (yLength/2)
				copiesAtCoordinate = size/(xSteps * ySteps)
				for _ in range(copiesAtCoordinate):
					population.append(Psip2D(xCoordinate, yCoordinate))
		return population

	@staticmethod
	def printPopulation(population):
		for member in population:
			print(member)

class Population3D(object):

	@staticmethod
<<<<<<< HEAD
	def initPopulation(size,xSteps,ySteps,xSteps,xLength,yLength,zLength):
		xStep=xLength/xSteps
		yStep=yLength/ySteps
		zStep=xLength/zSteps
		population=[]
		for x in range(xSteps):
			for y in range(ySteps):
				for z in range(zSteps):
					xCoordinate=(x*xStep)-(xLength/2)
					yCoordinate=(y*yStep)-(yLength/2)
					zCoordinate=(z*zStep)-(zLength/2)
					copiesAtCoordinate=size/(xSteps*ySteps*zSteps)
					for _ in range(copiesAtCoordinate):
						population.append(Psip3D(xCoordinate,yCoordinate,zCoordinate))
		return population


=======
	def initPopulation(size, xSteps, ySteps, zSteps, xLength, yLength, zLength):
		xStep = xLength/xSteps
		yStep = yLength/ySteps
		zStep = zLength/zSteps
		population = []
		for x in range(xSteps):
			for y in range(ySteps):
				for z in range (zSteps):
					xCoordinate = (x * xStep) - (xLength/2)
					yCoordinate = (y * yStep) - (yLength/2)
					zCoordinate = (z * yStep) - (zLength/2)
					copiesAtCoordinate = size/(xSteps * ySteps * zStep)
					for _ in range(copiesAtCoordinate):
						population.append(Psip2D(xCoordinate, yCoordinate, zCoordinate))
		return population

>>>>>>> 616803b1fec8813072fd755859e992955ef8d9d9
	@staticmethod
	def printPopulation(population):
		for member in population:
			print(member)