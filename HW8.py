myFile = open("mbox-short.txt")
print(myFile.read().find("X-DSPAM-Confidence:    0.8475"))
print(myFile.read()[-1])