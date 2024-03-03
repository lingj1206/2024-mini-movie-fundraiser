# functions go here

# checks that the user enters a valid response (yes or no,
# cash or credit) based on a list of options

def string_checker(question, num_letters, valid_responses):
    error = f"Please choose {valid_responses[0]} or {valid_responses[1]}"

    if num_letters == 1:
        short_version = 1
    else:
        short_version = 2

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:short_version] or response == item:
                return item

        print(error)


# makes sure that the user enters a name
def not_blank(question):
    while True:
        response = input(question)

        if response == "":
            print("this can't be left blank. enter your name")

        else:
            return response


# checks if what the user entered is a valid integer
def num_check(question):
    while True:
        error = "Please enter a valid number"
        try:
            response = int(input(question))
            return response
        except ValueError:
            print(error)


# calculates ticket prices
def calc_ticket_price(var_age):
    if var_age < 16:
        price = 7.5

    elif var_age < 65:
        price = 10.5

    else:
        price = 6.5

    return price


def instructions():
    print("instructions go here")
    print()


# main routine goes here


# set max tickets
MAX_TICKETS = 3
# set number of tickets sold to 0
tickets_sold = 0

yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

want_instructions = string_checker("Do you want to see instructions?: ", 1, yes_no_list)
print()

if want_instructions == "yes":
    instructions()

# loop to sell tickets
while tickets_sold < MAX_TICKETS:
    name = not_blank("enter your name or 'xxx' to exit: ")

    if name == 'xxx':
        break

    age = num_check("Age: ")

    if 12 <= age <= 120:
        pass

    elif age < 12:
        print("NO babies allowed, move along")
        print()
        continue
    else:
        print("shouldn't you be in a hospital bed")
        print()
        continue
    ticket_cost = calc_ticket_price(age)

    # get payment method
    pay_method = string_checker("Choose a payment method (cash or credit): ", 2, payment_list)
    print(f"you chose {pay_method}")

    tickets_sold += 1

if tickets_sold == MAX_TICKETS:
    print("you have sold all of the tickets")

else:
    print(f"you have sold {tickets_sold}. There are {MAX_TICKETS - tickets_sold} tickets left")
