import os
import pprint

def parseText(inputText):
	inputDir = inputText
	inputText = open(inputText,"r")
	inputText = inputText.read().splitlines()
	msg = ""
	msgs = []
	for line in inputText:
		if "]" in line:
			if msg == "":
				msg += line
			else:
				msgs.append(msg)
				msg = ""
		else:
			msg += line
	return msgs

msgs = parseText(r"C:\Users\Yujie Wang\Desktop\ml.txt")

#You might hate me but argparser takes 2 mins.

pprint.pprint(len(msgs))
mlmsgs = []
mlkeywords = ["machine", "machine learning", "ml ", " ml ", " ai ", ", ml", ", ai", "vision", "artificial", "intelligence", " ml.", " ai.", "genetic", "neural", "network", "data"]

msgs = [valid for valid in msgs if "joined #" not in valid]

for msg in msgs:
	msg = msg.lower()
	if any (mlkeyword in msg for mlkeyword in mlkeywords):
		mlmsgs.append(msg)

print("\n\n\n\n")
pprint.pprint(mlmsgs)
print(str(len(mlmsgs)) + "/" + str(len(msgs)))
print("\n\n\n\n")
notml = list(set(msgs) - set(mlmsgs))
pprint.pprint(notml)
