'''
LUGANDA TEXT NORMALIZATION MODULE
=================================

CARDINALS_ORIG.PY
============

HOW IT WORKS:
-------------
This module takes in one input; a number.

It factorizes the number by using a reversed list's indices (e.g.1265 is converted to ['5','6','2','1'])
and further breaks long numbers into groups of 3 depending on the place value e.g.
the number 12345676543 can be re-written to 12,345,676,543. This program does this like
['543','676','345','12'] as a Python list.

After, it uses the lists below to translate the entire number into Luganda.

NB: This module converts only integers in the range [0, 1e9)
'''

#!/usr/bin/env python3

import sys, re

ones = [
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

rones = [
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
    if l[i] == 0 and i < 6: continue
    
    if i == 0: y = ones[l[i]]
    
    elif i == 1: 
      if l[i] == 1: y = rones[l[i-1]]
      elif y == "": y = tens[l[i]]
      else: y = tens[l[i]] +  " mu " + y
      
    elif i == 2: 
      if y == "": y = hundreds[l[i]]
      else: y = hundreds[l[i]] +  " mu " + y
      
    elif i == 3: 
      if y == "": y = thousands[l[i]]
      else: y = thousands[l[i]] +  " mu " + y

    elif i == 4:
      if y == "": y = ten_thousands[l[i]]
      else: y = ten_thousands[l[i]] + " mu " + y

    elif i == 5:
      if y == "": y = hundred_thousands[l[i]]
      else: y = hundred_thousands[l[i]] + " mu " + y

    # check for millions 
    elif i == 6:
      L = len(str(a[2]))
      if L == 1:
        if (y == ""): y = millions[l[i]]
        else: y = millions[l[i]] + " mu " + y
      elif L == 2 or L == 3:
        M = to_reversed_list(a[2])
        if (y == ""): y = "obukadde " + factors(M, [])
        else: y = "obukadde " + factors(M, []) + " mu " + y
  
    # check for billions
    elif i == 9:
      L = len(str(a[3]))
      if L == 1:
        if y == "": y = billions[l[i]]
        else: y = billions[l[i]] + " mu " + y
      if L == 2 or L == 3:
        B = to_reversed_list(a[3])
        if y == "": y = "obuwumbi " + factors(B, [])
        else: y = "obuwumbi " + factors(B, []) + " mu " + y

  return y

def main(n):  
    l, a = converter(n)
    return factors(l, a)

def start(n):
  return main(n)

if __name__ == "__main__":
     print(main(sys.argv[1]))