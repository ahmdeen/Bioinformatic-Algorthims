"""
Given: Integers k and m followed by a set of points Data in a m-dimensional space.

Return: A set Centers consisting of k points (centers) resulting from applying FarthestFirstTraversal(Data, k), 
where the first point from Data is chosen as the first center to initialize the algorithm.

"""
from scipy.spatial import distance
import sys

def dist(p1, p2):
	'''Trivial Wrapper Method to Find Euclidean Distance'''
	return distance.euclidean(p1,p2)

def findClosestCenter(datapoint, centers):
	'''Finds the Closest Center to a Datapoint'''
	minDist = sys.maxint
	minIndex = 0
	for i in xrange(len(centers)):

		if dist(datapoint, centers[i]) < minDist:

			minDist = dist(datapoint, centers[i])
			minIndex = i

	return centers[minIndex]

def farthestFirst(k, data):
	'''Returns the centers of the Data Cluster'''
	centers = []
	centers.append(data.pop(0))
	
	while len(centers) < k:
		longestDist = 0.0
		candidateIndex = 0

		for i in xrange(len(data)):

			center = findClosestCenter(data[i], centers)
			if dist(center, data[i]) > longestDist:
				candidateIndex = i
				longestDist = dist(center, data[i])

		centers.append(data.pop(candidateIndex))

	return centers



data = []

with open('Data/rosalind_9a.txt') as infile:

	k,m = map(int, infile.readline().strip().split())
	data.extend([map(float, line.strip().split()) for line in infile.readlines()])

answer = farthestFirst(k, data)


with open('Ros9A_Answer.txt','w') as outfile:
	for center in answer:
		print ' '.join(map(str, center))+'\n'
		outfile.write(' '.join(map(str, center))+'\n')

