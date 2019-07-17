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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# =-=-=-=-=-=-=-=-=-=
# =     Part A      =
# =-=-=-=-=-=-=-=-=-=

area_codes = []
calls_made = 0
banga_banga = 0

for record in calls:
    calling = record[0]
    if "(080)" == calling[:5:]:
        calls_made += 1
        receiving = record[1]

        if "(080)" == receiving[:5:]:
            banga_banga += 1

        if receiving[0] == '(' and receiving[1] == '0':
            poss = receiving.find(')')
            area = receiving[1:poss:]

            if area not in area_codes:
                area_codes.append(area)

        if receiving[0] in ['7', '8', '9']:
            area = receiving[:4:]
            if area not in area_codes:
                area_codes.append(area)

        if '140' == receiving[:3:]:
            area = receiving[:4:]
            if area not in area_codes:
                area_codes.append(area)

print("The numbers called by people in Bangalore have codes:")
area_codes.sort()
for element in area_codes:
    print(element)


# =-=-=-=-=-=-=-=-=-=
# =    Part B       =
# =-=-=-=-=-=-=-=-=-=

percent = (banga_banga * 100) / calls_made

print(" {0:.2f} percent of calls from fixed lines in Bangalore are calls "
      "to other fixed lines in Bangalore".format(percent))
