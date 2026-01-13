#1 - Character frequency

s = "malayalam"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)

#-----------------------------------

#2 Word frequency

s = "hello hello world"
freq = {}

for w in s.split():
    freq[w] = freq.get(w, 0) + 1

print(freq)


#--------------------------------------------

# -3 s = "hello hello world"
freq = {}

for w in s.split():
    freq[w] = freq.get(w, 0) + 1

print(freq)

#--------------------------------------------

#4 -Sort dictionary by values

data = {'apple': 3, 'banana': 1, 'orange': 2}
print(dict(sorted(data.items(), key=lambda x: x[1])))

#-------------------------------------------------------












