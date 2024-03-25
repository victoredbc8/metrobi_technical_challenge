# A() represents Achilles positon and T() represents the Tortoise position
# the number above them is the distance between them
import time

achilles = 0
tortoise = 100
print("The distance betwen Achilles and the tortoise are 100m.")

while True:
    distance = tortoise - achilles
    print(f'                         ({distance})                           ')
    print(f'A({achilles:.15f})---------------------------------T({tortoise:.15f})')

    timeTaken = distance/10
    achilles += distance
    
    benRan = timeTaken * 2 
    tortoise += benRan

    time.sleep(1)