

def even ():
    print('It is an even number.')

def odd ():
        print('It is an odd number.')


number = int(input("Enter a number: "))

if number ==0:
      print('It is not odd or even!')

elif number %2==0:
      even()
else:
      odd()            