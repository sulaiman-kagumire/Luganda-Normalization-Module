'''
LUGANDA TEXT NORMALIZATION MODULE
=================================

MEASUREMENT.PY
============

HOW IT WORKS:
-------------
This sub-module takes in one input; a number with a measurement token .

It breaks it into the number component and the measurement token component.

The measurement token is converted into its Luganda representation using the measurements dictionary 
and the number component is converted to its Luganda representation by using cardinals_orig.py.
'''

import cardinals_orig, re, sys

measurements = {
    "km":"kilo mita",
    "m":"mita",
    "cm":"senti mita",
    "mm":"milli mita",
    "ft":"futi",
    "kg":"kilo",
    "g":"guramu",
    "L":"lita",
    'mL':'milli lita',
    "'":"yinchi",
    'cc':'cubic senti mita',
    'miles':'mailo',
    'mph' : 'mita buli saawa',
    '%' : 'buli kikumi'

    
}
#checks for measurement tokens such as 45 km and normalises them 
def main(user_in):
    user_in = re.sub( " ","", user_in)
    #user_in = re.sub("\\.", "", user_in)
    user_in = re.sub("\\,", "", user_in)
    '''
    #print(user_in)
    curr = [key for key in measurements.keys()]
    s = None
    suffix = None
'''
    p = re.search(r'(\'|ft|miles|cc|inch|[kKHDdcm]?[mglL])', user_in).group(1)
    #print(p)
    
    n = re.search(r'(\d+\.\d+|\d+)', user_in).group(1)
    #print(n)
    suffix = measurements[p]

    if suffix != None:
        parts = re.findall(re.compile(r'\d+'), n)
        whole = cardinals_orig.main(parts[0])
        response = suffix + " " + whole
        if len(parts) > 1: 
            frac = cardinals_orig.main(parts[1])
            response += " n'obutundu " + frac
        return response

'''
    if suffix != None:
        response = suffix + " " + cardinals_orig.main(n)
        print(response, end = '')


    for i in curr:     
        j = "(.*)" + i
        try:
            s = re.search(j, user_in).group(1)
            print(s)
            suffix = measurements[i]
        except AttributeError as e:
            pass'''

def start(f):
    try:
        return main(f)
    except Exception as e:
        print(f)
        return ""

if __name__ == "__main__":
    items = ""
    for i in sys.argv[1:]:
        items += i
    try:
        print(main(items), end ='')
    except Exception as e:
        print(items, end = '')
     



