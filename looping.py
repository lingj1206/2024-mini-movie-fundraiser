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


MAX_TICKETS = 3

tickets_sold = 0

while tickets_sold < MAX_TICKETS:
    name = input("Please enter your name or 'xxx' to exit: ")

    if name == 'xxx':
        break

    tickets_sold += 1


if tickets_sold == MAX_TICKETS:
    print("you have sold all of the tickets")

else:
    print(f"you have sold {tickets_sold}. There are {MAX_TICKETS - tickets_sold} tickets left")


