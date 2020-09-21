
print("Select pet.")
print("Dog")
print("Katt")
print("Bird")

import time
import random

num1 = random.randint(1, 20)

while True:
    # Take input from the user
    choice = input("Enter Pet Type (Dog/Katt/Bird): ")
    if choice in ('Dog', 'Katt', 'Bird'):
        print("Select gender.")
        print("Male")
        print("Female")
        petGender = input("Choose pets gender (Male/Female): ")
        petName = input("Name the pet: ")
        
        time.sleep(0.4)
        print("Rendering your pet...")
        time.sleep(0.6)
        print("Your pet:")
        print("--------")
        time.sleep(0.2)
        print("Name:", petName)
        time.sleep(0.2)
        print("Gender:", petGender)
        time.sleep(0.2)
        print("Age:", num1, "year/s old")
        time.sleep(0.3)
        if choice == 'Katt':
            print(" /\_/\ ")
            time.sleep(0.3)
            print("( o.o )")
            time.sleep(0.3)
            print(" > ^ < ")
        elif choice == 'Dog':
            print("---------")
            print("Here is a picture if your dog:")
            time.sleep(0.3)
            print(",-.___,-.")
            time.sleep(0.3)
            print("\_/_ _\_/")
            time.sleep(0.3)
            print("  )O_O(")
            time.sleep(0.3)
            print(" { (_) }")
            time.sleep(0.3)
            print("  `-^-' ")
        elif choice == 'Bird':
            print("Fågel")
        
        break
    else:
        print("Invalid Input")
