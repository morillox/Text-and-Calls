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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

ans_arr = []
msg_interact = []
telemarketers = []

for record in calls:
    receiver = record[1]
    if receiver not in ans_arr:
        ans_arr.append(receiver)

for record in texts:
    text_usr = record[0]
    reader = record[1]

    if text_usr not in msg_interact:
        msg_interact.append(text_usr)
    if reader not in msg_interact:
        msg_interact.append(reader)

for record in calls:
    is_it = record[0]
    if (is_it not in ans_arr) and (is_it not in msg_interact):
        telemarketers.append(is_it)

telemarketers = list(set(telemarketers))
telemarketers.sort()
print(*telemarketers, sep="\n")
