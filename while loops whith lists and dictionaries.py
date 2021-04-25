# lets begin:

unconfirmed_rabits = ['pico', 'rabit_girl', 'rabit_boy']  # list with unconfirmed rabits
confirmed_rabits = []  # empty list with confirmed rabbits

while unconfirmed_rabits:
    current_rabbit = unconfirmed_rabits.pop()

    print(f"lets veryfy the rabbits list: {current_rabbit.title()}")

    confirmed_rabits.append(current_rabbit)

    for current_rabbit in confirmed_rabits:
        print(current_rabbit)

# new one to practice: swimming pool users:

swimming_pool_with_users = ['santpedor', 'manresa', 'solsona', 'vic']  # full list
swimming_pool_without_users = []  # empty list

while swimming_pool_with_users:  # while loop

    new_swim_users = swimming_pool_with_users.pop()

    print(f"verifing users: {new_swim_users.title()}")

    swimming_pool_without_users.append(new_swim_users)
    print("these swimming pool users have been confirmed:")

    for swimming in swimming_pool_without_users:
        print(f"confirmed users: {swimming.title()}")
        print("")

# removing all instances of specific values from a list:

horses = ['horse01', 'horse02', 'horse03', 'bird']
print(horses)

while 'bird' in horses:
    horses.remove('bird')
    print(horses)

tv_brands = ['samsung', 'lg', 'sony', 'radio']

while 'radio' in tv_brands:
    tv_brands.remove('radio')
    print(tv_brands)

animals = ['cat', 'dog', 'cat', 'iguana', 'parrot', 'cat']

while 'cat' in animals:  # the while loop says: while the word parrot is in the list
    animals.remove('cat')  # the parrot word will be removed from the animals list
    print(animals)  # print the newly updated list without the 'parrot' word

cars = ['seat', 'fiat', 'mercedes', 'fiat', 'fiat']
print(cars)

while 'fiat' in cars:
    cars.remove('fiat')
    print(cars)

# filling a dictionary with user input:

responses = {}

polling_active = True

while polling_active:
    name = input("what is your name?")
    response = input("which mountain would you like to climb today?")

    responses[name] = response

    repeat = input("would you like to let another person respond?(yes/no)")
    if repeat == 'no':
        polling_active = False

    for name, response in responses.items():
        print(f"{name} would you like to climb {response}")




















responses = {}

polling_active = True


while polling_active:

    name = ("com et dius nano?")
    mountain = ("a quina muntanya vols pujar?")

    
