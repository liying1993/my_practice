import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(raw_input())
# print l 4
h = int(raw_input())
# print h 5
text_source = raw_input()
# print text_source
ascii_rows = []
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ?'
for d in xrange(h):
    ascii_row = raw_input()
    # print ascii_row
    ascii_rows.append(ascii_row)
# print ascii_rows
output = ['']

for i in xrange(h - 1):
    output.append('')

# print output
for character in text_source:
    for idx, letter in enumerate(alphabet):
        if character.upper() == letter:
            for it in xrange(h):
                output[it] += ascii_rows[it][l * idx:l * (idx + 1)]
                # print output[it]
            break  # no reason to keep checking anything
    else:
        # wasn't found
        for it in xrange(h):
            output[it] += ascii_rows[it][l * idx:l * (idx + 1)]

# print output
for row in output:
    print row