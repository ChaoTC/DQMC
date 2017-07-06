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
	def count(population, xLength, yLength, xSteps, ySteps):
		distribution = np.array([[0]*(ySteps)]*(xSteps))
		for psip in population:
			val = (psip.x+(xLength/2),psip.y+(yLength/2))
			xIndex = int(round(val[0]/(xLength/xSteps)))
			yIndex = int(round(val[1]/(yLength/ySteps)))
			if(xIndex >= 0 and xIndex < xSteps and yIndex >= 0 and yIndex < ySteps):
				distribution[xIndex,yIndex]+= 1
		return distribution

class Counter3D:

	@staticmethod
	def count(population, xLength, yLength, xSteps, ySteps):
		distribution = np.array([[[0]*(ySteps)]*(xSteps)]*(zSteps))
		for psip in population:
			val = (psip.x+(xLength/2),psip.y+(yLength/2))
			xIndex = int(round(val[0]/(xLength/xSteps)))
			yIndex = int(round(val[1]/(yLength/ySteps)))
			zIndex = int(round(val[2]/(zLength/zSteps)))
			if(xIndex >= 0 and xIndex < xSteps and yIndex >= 0 and yIndex < ySteps and zIndex >= 0 and zIndez < zSteps):
				distribution[xIndex,yIndex,zIndex]+= 1
		return distribution