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


yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

