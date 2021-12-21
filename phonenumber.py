'''
LUGANDA TEXT NORMALIZATION MODULE
=================================

PHONENUMBER.PY
============
This sub-module takes in one input; a phone number.

It converts a phone number it's Luganda representation by looping through the numbers list.
'''

import re, sys

numbers = [
  'zeero',
  'emu',
  'bbiri',
  'ssatu',
  'nnya',
  'ttaano',
  'mukaaga',
  'musanvu',
  'munaana',
  'mwenda'
]

def main(phoneNo):
  print(phoneNo)
  f = re.compile(r'(\+|\d)')
  l = re.findall(f,phoneNo)
  result = ''
  #deals with phone numbers with country code (e.g +256 754678925)
  for num in l:
    if num == '+': result += 'Kasalamba, '
    else: result += numbers[int(num)] + ', '

  result = result[:-2]
  #print(result, end ='')
  return result

def start(f):
  return main(f)

if __name__ == "__main__":
  items = ''
  if len(sys.argv) > 1:
    for i in sys.argv[1:]:
      items += i
    main(items)
