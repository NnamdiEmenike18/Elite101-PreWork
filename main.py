import random
#This is a chatbot and this is a comment, not executed by the program
#Extend it to make the computer ask for your favourite movie and respond accordingly!

print('Hello this is your computer...what is your favourite number?')
#Declaring our first variable below called 'computerfavnumber' and storing the value 33
computerfavnumber= random.randint(1,100)
#We now declare a variable but set the variable to hold whatever the *user* inputs into the program
favNumber = input()
print(favNumber + ' ... is a very nice number indeed. So...what is your name?')
name = input()
print('what a lovely name:  ' + name + ' ... 4now, I will reveal what my favourite number is:')

print (computerfavnumber)

favcolour = input("Now, tell me, what is your favourite colour?")

print(favcolour + " ... Wow! That is my favourite colour too!") 


print("Lets play a game! I am thinking of a number between 1 and 20. Try to guess the number!")

guessesTaken = 0

number = random.randint(1, 20)

while guessesTaken < 3:
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is too high.')



if guess == number:
    guessesTaken = (guessesTaken)
    print('Good job! You guessed my number in ' + str(guessesTaken + ' guesses!'))

if guess != number:
    number = (number)
    print('Nope. The number I was thinking of was ' + str(number))

print("That was a fun game! BTW what is your best skill?")
bestskill=input()
print( bestskill + " ... that's good. My best skill is having tea")

answer = input("Is it your birthday?")
if answer == "yes":
  print("Happy Birthday to you!") 
  print("Happy Birthday to you!")
  print("Happy Birthday, dear " + name)
  #sleep for one second
  import time
  time.sleep(1)
  print ("Happy Birthday to you!")
#indlude other option for yes
elif answer == "Yes": 
  print("Happy Birthday to you!") 
  print("Happy Birthday to you!")
  print("Happy Birthday, dear " + name)
  #sleep for one second
  import time
  time.sleep(1)
  print ("Happy Birthday to you!")


else:
  input("when is it?")
  print ("okay ill keep that in mind!")


# 12 End Conversation
print("It was nice talking to you")
print("Have a good day! :)")

keepTalking = input('Do you want to countinue? (y/n)')

if keepTalking == 'n':
  print("Bye!")