#1 Prime number check

n = 29
for i in range(2, int(n**0.5)+1):
    if n % i == 0:
        print(False)
        break
else:
    print(True)

#-----------------------------

# 2 Fibonacci series

a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b
#----------------------------------

#3 - Factorial

n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)

#-----------------------------------

#4 Armstrong number

n = 153
print(sum(int(d)**3 for d in str(n)) == n)


#---------------------------------

#5 Sum of digits

n = 987
print(sum(int(d) for d in str(n)))








