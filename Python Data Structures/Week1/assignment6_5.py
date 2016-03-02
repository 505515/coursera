text = "X-DSPAM-Confidence:    0.8475"

fwhite = text.find(' ')
swhite = text[fwhite:]

score = float(swhite.lstrip())

print(score)

