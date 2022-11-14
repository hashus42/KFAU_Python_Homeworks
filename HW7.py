text = "X-DSPAM-Confidence:    0.8475"

indexOfNum = text.find("0")

num = text[indexOfNum:]
print(float(num))