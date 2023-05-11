print('==========Welcome==========')
restaurants=[]
while True:
 
   print('Please choose your options>>>>')
   print('a: Add a restaurant ')  
   print('b: Remove a restaurant') 
   print('c: Show all restaurant')
   print('d: Exit the restaurant\n')


   user_choice=input('Please enter your choice: ')



   if user_choice.upper()=='A':
    resturant=input('Which restaurant do you want to recommend?\n')
    restaurants.append(resturant)

   elif user_choice.upper()=='B':
     resturant=input('Which restaurant do you want to remove?\n')
     restaurants.remove(resturant)

   elif user_choice.upper()=='C':
     print(restaurants)

   elif user_choice.upper()=='D':
     print('d: Exit the restaurant\n')

   else:
     print('Invalid input!')  
     





