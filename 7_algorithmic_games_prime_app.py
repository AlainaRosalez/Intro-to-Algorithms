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

#! Christian D.
import random
do_again = 'yes'
while do_again == 'yes':
    num = int(input( "what is your number"))
    counter = 1
    start = 1
    end = 100
    number = random.randrange(start,end)
    print(number)
    num_ans = str(input("big = b, small = s, correct = c"))
    while num_ans != "c":
        if num_ans == 's':
            counter = counter + 1
            start = number
            number = random.randrange(start, end)
            print(number)
            num_ans = str(input("big = b, small = s, correct = c"))
        elif num_ans == 'b':
            counter = counter + 1
            end = number
            number = random.randrange(start,end)
            print(number)
            num_ans = str(input("big = b, small = s, correct = c"))
        if num_ans == 'c':
            print('I have done it!', counter , 'times')
            do_again = str(input("do you want to play again?")) 
