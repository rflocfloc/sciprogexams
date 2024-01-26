def loadReadCounts(file, minGeneReadCount = -1, minSampleReadCount = -1):
		raise Exception("TODO IMPLEMENT ME !")

def getStableGenes(counts, n = 10):
		raise Exception("TODO IMPLEMENT ME !")

def normalizeReadCounts(counts):
		raise Exception("TODO IMPLEMENT ME !")

def plotCounts(counts, hist=True):
		raise Exception("TODO IMPLEMENT ME !")


# Example code to test the functions
# WARNING: this code does not test all possible parameters
#          be sure to test them all
counts = loadReadCounts("rawcounts.all.txt")
stableGenesCounts = getStableGenes(counts, n = 20)
normCounts = normalizeReadCounts(counts)
plotCounts(normCounts, hist=True)
