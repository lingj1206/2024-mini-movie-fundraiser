import pandas
import random
from datetime import date


# functions go here

# checks that the user enters a valid response (yes or no,
# cash or credit) based on a list of options

def string_checker(question, num_letters, valid_responses):
    error = f"Please choose {valid_responses[0]} or {valid_responses[1]}"

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
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


# instructions
def instructions():
    print('''\n
***** Instructions *****

For each ticket, enter ...
- The person's name (can't be blank)
- Age (Between 12 and 128)
- Payment method (cash / credit)

When you have entered all the users, press 'xxx' to quit.

The program will them display the ticket details 
including the cost of each ticket, the total cost and the total profit

This information will also be automatically written to 
a text file

****************************************************
''')


# currency formatting function
def currency(x):
    return f"${x:.2f}"


# main routine goes here


# set max tickets
MAX_TICKETS = 5
# set number of tickets sold to 0
tickets_sold = 0

yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

# Lists to hold ticket details
all_names = []
all_ticket_costs = []
all_surcharge = []

# Dictionary used to create sata frame
mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": all_surcharge
}
want_instructions = string_checker("Do you want to see instructions?: ", 1, yes_no_list)
print()

if want_instructions == "yes":
    instructions()

# loop to sell tickets
while tickets_sold < MAX_TICKETS:
    name = not_blank("enter your name or 'xxx' to exit: ")

    if name == 'xxx' and len(all_names) <= 0:
        print("You must sell at least One ticket before quitting")
        continue
    elif name == 'xxx':
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

    if pay_method == "cash":
        surcharge = 0
    else:
        # calculate 5% surcharge if the user is paying by credit card
        surcharge = ticket_cost * 0.05

    tickets_sold += 1

    all_names.append(name)
    all_ticket_costs.append(ticket_cost)
    all_surcharge.append(surcharge)

mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# Calculate the total cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge']\
    + mini_movie_frame['Ticket Price']

# calculate the total profit for each ticket
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# Calculate ticket and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# choose winner and look up total won
winner_name = random.choice(all_names)
win_index = all_names.index(winner_name)
total_won = mini_movie_frame.at[win_index, 'Total']

# Currency Formatting (uses currency function)
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

mini_movie_frame = mini_movie_frame.set_index('Name')

# **** Get current date for heading and filename ****
# get today's date
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%y")

heading = f"---- Mini Movie Fundraiser Ticket Data ({day}/{month}/{year})"
filename = f"MMF_{year}_{month}_{day}"

# change frame to string so that we can export it to file
mini_movie_string = pandas.DataFrame.to_string(mini_movie_frame)

# create strings for printing
ticket_cost_heading = "\n---- Tic" \
                      "get Cost / Profit ----"
total_ticket_sales = f"Total Ticket sales: ${total}"
total_profit = f"total profit: ${profit}"

#
if tickets_sold == MAX_TICKETS:
    sales_status = "\n*** All the tickets have been sold ***"
else:
    sales_status = f"***8 you have sold {tickets_sold} out of {MAX_TICKETS} tickets ****"

winner_heading = "\n---- Raffle winner ----"
winner_text = f"The winner of the raffle is {winner_name}."\
    f"They have won ${total_won:.2sf}. ie: their ticket is free!"

# list holding content to print / write to file
to_write = [heading, mini_movie_string, ticket_cost_heading,
            total_ticket_sales, total_profit, sales_status,
            winner_heading, winner_text]

for item in to_write:
    print(item)

# write output to file
# create file to hold data (afdd .txt extension)
write_to = f"{filename}.txt"
text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# close file
text_file.close()
