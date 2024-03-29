def prime_checker(number):
  is_prime = True
  #iterating on numbers other than 1 and number  
  for num in range(2,number):
    #prime number only divisible by 1 and number itself
    if number % num == 0:
    #if completely divisible by num other than 1 and itself then not prime
      is_prime = False

  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")
   
# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)
   