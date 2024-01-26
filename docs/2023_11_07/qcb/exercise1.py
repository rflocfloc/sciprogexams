def computeRotation(text, offset):
	raise Exception("TODO IMPLEMENT ME !")

def computeCompressibility(text):
	raise Exception("TODO IMPLEMENT ME !")

myText ="Hello World"
print("Text:", myText)
print("Rotation 2 of the text: {}".format(computeRotation(myText, 2)))
print("Compressibility: {:1.2f}".format(computeCompressibility(myText)))

myText ="lorem ipsum dolor sit amet consectetur adipiscing elit"
print("Text:", myText)
print("Rotation -26 of the text: {}".format(computeRotation(myText, -6)))
print("Compressibility: {:1.2f}".format(computeCompressibility(myText)))

myText ="Sometimes it's better to light a flamethrower than curse the darkness."
print("Text:", myText)
print("Rotation 123 of the text: {}".format(computeRotation(myText, 123)))
print("Compressibility: {:1.2f}".format(computeCompressibility(myText)))
