"""Solution to exercise 1"""

def computeRotation(text, offset):
	if offset >= 0:
		start = offset % len(text)
		return text[start:] + text[:start]
	else:
		start = -offset % len(text)
		return text[len(text) - start:] + text[:len(text) - start]
	
def computeCompressibility(text):
	#print(set(text))
	#print(len(set(text)))
	#print(len(text))
	return 1 - (len(set(text)) / len(text))

myText ="Hello World"
print("Text:", myText)
print("Rotation 2 of the text: {}".format(computeRotation(myText, 2)))
print("Rotation -2 of the text: {}".format(computeRotation(myText, -2)))
print("Compressibility: {:1.2f}".format(computeCompressibility(myText)))

myText ="lorem ipsum dolor sit amet consectetur adipiscing elit"
print("Text:", myText)
print("Rotation -26 of the text: {}".format(computeRotation(myText, -26)))
print("Compressibility: {:1.2f}".format(computeCompressibility(myText)))

myText ="Sometimes it's better to light a flamethrower than curse the darkness."
print("Text:", myText)
print("Rotation 123 of the text: {}".format(computeRotation(myText, 123)))
print("Compressibility: {:1.2f}".format(computeCompressibility(myText)))