tickets_sold = 0

while True:

    name = input("enter name / 'xxx' to quit: ")

    if name == "xxx":
        break

    age = int(input("Age: "))

    if 12 <= age <= 120:
        pass

    elif age < 12:
        print("NO babies allowed, move along")
        continue
    else:
        print("shouldn't you be in a hospital bed")
        continue
    tickets_sold += 1

print(f"you have sold {tickets_sold} tickets")
