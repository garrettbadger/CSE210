def main():
    age_1 = int(input("What is the age of the first rider?"))
    height_1 = int(input("What is the height of the first rider?"))
    riders = input("Is there a second rider?")
    choice(riders, age_1, height_1)

def choice(riders, age_1, height_1):
    if riders == "yes":
        age_2 = int(input("What is the age of the second rider?"))
        height_2 = int(input("What is the height of the second rider?"))
        if height_1 and height_2 >= 36:

            if age_1 >= 18 or age_2 >= 18:
                print("Congratulation! You can ride this ride!")
            else:
                print("Sorry! You are not qualified to ride this ride.")
        else:
            print("Sorry! You are not qualified to ride this ride.")
    elif age_1 >= 18:
        if height_1 >= 62:
            print("Congratulation! You can ride this ride!")
        else:
            print("Sorry! You are not qualified to ride this ride.")
    else:
        print("Sorry! You are not qualified to ride this ride.")



main()