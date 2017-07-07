from Psips import *

class Population1D(object):

	@staticmethod
	def initPopulation(size, steps, length):
		stepLength = length/steps
		population = []
		for x in range(steps):
			xCoordinate = (x * stepLength) - (length/2)
			copiesAtCoordinate = size/steps
			for y in range(copiesAtCoordinate):
				population.append(Psip1D(xCoordinate))
		return population

class Population2D(object):

	@staticmethod
	def initPopulation(size, steps, length):
		stepLength = length/steps
		population = []
		for x in range(steps):
			for y in range(steps):
				xCoordinate = (x * stepLength) - (length/2)
				yCoordinate = (y * stepLength) - (length/2)
				copiesAtCoordinate = size/(steps*steps)
				for _ in range(copiesAtCoordinate):
					population.append(Psip2D(xCoordinate, yCoordinate))
		return population

	@staticmethod
	def printPopulation(population):
		for member in population:
			print(member)

class Population3D(object):

	@staticmethod
	def initPopulation(size, steps, length):
		stepLength = length/steps
		population=[]
		for x in range(steps):
			for y in range(steps):
				for z in range(steps):
					xCoordinate=(x*stepLength)-(length/2)
					yCoordinate=(y*stepLength)-(length/2)
					zCoordinate=(z*stepLength)-(length/2)
					copiesAtCoordinate=size/(steps*steps*steps)
					for _ in range(copiesAtCoordinate):
						population.append(Psip3D(xCoordinate,yCoordinate,zCoordinate))
		return population

	@staticmethod
	def printPopulation(population):
		for member in population:
			print(member)