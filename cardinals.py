'''
LUGANDA TEXT NORMALIZATION MODULE
=================================

CARDINALS.PY
============

HOW IT WORKS:
-------------
This sub-module takes in one input; a number.

It factorizes the number by using a reversed list's indices (e.g.1265 is converted to ['5','6','2','1'])
and further breaks long numbers into groups of 3 depending on the place value e.g.
the number 12345676543 can be re-written to 12,345,676,543. This program does this like
['543','676','345','12'] as a Python list.

After, it uses the lists below to translate the entire number into Luganda.

NB: This module converts decimals by converting the integer and fractional parts independently.
NB: This module outputs the number depending on the noun class of the word before it.
'''

#!/usr/bin/env python3

import sys, re

ones = [
  ['zeero'],
  ['emu','omu','gumu','limu','kimu','kumu','lumu','kamu'],
  ['bbiri','babiri','ebiri','abiri','bibiri','bubiri','abiri'],
  ['ssatu','basatu','esatu','asatu','bisatu','busatu','asatu'],
  ['nnya','bana','ena','ana','bina','buna','ana'],
  ['ttaano','bataano','etaano','ataano','bitaano','butaano','ataano'],
  ['mukaaga', 'mukaaga', 'mukaaga', 'mukaaga', 'mukaaga', 'mukaaga','mukaaga'],
  ['musanvu', 'musanvu', 'musanvu', 'musanvu', 'musanvu', 'musanvu','musanvu'],
  ['munaana', 'munaana', 'munaana', 'munaana', 'munaana', 'munaana','munaana'],
  ['mwenda', 'mwenda', 'mwenda', 'mwenda', 'mwenda', 'mwenda','mwenda']
]


rones = [
  ['kkumi', 'kkumi', 'kkumi', 'kkumi', 'kkumi', 'kkumi'],
  ['kkumi n\'emu',"kkumi n'omu","kkumi na gumu",
    'kkumi na limu','kkumi na kimu','kkumi na lumu','kkumi na kamu'],
  ['kkumi na bbiri', 'kkumi na babiri', 'kkumi na ebiri',
  'kkumi na abiri', 'kkumi na bibiri', 'kkumi na bbiri','kkumi na abiri'],
  ['kkumi na ssatu','kkumi na basatu','kkumi na esatu',
  'kkumi na asatu','kkumi na bisatu','kkumi na busatu','kkumi na asatu'],
  ['kkumi na nnya','kkumi na bana','kkumi na ena',
  'kkumi na ana','kkumi na bina','kkumi na buna','kkumi na ana'],
  ['kkumi na ttaano','kkumi na bataano','kkumi na etaano',
  'kkumi na ataano','kkumi na bitaano','kkumi na butaano','kkumi na ataano'],
  ['kkumi na mukaaga', 'kkumi na mukaaga', 'kkumi na mukaaga',
  'kkumi na mukaaga', 'kkumi na mukaaga', 'kkumi na mukaaga','kkumi na mukaaga'],
  ['kkumi na musanvu', 'kkumi na musanvu', 'kkumi na musanvu',
  'kkumi na musanvu', 'kkumi na musanvu', 'kkumi na musanvu','kkumi na musanvu'],
  ['kkumi na munaana', 'kkumi na munaana', 'kkumi na munaana',
  'kkumi na munaana', 'kkumi na munaana', 'kkumi na munaana','kkumi na munaana'],
  ['kkumi na mwenda', 'kkumi na mwenda', 'kkumi na mwenda',
  'kkumi na mwenda', 'kkumi na mwenda', 'kkumi na mwenda','kkumi na mwenda']
]

tens = [
  '', '',
  'abiri',
  'asatu',
  'ana',
  'ataano',
  'nkaaga',
  'nsanvu',
  'kinaana',
  'kyenda'
]

hundreds = [
  '',
  'kikumi',
  'bibiri',
  'bisatu',
  'bina',
  'bitaano',
  'lukaaga',
  'lusanvu',
  'lunaana',
  'lwenda'
]

