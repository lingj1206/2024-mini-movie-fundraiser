# functions go here

# yes_no checker
def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            response = "yes"
            return response
        elif response == "no" or response == "n":
            response = "no"
            return response
        else:
            print("Please answer yes/no")


# makes sure that the user enters a name
def not_blank(question):
    while True:
        response = input(question)

        if response == "":
            print("this can't be left blank. enter your name")

        else:
            return response


def instructions():
    print("instructions go here")
# main routine goes here


# set max tickets
MAX_TICKETS = 3
# set number of tickets sold to 0
tickets_sold = 0

want_instructions = yes_no("Do you want to see instructions?: ")
print()

if want_instructions == "yes":
    instructions()


# loop to sell tickets
while tickets_sold < MAX_TICKETS:
    name = not_blank("enter your name or 'xxx' to exit: ")

    if name == 'xxx':
        break

    tickets_sold += 1

if tickets_sold == MAX_TICKETS:
    print("you have sold all of the tickets")

else:
    print(f"you have sold {tickets_sold}. There are {MAX_TICKETS - tickets_sold} tickets left")
