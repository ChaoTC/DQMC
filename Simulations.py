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
		stepLength = self.length/self.steps
		population = Diffuser1D.diffuse(population, self.potentialFunction, stepLength, self.reps)
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

	length = 2.0
	steps = 100
	potentialFunction = ZeroPotential()

	def __init__(self, size, reps):
		self.size = size
		self.reps = reps

		self.stepLength = self.length/self.steps

	def initPopulation(self):
		population = Population2D.initPopulation(self.size, self.steps, self.length)
		return population
		

	def diffuse(self, population):
		population = Diffuser2D.diffuse(population, self.potentialFunction, self.stepLength, self.reps)
		return population

	def postProcess(self, population):
		distribution = Counter2D.count(population, self.length, self.steps)
		return distribution
		
class ParticleInABox2D(Simulation2D):
	def __init__(self, size, reps):
		self.potentialFunction = ParticleInABoxPotential2D(self.length)
		Simulation2D.__init__(self, size, reps)

	def postProcess(self, population):
		distribution = Simulation2D.postProcess(self, population)
		Visualizer2D.visualize("Particle in a Box", distribution, self.length, self.stepLength)

class HarmonicOscillator2D(Simulation2D):
	def __init__(self, size, reps):
		self.potentialFunction = HarmonicOscillatorPotential2D()
		Simulation2D.__init__(self, size, reps)

	def postProcess(self, population):
		distribution = Simulation2D.postProcess(self, population)
		Visualizer2D.visualize("Harmonic Oscillator", distribution, self.length, self.stepLength)
	

class Simulation3D(object):

	length = 2.0
	steps = 50
	potentialFunction = ZeroPotential()

	def __init__(self, size, reps):
		self.size=size
		self.reps=reps
		
		self.stepLength = self.length/self.steps

	def initPopulation(self):
		population=Population3D.initPopulation(self.size, self.steps, self.length)
		return population

	def diffuse(self, population):
		population=Diffuser3D.diffuse(population, self.potentialFunction, self.stepLength,self.reps)
		return population

	def postProcess(self, population):
		distribution=Counter3D.count(population, self.length, self.steps)
		return distribution
		
class ParticleInABox3D(Simulation3D):
	def __init__(self, size, reps):
		self.potentialFunction = ParticleInABoxPotential3D(self.length)
		Simulation3D.__init__(self, size, reps)

	def postProcess(self, population):
		distribution = Simulation3D.postProcess(self, population)
		Visualizer3D.visualize("Particle in a Box", distribution, self.length, self.stepLength)

class HarmonicOscillator3D(Simulation3D):
	def __init__(self, size, reps):
		self.potentialFunction = HarmonicOscillatorPotential3D()
		Simulation3D.__init__(self, size, reps)

	def postProcess(self, population):
		distribution = Simulation3D.postProcess(self, population)
		Visualizer3D.visualize("Harmonic Oscillator", distribution, self.length, self.stepLength)
	
class HydrogenAtom(object):
	bohrRad = 5.29177E-11
	stepLength = bohrRad/100
	potentialFunction = HydrogenicPotential()

	def __init__(self, size, reps):
		self.size=size
		self.reps=reps

	def initPopulation(self):
		population = PopulationH.initPopulation(self.size, self.stepLength)
		return population

	def diffuse(self, population):
		population=DiffuserH.diffuse(population, self.potentialFunction, self.stepLength,self.reps)
		return population