thousands = [
  '',
  'lukumi',
  'nkumi bbiri',
  'nkumi ssatu',
  'nkumi nnya',
  'nkumi ttaano',
  'kakaaga',
  'kasanvu',
  'kanaana',
  'kenda'
]



ten_thousands = [
  '',
  'mutwaalo gumu',
  'emitwaalo ebiri',
  'emitwaalo esatu',
  'emitwaalo ena',
  'emitwaalo etaano',
  'emitwaalo mukaaga',
  'emitwaalo musanvu',
  'emitwaalo munaana',
  'emitwaalo mwenda'
]

hundred_thousands = [
 '',
 'akasiriivu kamu',
 'obusiriivu bubiri',
 'obusiriivu busatu',
 'obusiriivu buna',
 'obusiriivu butaano',
 'obusiriivu mukaaga',
 'obusiriivu musanvu',
 'obusiriivu munaana',
 'obusiriivu mwenda'
]

millions = [
  '',
  'kakadde kamu',
  'obukadde bubiri',
  'obukadde busatu',
  'obukadde buna',
  'obukadde butaano',
  'obukadde mukaaga',
  'obukadde musanvu',
  'obukadde munaana',
  'obukadde mwenda'
]

billions = [
  '',
  'kawumbi kamu',
  'obuwumbi bubiri',
  'obuwumbi busatu',
  'obuwumbi buna',
  'obuwumbi butaano',
  'obuwumbi mukaaga',
  'obuwumbi musanvu',
  'obuwumbi munaana',
  'obuwumbi mwenda'
]

noun_classes = [
  r'^[aA]ba.+',
  r'^[eE]m.+',
  r'^[aA]ma.+',
  r'^[eE]b.+',
  r'^[oO]bu.+',
  r'^[aA]ga.+'
]

# FACTORIZES THE NUMBER, n, INTO THE REVERESED LISTS
def converter(n):

    p = re.compile(r'\d{1,3}')
    l = list(str(n))

    l.reverse()

    a = ""

    for i in l:
      l[l.index(i)] = int(i)
      a = a + i

    a = re.findall(p, a)

    for i in a:
      b = list(i)
      b.reverse()
      x = ""
      for c in b: x = x + c
      a[a.index(i)] = int(x)

    return l, a
# utility method to convert a number into a reversed list of digits
def to_reversed_list(n):
  l = list(str(n))
  l.reverse()
  for i in l: l[l.index(i)] = int(i)
  return l

# CONVERTS FACTORIZED NUMBER INTO LUGANDA
def factors(l, a):
  y = ""
  N = len(l)
  for i in range(N):
    if l[i] == 0 and i < 6: continue # only for numbers < one million

    elif i == 1:
      if l[i] == 1:
        y = rones[l[i-1]]
      elif y == "": y = tens[l[i]]
      else: y = tens[l[i]] +  " mu " + y

    elif i == 2:
      if y == "": y = hundreds[l[i]]
      else:
        if type(y) == list:
          y = [hundreds[l[i]] +  " mu " + j for j in y]
        else:
          y = hundreds[l[i]] +  " mu " + y

    elif i == 3:
      if y == "": y = thousands[l[i]]
      else:
        if type(y) == list:
          y = [thousands[l[i]] +  " mu " + j for j in y]
        else:
          y = thousands[l[i]] +  " mu " + y

    elif i == 4:
      if y == "": y = ten_thousands[l[i]]
      else:
        if type(y) == list:
          y = [ten_thousands[l[i]] +  " mu " + j for j in y]
        else:
          y = ten_thousands[l[i]] + " mu " + y

    elif i == 5:
      if y == "": y = hundred_thousands[l[i]]
      else:
        if type(y) == list:
          y = [hundred_thousands[l[i]] +  " mu " + j for j in y]
        else:
          y = hundred_thousands[l[i]] + " mu " + y

    #check for millions
    elif i == 6:
      L = len(str(a[2]))
      if L == 1:
        if (y == ""): y = millions[l[i]]
        else:
          if type(y) == list:
            y = [millions[l[i]] +  " mu " + j for j in y]
          else:
            y = millions[l[i]] + " mu " + y
      elif L == 2 or L == 3:
        M = to_reversed_list(a[2])
        if (y == ""): y = "obukadde " + factors(M, [])
        else:
          if type(y) == list:
            y = ["obukadde " + factors(M, []) + " mu " + j for j in y]
          else:
            y = "obukadde " + factors(M, []) + " mu " + y

    # check for billions
    elif i == 9:
      L = len(str(a[3]))
      if L == 1:
        if y == "": y = billions[l[i]]
        else:
          if type(y) == list:
            y = [billions[l[i]] +  " mu " + j for j in y]
          else:
            y = billions[l[i]] + " mu " + y
      if L == 2 or L == 3:
        B = to_reversed_list(a[3])
        if y == "": y = "obuwumbi " + factors(B, [])
        else:
          if type(y) == list:
            y = ["obuwumbi " + factors(B, []) + " mu " + j for j in y]
          else:
            y = "obuwumbi " + factors(B, []) + " mu " + y

  return y

