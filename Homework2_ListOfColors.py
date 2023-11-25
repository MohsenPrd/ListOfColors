## Mohsen Pourdehghan

import random

colorsList= ['blue','red','yellow','green','black','white','gray','aqua','lime','orange']

for number in range(3):
    j= random.randint(0,len(colorsList)-1)
    print(colorsList[j])
    # Avoid duplicate colors
    colorsList.pop(j)
    ##
