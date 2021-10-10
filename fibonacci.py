
nterms = 100

# uncomment to take input from the user
#nterms = int(input("How many terms? "))

# first two terms
a = 0
b = 1
cnt = 0

# check if the number of terms is valid
if nterm <= 0:
   print("Please enter a positive integer")
elif nterm == 1:
   print("Fibonacci Sequence upto",nterm,":")
   print(a)
else:
   print("Fibonacci Sequence upto",nterm,":")
   while cnt < nterm:
       print(a,end=' , ')
       nth = a + b
       # update values
       a = b
       b = nth
cnt += 1
