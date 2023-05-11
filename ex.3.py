print('=================Welcome to the game=================')

while True:

  user=str (input('Do you want search treasure?\n'))

  if user.upper() == 'YES':

    user=str (input('a: at the beach \nb: in the mountains\n'))

    if user.upper() == 'A':
        user=str (input('You want to search in:\nc: in the water \nd: dig a hole in the sand\n'))

        if user.upper()=='C':
            print("You didn't find the treasure!\nYou just find an old skiny shoe. ")
        elif user.upper()=='D':
            print('Congratulation ! You found a treasure box with gold.')
        else:
         print('Unvalid input!')

    elif user.upper() == 'B':
         user=str (input('You want to search in:\ne: under a palm tree \nf: in a lake\n'))      
         if user.upper()=='E':
            print("You have got bit by snake!\nYou lost the game. ")
         elif user.upper()=='F':
            print('Congratulation ! You found a treasure box under water, but it is empty.')

         else:
           print('Unvalid input!')







  elif user.upper()=='NO':
      print('Prgram exit')
  else:
      print('Unvalid input!')
