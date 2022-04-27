print("Welcome to the prime number counter!")
starting_num = 1
ending_num = int(input("What number would you like to count through?: "))

for num in range(starting_num, ending_num + 1):
   
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

#! Alaina R.