#checks for decimal numbers and converts each part to Luganda representation
def main(n):
    if '.' in str(n):
        nums = re.split(r'\.', n)
        nums.insert(1, " n'obutundu ")
        l, a = converter(nums[0])
        if (int(nums[0]) < 10):
          response = ones[int(nums[0])]
        elif (10 <= int(nums[0]) < 20):
          response = [rones[int(nums[0])-10]]
        else:
          if l[1] == 1:
            response = factors(l, a)
          else:
            response = [factors(l, a) + " mu " + i for i in ones[l[0]]]
        m, b = converter(nums[2])
        if (int(nums[2]) < 10):
          response2 = ones[int(nums[2])]
        elif (10 <= int(nums[2]) < 20):
          response2 = [rones[int(nums[2])-10]]
        else:
          if l[1] == 1:
            response2 = factors(m, b)
          else:
            response2 = [factors(m, b) + " mu " + i for i in ones[m[0]]]
        response = [j + " n'obutundu " + k for j, k in zip(response, response2)]
        return [response[-1]]

    else:
        l, a = converter(n)
        if (int(n) < 10):
          response = ones[int(n)]
        elif (10 <= int(n) < 20):
          response = rones[int(n)-10]
        else:
          if 1 <= l[0] <= 5:
            m = l[0]
            l[0] = 0
            response = [factors(l, a) + " mu " + i for i in ones[m]]
          else:
            response = factors(l, a)
        return response

# detects the word before the number and picks appropriate response depending on the word's noun class
def sorter(word, response):
  for i in noun_classes:
    j = noun_classes.index(i) + 1
    if re.search(i, word):
      if type(response) == str: return response
      elif len(response) == 1: return response[0]
      else: return response[j]
  if type(response) == str: return response
  elif len(response) == 1: return response[0]
  else: return response[0]

def get_response_from_noun_class_1(num):
    return sorter('abafirstclass', main(num))

def start(g):
  f = re.compile(r'([a-zA-z]+|\d{2,}\.\d{2,}|\d{2,}\.\d|\d\.\d{2,}|\d\.\d|\d{2,}|\d)')
  p = re.findall(f, g)
  k = sorter(p[0], main(p[1]))
  result = p[0] + " " + k
  return result

if __name__ == "__main__":
  f = re.compile(r'([a-zA-z]+|\d{2,}\.\d{2,}|\d{2,}\.\d|\d\.\d{2,}|\d\.\d|\d{2,}|\d)')
  p = re.findall(f, sys.argv[1])
  print(p)
  k = sorter(p[0], main(p[1]))
  print(p[0]+ " " + k, end='')
