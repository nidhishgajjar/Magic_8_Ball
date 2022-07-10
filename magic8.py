import random 

answer = ""
random_number = random.randint(1, 9)

if random_number == 1:
  answer = 'Yes - definately.'
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doutful."
else:
  answer = "Error"


name = input("\nPlease enter your name below.\n")
print('\nWelcome {0} we are excited to predict the future for you.\n'.format(name))
question = input('Ask something and we will provide our prediction.\n')
print("\n" + str(name)+ " asks: "+str(question) + '\n')
print("Magic 8-Ball's answer: " +str(answer)+ "\n\n")
