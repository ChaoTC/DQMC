import multiprocessing as mp
from Diffusers import *
from Populations import *
from Simulations import *

class DQMCRunner(object):

	#Initializes the DQMC Runner object with the specified simulation and desired number of processes (default 4)
	def __init__(self, simulation, num_processes):
		self.simulation = simulation
		self.num_processes = num_processes

	#Defines that function that is performed by each process
	#Output is sent to the multiprocessing queue output
	def process(self, output):
		population = self.simulation.initPopulation()
		population = self.simulation.diffuse(population)
		output.put(population)

	#Defines the function that is preformed after the processes are joined 
	#Combines all populations into one large population, then invokes the simulation-specific postProcessing behavior
	def postProcess(self, outputPopulations):
		# Assemble all populations into one large one
		population = []
		for outputPopulation in outputPopulations:
			for member in outputPopulation:
				population.append(member)
		self.simulation.postProcess(population)

	#Runs the DQMC simulation
	def run(self):
		print "Running..."
		#Start multprocessing
		output= mp.Queue()	#Multiprocessing queue. Holds output of various processes
		processes = [mp.Process(target= self.process, args= (output,)) for x in range(self.num_processes)]
		for p in processes:
			p.start()
		outputPopulations = [output.get() for x in range(self.num_processes)]	#Move output data of parallel processes to normal list
		for p in processes:
			p.join()

		#Process the output populations from the different processes
		print '\a'
		print "Post-Processing..."
		self.postProcess(outputPopulations)

if __name__ == "__main__":
	SIZE = 125000
	REPS = 500
	NUM_PROCESSES = 2

	simulation = HarmonicOscillator3D(SIZE, REPS)
	runner = DQMCRunner(simulation, NUM_PROCESSES)
	runner.run()
	print "Finished"