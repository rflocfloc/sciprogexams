import pandas as pd
import matplotlib.pyplot as plt


def loadReadCounts(file, minGeneReadCount = -1, minSampleReadCount = -1):
		readCounts = pd.read_csv(file, sep='\t', header= 0, index_col=0 )
		print(readCounts.shape)

		if minGeneReadCount > 0:
			geneTotalCounts = readCounts.sum(axis=1)
			readCounts = readCounts[geneTotalCounts >= minGeneReadCount]
			print(readCounts.shape)

		if minSampleReadCount > 0:
			sampleTotalCounts = readCounts.sum(axis=0)
			readCounts = readCounts.loc[:,sampleTotalCounts >= minSampleReadCount]
			print(readCounts.shape)

		samples = readCounts.columns.unique()
		genes = readCounts.index.unique()
		return {"counts": readCounts, "samples": samples, "genes": genes}

def getStableGenes(counts, n = 10):
		stableCounts = counts["counts"].copy()
		stableTotalCounts = stableCounts.sum(axis=1)
		stableCounts = stableCounts[stableTotalCounts > 0]
		print(stableCounts.shape)

		vars = stableCounts.var(axis=1)
		lowestNVars = vars.sort_values()
		stableCounts = stableCounts.loc[lowestNVars.index[:n],:]
		print(stableCounts.shape)

		return {"counts": stableCounts, "samples": counts["samples"], "genes": stableCounts.index.unique()}

def normalizeReadCounts(counts):
		normalizedCounts = counts["counts"].copy()
		return  {"counts": normalizedCounts.div(normalizedCounts.sum(axis=0) / 1000000), "samples": counts["samples"], "genes": counts["genes"]}

def plotCounts(counts, hist=True):
		plotData = counts["counts"]

		isCPM = str(type(plotData.iloc[1,1])) == "<class 'numpy.float64'>"
		print("Are those CPMs? : " + str(isCPM))

		plotTitle = "Read counts " + ("histogram" if hist else "boxplot") + " by sample of " + ("CPM" if isCPM else "raw counts") + " values"

		if hist:
			plotData.plot(subplots=True, kind="hist", title= plotTitle, layout=(4, round(plotData.shape[1] / 4) + 1))
		else:
			plotData.plot(subplots=False, kind="box", title= plotTitle, layout=(4, round(plotData.shape[1] / 4) + 1))

		plt.show()
		plt.close()


# Example code to test the functions
# WARNING: this code does not test all possible parameters
#          be sure to test them all
counts = loadReadCounts("rawcounts.all.txt", minGeneReadCount=10, minSampleReadCount=4400000)
stableGenesCounts = getStableGenes(counts, n = 20)
normCounts = normalizeReadCounts(counts)
plotCounts(counts, hist=True)
plotCounts(normCounts, hist=False)
