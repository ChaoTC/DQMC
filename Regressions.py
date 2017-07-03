import scipy.integrate as integrate
import numpy as np
import math

class HarmonicOscillatorRegression:

	#Expected wavefunction form
	def func(self, x, f, A):
		return f*math.exp((-1*x*x)/(2*A*A))

	#Integrand
	def integrand(self, x, f, A):
		return func(x, f, A)*func(x, f, A)

	#Find the best fitting function of the form fe^(-(x^2/A^2)
	#Requires an anticipated range for both A and f
	#Returns an array containing best fitting A and r squared
	def regress(self, distribution, length):
		precision = 1000.0

		xList = [0]*len(distribution)
		for i in range(len(distribution)):
			xList[i] = (i*(length/len(distribution)))-(length/2)

		while(distribution[0] == 0):
			distribution = distribution[1:]
			xList = xList[1:]

		while (distribution[-1] == 0):
			distribution.pop()
			xList.pop()

		m = np.mean(distribution)
		bestF = 0
		bestA=0
		bestRsqr = 0

		for A in [x /precision for x in range(1, int(precision*2))]:
			print A
			if round((10*precision*A)%precision) ==0:
					print "%.1f%%" % (A*100)

			for F in range(max(distribution)-25, max(distribution)):
				SStot = 0
				SSres = 0

				for i in range(len(distribution)):
					SSres += (distribution[i] - self.func(xList[i], F, A))**2
					SStot += (distribution[i] - m)**2

				rsqr = 1-(SSres/SStot)
				if(rsqr>bestRsqr):
					bestA = A
					bestF = F
					bestRsqr = rsqr

		self.normalize(bestF, bestA, bestRsqr)
		return [bestF, bestA, bestRsqr]

	#Normalize the wavefunction
	def normalize(self, bestF, bestA, bestRsqr):
		if bestA != 0:
			N = 1/(math.sqrt(integrate.quad(cls.integrand, -(LEN/2), (LEN/2), args = (bestF, bestA))[0]))
			fNorm = N * bestF

			print "WaveFunction = %fe^(-x^2)/(2*%f^2)\nR-squared = %f" % (bestF, bestA, bestRsqr)
			print "Normalized WaveFunction = %fe^((-x^2)/(2*%f^2))" % (fNorm, bestA)
		else:
			print "function not appropriate"

class ParticleInABoxRegression:

	#Expected wavefunction form
	def func(self, x, C, D):
		return C*math.cos(D*x);

	#Integrand
	def integrand(self, x, C, D):
		return func(x, C, D)*func(x, C, D)

	#Find the best fitting function of the form fe^(-(x^2/A^2)
	#Requires an anticipated range for both A and f
	#Returns an array containing best fitting A and r squared
	def regress(self, distribution, length):
		precision = 1000

		xList = [0]*len(distribution)
		for i in range(len(distribution)):
			xList[i] = (i*(length/len(distribution)))-(length/2)

		while(distribution[0] == 0):
			distribution = distribution[1:]
			xList = xList[1:]

		while (distribution[-1] == 0):
			distribution.pop()
			xList.pop()

		m = np.mean(distribution)
		bestC = 0
		bestD=0
		bestRsqr = 0

		for D in [x /precision for x in range(precision, int(precision*2))]:
			if round((10*precision*D)%precision) ==0:
					print "%.1f%%" % (D*100-100)

			for C in range(max(distribution)-10, max(distribution)+10):
				SStot = 0
				SSres = 0

				for i in range(len(distribution)):
					SSres += (distribution[i] - self.func(xList[i], C, D))**2
					SStot += (distribution[i] - m)**2

				rsqr = 1-(SSres/SStot)
				if(rsqr>bestRsqr):
					bestC = C
					bestD = D
					bestRsqr = rsqr

		self.normalize(bestC, bestD, bestRsqr)
		return [bestC, bestD, bestRsqr]

	#Normalize the wavefunction
	def normalize(self, bestC, bestD, bestRsqr):
		if bestC != 0:
			N = 1/(math.sqrt(integrate.quad(integrand, -1, 1, args = (bestC, bestD))[0]))
			CNorm = N * bestC
			return CNorm
		else:
			print "function not appropriate"
			return 0

