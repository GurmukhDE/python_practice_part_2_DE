#1 - Common elements between lists

a = [1,2,3,4]
b = [3,4,5,6]
print(list(set(a) & set(b)))

#----------------------

#2 -Unique words

sentence = "Python is powerful and Python is easy"
print(set(sentence.lower().split()))


#--------------------------

#3 - Star pattern

for i in range(1, 6):
    print("*" * i)

#---------------------------------

#4 - Reverse integer using while

n = 1234
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print(rev)

#----------------------------------

