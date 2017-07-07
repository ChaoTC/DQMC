import numpy as np
import random, math
from PotentialFunctions import *

class Diffuser1D(object):

	@staticmethod
	def diffuse(population, potentialFunction, stepLength, reps):
		startSize = len(population)

		for _ in range(reps):
			potentials = []
			while len(population)>(2*startSize):
				population=population[1::2]
			while len(population)<(startSize/2):
				population=[population[i//2] for i in range(len(population)*2)]

			#Movement
			for i in xrange(len(population) - 1, 0, -1):
				step = random.gauss(20*stepLength, 6*stepLength)
				if random.random() < .5:
					population[i].move(step)
				else:
					population[i].move(-step)
				potentials.append(potentialFunction.calculatePotential(population[i]))
			avgPot = np.mean(potentials)

			#death/birth
			for i in xrange(len(population) - 1, 0, -1):
				iPot = potentialFunction.calculatePotential(population[i])
				if iPot<avgPot:
					rando = random.random()
					check = math.exp(-1*(avgPot-iPot))
					if rando>check:
						population.append(population[i].replicate())
				elif iPot>avgPot:
					rando = random.random()
					check = math.exp(-1*(iPot-avgPot))
					if rando>check:
						del population[i]

		return population

class Diffuser2D(object):

	@staticmethod
	def diffuse(population, potentialFunction, stepLength, reps):
		startSize = len(population)

		for _ in range(reps):
			potentials = []
			while len(population)>(2*startSize):
				population = population[1::2]
			while len(population)<(startSize/2):
				population = [population[1//2] for i in range(len(population)*2)]

			#Movement
			for i in xrange(len(population) - 1, 0, -1):
				angle = random.random()*(2*math.pi)
				step = random.gauss(4*stepLength,stepLength)
				population[i].move(step,angle)
				potentials.append(potentialFunction.calculatePotential(population[i]))
			avgPot = np.mean(potentials)

			#Birth/Death
			for i in xrange(len(population) - 1, 0, -1):
				iPot = potentialFunction.calculatePotential(population[i])
				if iPot<avgPot:
					rando = random.random()
					check = math.exp(-1*(avgPot-iPot))
					if rando>check:
						population.append(population[i].replicate())
				elif iPot>avgPot:
					rando = random.random()
					check = math.exp(-1*(iPot-avgPot))
					if rando>check:
						del population[i]

		return population

class Diffuser3D(object):

	@staticmethod
	def diffuse(population,potentialFunction, stepLength, reps):
		startSize=len(population)

		for _ in range(reps):
			print len(population)
			potentials=[]
			while len(population)>(2*startSize):
				population=population[1::2]
			while len(population)<(startSize/2):
				population=[population[1//2] for i in range(len(population)*2)]

			#Movement
			for i in xrange(len(population)-1,0,-1):
				radial=random.random()*(2*math.pi)
				azimuthal=random.random()*math.pi
				step=random.gauss(4*stepLength,stepLength)
				population[i].move(step,radial,azimuthal)
				potentials.append(potentialFunction.calculatePotential(population[i]))
			avgPot=np.mean(potentials)

			#Birth/Death
			for i in xrange(len(population)-1,0,-1):
				iPot=potentialFunction.calculatePotential(population[i])
				if iPot<avgPot:
					rando=random.random()
					check=math.exp(-1*(avgPot-iPot))
					if rando>check:
						population.append(population[i].replicate())
					elif iPot>avgPot:
						rando=random.random()
						check=math.exp(-1*(iPot-avgPot))
						if rando>check:
							del population[i]

		return population

