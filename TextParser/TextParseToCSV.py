########################################################
#Created by John Hartman, IBM, Cyber Security Apprentice
########################################################

import re, csv

#This section starts by parsing the text to remove the email header garbage
filename = "./input.txt"
infile = open(filename, 'r')
lines = infile.readlines()
lines[0:13]

for line in lines:
    if re.match("TICKET NUMBER|OLD SOURCE IP|OLD SOURCE PORT|HOST IP|HOST PORT|EXPLOIT", line):
        print(line.strip())


#This section takes the new parsed text and formats it into a dictionary which is then used to read as CSV 
#This first fields line is what will come up as the header column in the CSV
fields = ["TICKET NUMBER", "OLD SOURCE IPIP", "OLD SOURCE PORT", "HOST IP", "HOST PORT", "EXPLOIT"]
re_valid_field = re.compile('|'.join(fields))

with open('input.txt') as f_input, open('output.csv', 'w', newline='') as f_output:
    csv_output = csv.DictWriter(f_output, fieldnames=fields, restval='')
    csv_output.writeheader()

    row = {}

    for line in f_input:
        if re_valid_field.match(line):
            key, sep, value = line.strip().partition(':')
            row[key.strip()] = value.strip()
        elif row:
            csv_output.writerow(row)
            row = {}

    # Any remaining row to be written?
    if row:
        csv_output.writerow(row)
