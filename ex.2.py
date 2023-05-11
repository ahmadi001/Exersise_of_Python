print('=================Welcome to the game=================')


user = str(input('Are you ready? \n'))
if user.upper()=='YES':
 score=0

 def score_c ():
    global score 
    score = score+1
    
    




 q1= str(input('Which city is the capital of Afghanistan?\n'))

 if q1=='kabul' or q1 == 'KABUL':
           score_c ()
    

 else:
        print('your answer is incorrect!')    

    
 q2= str(input('In which continent Afghanistan located?\n'))

 if q2=='asia' or q1 == 'ASIA':
       score_c ()
 else:
      print('your answer is incorrect!') 

 q3= int(input(' How many provinces Afghanistan has?\n'))
 if q3==34:
       score_c ()
 else:
        print('your answer is incorrect!') 


 print("Your total score is ", score)    

elif user.upper()=='NO':
      print('Prgram exit')
else:
      print('Unvalid input!')