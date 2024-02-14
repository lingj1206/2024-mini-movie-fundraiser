def not_blank(question):
    while True:
        response = input(question)

        if response == "":
            print("this can't be left blank. enter your name")

        else:
            return response


while True:
    name = not_blank("enter your name (or 'xxx' to quit)")

    if name == "xxx":
        break

print("done")
