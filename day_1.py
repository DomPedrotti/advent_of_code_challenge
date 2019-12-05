import pandas as pd
'''
Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

For example:

For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
For a mass of 1969, the fuel required is 654.
For a mass of 100756, the fuel required is 33583.
The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.

What is the sum of the fuel requirements for all of the modules on your spacecraft?
'''

def fuel_spent(mass):
    '''
    >>> fuel_spent(12)
    2
    >>> fuel_spent(14)
    2
    >>> fuel_spent(1969)
    654
    >>> fuel_spent(100756)
    33583
    '''
    return((mass//3) - 2)

modules = pd.read_csv('data_day_1.csv', names=['mass'])
fuel = modules.apply(fuel_spent).sum()
print(fuel)
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()