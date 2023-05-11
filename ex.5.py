
print('=========Welcome to money machine=========\n\n\n')

exchange_rates = {
    "Ghana Cedi" : 12.94,
    "Mexican Peso" : 19.84,
    "Nigerian Naira" : 507.08,
    "Swiss Franc" : 0.98,
    "US Dollar" : 0.91,
}


while True:
    user_currancy=input('Enter the currancy to convert: ')
    amount_euro=float(input('Enter the amount in Euro to convert:'))

    converted= amount_euro * exchange_rates.get(user_currancy,0)

    print('Your converted amount:',converted, user_currancy)



