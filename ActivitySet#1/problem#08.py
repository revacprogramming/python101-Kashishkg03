text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(':')
p = text[pos+1:]
end = float(p)
print(end)