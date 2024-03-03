# cash or credit checker
def cash_credit(question):
    while True:
        response = input(question).lower()
        if response == "cash" or response == "ca":
            response = "cash"
            return response
        elif response == "credit" or response == "cr":
            response = "credit"
            return response
        else:
            print("Please choose a valid payment method")


while True:

    payment_method = cash_credit("Choose a payment method (cash or credit): ")

    print("You chose ", payment_method)
