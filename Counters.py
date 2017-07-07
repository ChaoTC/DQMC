import math
import numpy as np

class Counter1D:
	
	@staticmethod
	def count(population, length, steps):
		distribution = [0]*(steps+1)
		for psip in population:
			val = psip.x-(length/2)
			index = int(math.floor(val/(length/steps)))
			distribution[index] += 1

		return distribution

class Counter2D:

	@staticmethod
	def count(population, length, steps):
		distribution = np.array([[0]*(steps)]*(steps))
		for psip in population:
			val = (psip.x+(length/2), psip.y+(length/2))
			xIndex = int(round(val[0]/(length/steps)))
			yIndex = int(round(val[1]/(length/steps)))
			if(xIndex >= 0 and xIndex < steps and yIndex >= 0 and yIndex < steps):
				distribution[xIndex,yIndex]+= 1
		return distribution

class Counter3D:

	@staticmethod
	def count(population, length, steps):
		distribution = np.array([[[0]*(steps)]*(steps)]*(steps))
		for psip in population:
			val = (psip.x+(length/2),psip.y+(length/2),psip.z+(length/2))
			xIndex = int(round(val[0]/(length/steps)))
			yIndex = int(round(val[1]/(length/steps)))
			zIndex = int(round(val[2]/(length/steps)))
			if(xIndex >= 0 and xIndex < steps and yIndex >= 0 and yIndex < steps and zIndex >= 0 and zIndez < steps):
				distribution[xIndex,yIndex,zIndex]+= 1
		return distribution