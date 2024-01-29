"""Solution to exercise 2"""

import pandas as pd
import matplotlib.pyplot as plt

def loadAnnotations(filename, source = ""):
	annotColnames = ["seqname","source","feature","start","end","score","strand","frame","attribute"]
	data = pd.read_csv(filename, sep="\t", 	names=annotColnames)
	
	attributeColnames = data["attribute"].iloc[0].rstrip(" ").split("; ")
	attributeColnames = [x.split(" ")[0] for x in attributeColnames]

	attributeData = data["attribute"].str.rstrip("; ").str.split(";")
	newAttributeData = []
	for item in attributeData:
		currItemData = ""
		for part in item:
			currItemData += part.lstrip(" ").replace("\"", "").split(" ")[1] + " "
		newAttributeData.append(currItemData.rstrip(" "))
	
	data["attribute"] = newAttributeData
	data[attributeColnames] = data['attribute'].str.split(" ", expand=True)
	data.drop(columns="attribute", inplace=True)

	if (source != ""):
		data = data[data["source"] == source]

	print("Number of items found in annotation: {}".format(data.shape[1]))
	print("Sources found in annotation: {}".format(data["source"].unique()))
	print("Types of features found in annotation: {}".format(data["feature"].nunique()))
	
	return(data)
	
annots = loadAnnotations("hs_annotation.gtf", "")

def plotGeneTypes(annotations): 
	counts = annotations.groupby("gene_type")["gene_id"].count()
	
	if (annotations["source"].nunique() == 1):
		counts.plot(kind="bar")
		plt.xlabel("gene_type")
		plt.ylabel("frequency")
		plt.title("Frequency of genes by gene_type")
		plt.show()
		plt.close()
	else:
		counts = []
		fig = plt.figure()
		sources = annotations["source"].unique()
		plotNum = 0
		for source in sources:
			sourceCounts = annotations[annotations["source"]==source].groupby("gene_type")["gene_id"].count()
			plotNum += 1
			pos = int(str(len(sources)) + "1" + str(plotNum))
			ax = fig.add_subplot(pos)
			ax.bar(x = range(len(sourceCounts)), height=sourceCounts, tick_label = sourceCounts.index)
			ax.set_xlabel("gene_type")
			ax.set_ylabel("frequency")
			ax.set_title("Frequency of genes by gene_type: {}".format(source))
			counts.append(sourceCounts)
			
		plt.show()
		plt.close()

	return(counts)

geneTypes = plotGeneTypes(annots)
print(geneTypes)

def computeGeneTypeOccupancy(annotations, gene_type, relative=False): 
	genes = annotations[annotations["gene_type"] == gene_type].copy()
	genes["length"] = genes["end"] - genes["start"]
	if (relative):
		allLength = annotations["end"] - annotations["start"]
		return 100.0*(genes["length"].sum() / allLength.sum())
	else:
		return genes["length"].sum()

print("Absolute protein-coding occupancy: {}".format(computeGeneTypeOccupancy(annots, "protein_coding")))
print("Relative protein-coding occupancy: {}%".format(computeGeneTypeOccupancy(annots, "protein_coding", relative=True)))

