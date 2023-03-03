n = int(input("Enter the number of terms: "))
# first two terms 
t1, t2 = 0, 1
count = 0

# Check if the number of terms is valid
if n <= 0:
   print("Please enter a positive interger")
elif n == 1:
   print("Fibonacci sequence up to ",n,":")
   print(t1)
else 
   print("Fibonacci Sequence")
   while count < n:
   nth = t1 + t2
   # update values 
   t1 = t2
   t2 = nth
   count += 1
