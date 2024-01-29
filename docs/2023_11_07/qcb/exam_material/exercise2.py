def loadAnnotations(filename, source = ""):
	raise Exception("TODO IMPLEMENT ME !")

def plotGeneTypes(annotations):
	raise Exception("TODO IMPLEMENT ME !")

def computeGeneTypeOccupancy(annotations, gene_type, relative=False):
	raise Exception("TODO IMPLEMENT ME !")

annots = loadAnnotations("hs_annotation.gtf", "")
geneTypes = plotGeneTypes(annots)
print(geneTypes)
print("Absolute protein-coding occupancy: {}".format(computeGeneTypeOccupancy(annots, "protein_coding")))
print("Relative protein-coding occupancy: {}%".format(computeGeneTypeOccupancy(annots, "protein_coding", relative=True)))
