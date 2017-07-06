from Diffusers import *
from Populations import *
from Counters import *
from Regressions import *
from Visualizers import *

class Simulation1D(object):
	length = 2.0
	steps = 1000
	potentialFunction = ZeroPotential()

	def __init__(self, size, reps):
		self.size = size
		self.reps = reps

	def initPopulation(self):
		return Population1D.initPopulation(self.size, self.steps, self.length)

	def diffuse(self, population):
		xStep = self.length/self.steps
		population = Diffuser1D.diffuse(population, self.potentialFunction, xStep, self.reps)
		return population

	def postProcess(self, population):
		distribution = Counter1D.count(population, self.length, self.steps)
		i=0
		tot = 0
		for val in distribution:
			if(i%5 == 0):
				print (-1+((self.length/self.steps)*float(i))), ",", tot
				tot = 0
			i += 1
			tot+= val
		return distribution

class ParticleInABox1D(Simulation1D):
	def __init__(self, size, reps):
		self.potentialFunction = ParticleInABoxPotential1D(self.length)
		Simulation1D.__init__(self, size, reps)

	def postProcess(self, population):
		distribution = Simulation1D.postProcess(self, population)
		
	
class HarmonicOscillator1D(Simulation1D):
	def __init__(self, size, reps):
		self.potentialFunction = HarmonicOscillatorPotential1D()
		Simulation1D.__init__(self, size, reps)
	
	def postProcess(self, population):
		distribution = Simulation1D.postProcess(self, population)


class Simulation2D(object):

	xLength = 2.0
	yLength = 2.0
	xSteps = 100
	ySteps = 100
	potentialFunction = ZeroPotential()

	def __init__(self, size, reps):
		self.size = size
		self.reps = reps

		self.xStep = self.xLength/self.xSteps
		self.yStep = self.yLength/self.ySteps

	def initPopulation(self):
		population = Population2D.initPopulation(self.size, self.xSteps, self.ySteps, self.xLength, self.yLength)
		return population
		

	def diffuse(self, population):
		population = Diffuser2D.diffuse(population, self.potentialFunction, self.xStep, self.yStep, self.reps)
		return population

	def postProcess(self, population):
		distribution = Counter2D.count(population, self.xLength, self.yLength, self.xSteps, self.ySteps)
		return distribution
		
class ParticleInABox2D(Simulation2D):
	def __init__(self, size, reps):
		self.potentialFunction = ParticleInABoxPotential2D(self.xLength, self.yLength)
		Simulation2D.__init__(self, size, reps)

	def postProcess(self, population):
		distribution = Simulation2D.postProcess(self, population)
		Visualizer2D.visualize("Particle in a Box", distribution, self.xLength, self.yLength, self.xStep, self.yStep)

class HarmonicOscillator2D(Simulation2D):
	def __init__(self, size, reps):
		self.potentialFunction = HarmonicOscillatorPotential2D()
		Simulation2D.__init__(self, size, reps)

	def postProcess(self, population):
		distribution = Simulation2D.postProcess(self, population)
		Visualizer2D.visualize("Harmonic Oscillator", distribution, self.xLength, self.yLength, self.xStep, self.yStep)
	

class Simulation3D(object):

	xLength = 2.0
	yLength = 2.0
	zLength = 2.0
	xSteps = 100
	ySteps = 100
	zSteps = 100
	potentialFunction = ZeroPotential()

	def __init__(self, size, reps):
		self.size=size
		self.reps=reps
		self.xStep=self.xLength/self.xSteps
		self.yStep=self.yLength/self.ySteps
		self.zStep=self.zLength/self.zSteps

	def initPopulation(self):
		population=Population3D.initPopulation(self.size,self.xSteps,self.ySteps,self.zSteps,self.xLength,self.yLength,self.zLength)
		return population

	def diffuse(self, population):
		population=Diffuser3D.diffuse(population,self.potentialFunction,self.xStep,self.yStep,self.zStep,self.reps)
		return population

	def postProcess(self, population):
		distribution=Counter3D.count(population,self.xLength,self.yLength,self.zLength,self.xSteps,self.ySteps,self.zSteps)
		return distribution
		
class ParticleInABox3D(Simulation3D):
	def __init__(self, size, reps):
		self.potentialFunction = ParticleInABoxPotential3D(self.xLength, self.yLength, self.zLength)
		Simulation3D.__init__(self, size, reps)

	def postProcess(self, population):
		distribution = Simulation3D.postProcess(self, population)
		Visualizer3D.visualize("Particle in a Box", distribution, self.xLength, self.yLength, self.zLength, self.xStep, self.yStep, self.zStep)

class HarmonicOscillator3D(Simulation3D):
	def __init__(self, size, reps):
		self.potentialFunction = HarmonicOscillatorPotential3D()
		Simulation3D.__init__(self, size, reps)

	def postProcess(self, population):
		distribution = Simulation3D.postProcess(self, population)
		Visualizer3D.visualize("Harmonic Oscillator", distribution, self.xLength, self.yLength, self.zStep, self.xStep, self.yStep, self.zStep)
	











