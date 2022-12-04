#Python 3.0
import re
import os
import collections
import time
import numpy as np
#import other modules as needed

class pagerank:
	
	def pagerank(self, input_file, alpha = 0.15):
	#function to implement pagerank algorithm
	#input_file - input file that follows the format provided in the assignment description
		transitionMatrix = self.getTransitionMatrixWithTeleporting(input_file, alpha)
		initialVector = self.getInitialVector(len(transitionMatrix))
		for _ in range(100):
			initialVector = self.powerIteration(initialVector, transitionMatrix)
		
		pageRank = initialVector.tolist()[0]
		pageRankToId = [(value, i) for i, value in enumerate(pageRank)]
		pageRankToId = sorted(pageRankToId, reverse = True)

		for value, id in pageRankToId:
			print(f"Page id: {id}, Page rank: {value}")

	def getAdjacencyMatrix(self, input_file):
		lines = None
		with open(input_file) as f:
			lines = f.readlines()
		
		lines = [line.strip() for line in lines]
		numPages = int(lines[0])
		numLinks = int(lines[1])

		edges = [[0] * numPages for _ in range(numPages)]

		for line in lines[2:]:
			line = [int(l) for l in line.split()]
			x, y = line
			edges[x][y] = 1
		return edges

	def getTransitionMatrixWithTeleporting(self, input_file, alpha):
		test = self.getAdjacencyMatrix(input_file)
		n = len(test)
		for r in range(len(test)):
			numOfOnes = sum(test[r])
			if numOfOnes == 0:
				for c in range(len(test[0])):
					test[r][c] = 1 / n
			else:
				for c in range(len(test[0])):
					if test[r][c] == 1:
						test[r][c] = 1/numOfOnes
		test = np.matrix(test)
		test = test*(1-alpha)
		test = test + (alpha / n)
		return test
	
	def getInitialVector(self, n):
		x = np.array([1/n for _ in range(n)])
		return x

	def powerIteration(self, x, p):
		return x.dot(p)

if __name__ == "__main__":
	pr = pagerank()
	print(f"For file test1.txt")
	pr.pagerank('groupassignment4/pagerank/test1.txt')
	print(f"For file test2.txt")
	pr.pagerank('groupassignment4/pagerank/test2.txt')