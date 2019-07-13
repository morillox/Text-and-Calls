"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

# First lest run the text messages to see how many different numbers we have and put them in
# an array to keep track of them.
arrNumbers = []
for each in texts:
    if each[0] not in arrNumbers:
        arrNumbers.append(each[0])
    if each[1] not in arrNumbers:
        arrNumbers.append(each[1])

# Second lest do the same we did for the text messages for the calls.
for talked in calls:
    if talked[0] not in arrNumbers:
        arrNumbers.append(talked[0])
    if talked[1] not in arrNumbers:
        arrNumbers.append(talked[1])

# Solution: the total of different numbers will be the length of both arrays.
print("There are {} different telephone numbers in the records.".format((len(arrNumbers))))

