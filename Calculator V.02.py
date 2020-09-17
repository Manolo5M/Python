#Enter the problem down below and then press "Run"

problem = (7919 ** 2 - 1) / 24
import time
import random
num1 = random.randint(0, 20)
num2 = random.randint(30, 50)
num3 = random.randint(60, 70)
num4 = random.randint(75, 90)

print("Calculating, please wait")
if problem > 100000:
    time.sleep(0.3)
    print(num1,"% is calculated...")
    time.sleep(0.3)
    print(num2,"% is calculated...")
    time.sleep(0.3)
    print(num3,"% is calculated...")
    time.sleep(0.6)
    print(num4,"% is calculated...")
    time.sleep(0.3)
    print(problem)
else:
    time.sleep(0.2)
    print(num1,"% is calculated...")
    time.sleep(0.1)
    print(num2,"% is calculated...")
    time.sleep(0.2)
    print(num3,"% is calculated...")
    print(problem)
time.sleep(2.5)
print("Made by Manlito")