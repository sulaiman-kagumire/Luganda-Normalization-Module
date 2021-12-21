'''
LUGANDA TEXT NORMALIZATION MODULE
=================================

TIME.PY
============

HOW IT WORKS:
-------------
This sub-module takes in one input; the time.

It breaks it into the hour component and the minutes component.

Each is converted to it's Luganda representation with the use of the "ones" and
"tens" lists, and combined to give the normalized time as output.
'''

import sys
# import re

ones = [
  '',
  'emu',
  'bbiri',
  'ssatu',
  'nnya',
  'ttaano',
  'mukaaga',
  'musanvu',
  'munaana',
  'mwenda',
  'kkumi',
  'kkumi n\'emu',
  'kkumi na bbiri',
  'kkumi na ssatu',
  'kkumi na nnya',
  'kkumi na ttaano',
  'kkumi na mukaaga',
  'kkumi na musanvu',
  'kkumi na munaana',
  'kkumi na mwenda'
]

tens = [
  '', '',
  'abiri',
  'asatu',
  'ana',
  'ataano'
]

#converts each time component to a number e.g 08 to munaana
def num_to_txt(num):
    if (num < 20):
        return ones[num]
    else:
        s = ""
        if ((num % 10) > 0): s = " mu " + num_to_txt(num % 10)
        return tens[num // 10] + s
#combines the hours and minutes time components and outputs it into Luganda representation 
def to_luganda_time(time_string):
    hhmm = time_string.split(':')
    hrs = num_to_txt(int(hhmm[0]))
    mins = num_to_txt(int(hhmm[1]))
    if (mins == ""): return hrs
    else: return  hrs + ' n\'eddakika ' + mins

n = sys.argv[1]

print(to_luganda_time(n), end='')