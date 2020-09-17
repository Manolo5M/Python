
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
        time.sleep(0.2)
        print("Name:", petName)
        time.sleep(0.2)
        print("Gender:", petGender)
        time.sleep(0.2)
        print("Age:", num1, "year/s old")
        
        break
    else:
        print("Invalid Input")
