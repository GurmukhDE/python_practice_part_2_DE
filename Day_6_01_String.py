#1Reverse a string (loop)

s = "suresh"
rev = ""
for ch in s:
    rev = ch + rev
print(rev)
#-------------------------------

#2Check Palindrome

s = "radar"
print(s == s[::-1])
#-------------------------------

#3Anagram Check
s1 = "listen"
s2 = "silent"
print(sorted(s1) == sorted(s2))
#--------------------------------


#4Count vowels
s = "engineering"
vowels = "aeiou"
freq = {}

for ch in s:
    if ch in vowels:
        freq[ch] = freq.get(ch, 0) + 1


print(freq)
#------------------------------------


#5First non-repeating character
s = "aabbcddde"
for ch in s:
    if s.count(ch) == 1:
        print(ch)
        break
#--------------------------------------
#6Remove duplicate characters (preserve order)

s = "engineering"
res = ""
for ch in s:
    if ch not in res:
        res += ch
print(res)

#7Longest word in sentence
sentence = "Python makes coding enjoyable and powerful"
print(max(sentence.split(), key=len))
#-------------------------------------------------

#8Remove vowels
s = "beautiful"
vowels = "aeiouAEIOU"
print("".join(ch for ch in s if ch not in vowels))

#------------------------------------------------


