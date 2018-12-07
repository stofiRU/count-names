# Function count_names takes one string, start as a parameter. The function returns
# a tuple (a, b) where a and b are the numbers of citizens that have a first and 
# middle name that starts with the string start, respectively.
# names: https://hagstofa.is/media/49531/names.json
import json
from urllib.request import urlopen
def count_names(start):
    f = urlopen('https://hagstofa.is/media/49531/names.json')
    jsondata = json.load(f)
    
    firstNameCount = 0
    secondNameCount = 0
    for j in jsondata:
        if j['Nafn'].startswith(start):
            firstNameCount += int(j['Fjoldi1'])
            secondNameCount += int(j['Fjoldi2'])
    return (firstNameCount, secondNameCount)

print(count_names('Þór'))
print(count_names('Bja'))
print(count_names('Wat'))
print(count_names('Snati'))