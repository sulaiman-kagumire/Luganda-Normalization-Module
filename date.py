'''
LUGANDA TEXT NORMALIZATION MODULE
=================================

DATE.PY
============

HOW IT WORKS:
-------------
This sub-module takes in one input; the date.

It breaks it into the day component, the month component and the year component.

The day and year components are converted to their Luganda representation by using
cardinals_orig.py.

The month component is converted to it's Luganda representation with the use of the months list

The 3 components are combined to give the normalized date as output.

'''

import cardinals_orig, re, sys

months = [
  '',
  'ogusooka',
  'ogwokubiri',
  'ogwokusatu',
  'ogwokuna',
  'ogwokutaano',
  'ogwomukaaga',
  'ogwomusanvu',
  'ogwomunaana',
  'ogwomwenda',
  'ogwekkumi',
  'ogwekkuminogumu',
  'ogwekkuminebiri'
]
'''
months = [
  '',
  'Gatonnya',
  'Mukutulasanja',
  'Mugulansigo',
  'Kafumulampawu',
  'Muzigo',
  'Ssebo Aseka',
  'Kasambula',
  'Muwakanya',
  'Mutunda',
  'Mukulukusa Bitungotungo',
  'Museenene',
  'Ntenvu'
]
'''
months_eng = [
  '',
  'Jan',
  'Feb',
  'Mar',
  'Apr',
  'May',
  'Jun',
  'Jul',
  'Aug',
  'Sep',
  'Oct',
  'Nov',
  'Dec'
]
#matches months_eng list with English month short forms with the months list with Luganda months
mth = {i : j for i, j in zip(months_eng, months)}

def start(f):
  regex = re.compile(r'([a-zA-Z]{3}|\d{4}|\d{1,2})')
  g = re.findall(regex, f)
  y = cardinals_orig.main(g[2])
  d = cardinals_orig.main(g[0])
  try:
    month = months[int(g[1])]
  except ValueError as identifier:
    month = mth[g[1]]

  total_date = "nga " + d + " omwezi " + month + " " + y
  return total_date

#checks for date and normalises it to its Luganda representation
if __name__ == "__main__":
    f = sys.argv[1]
    regex = re.compile(r'([a-zA-Z]{3}|\d{4}|\d{1,2})')
    g = re.findall(regex, f)
    y = cardinals_orig.main(g[2])
    d = cardinals_orig.main(g[0])
    try:
      month = months[int(g[1])]
    except ValueError as identifier:
      month = mth[g[1]]

    total_date = "nga " + d + " omwezi " + month + " " + y
    print (total_date, end='')