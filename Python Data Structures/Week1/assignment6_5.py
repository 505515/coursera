text = "X-DSPAM-Confidence:    0.8475"

fwhite = text.find(':')
swhite = text[fwhite + 1:]

score = float(swhite.lstrip())

print(score)

