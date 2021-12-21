'''
LUGANDA TEXT NORMALIZATION MODULE
=================================

CURRENCY.PY
============

HOW IT WORKS:
-------------
This sub-module takes in one input; a number with a currency token/symbol .

It breaks it into the number component and the currency token component.

The currency token is converted into its Luganda representation using the currencies dictionary 
and the number component is converted to its Luganda representation by using cardinals_orig.py.
'''

import cardinals_orig, re, sys

currencies = {
    "currency" : {
    r'\$': "dolla",
    "USD" : "dolla",    
    "UGX": "Siringi za Uganda",
    "KES" : "Siringi za Kenya",
    "TSH" : "Siringi za Tanzania",
    "SSP" : "pawudi za south sudan",
    "R₣" : "Franc za Rwanda",
    "FBu" : "Franc za Burundi",
    "ZK" : "kwacha",
    "SD" : "pawundi za Sudan",
    "GH₵" : "Cedi",
    "P" :"pula",
    "₦" : "Naira",
    "Br" : "birr",
    "R" : "Rand",
    "KR" : "Krona",
    "£" : "pawudi",
    "€" : "euro",
    "FR" : "franc",
    "₽" : "Ruble",
    "₹": "Rupi",
    "AED" : "Dhiram",
    "DHS" : "Dhiram",
    "DH" : "Dhiram",
    "QR" : "Riyal",
    "₩" : "won",
    r"A\$" : "dolla za Australia",
    r"C\$" : "dolla za canada",
    r"Can\$" : "dolla za canada",
    "CAD" : "dolla za canada",
    r"S\$" : "dolla za singapore",
    "NZD" : "dolla za New Zealand",
    "CHF" : "Swiss Francs",
    "SFR" : "Swiss Francs",
    "RM" : "ringgit",
    "MYR" : "ringgit",
    "¥" : "Yen",
    "JPY" : "Yen",
    "￥" : "Yuan",
    "CNY": "Yuan"},
    "only": {"/=" : "Siringi za Uganda",
    "/-" : "Siringi za Uganda",
    "/ " : "Siringi za Uganda"}
    }

f = re.compile(r'\d+')
#checks for currency tokens such as £22 and normalises them 
def main(user_in):
    user_in = re.sub(r'\s',"", user_in)
    # user_in = re.sub(r'\$', "", user_in)
    user_in = re.sub(r'\,', "", user_in)
    #print(user_in)
    curr = [key for key in currencies.keys()]
    s = None
    suffix = None
    for k in curr:
        p = [key for key in currencies[k].keys()]
        if k == "currency":
            for i in p:
                j = i + "(.*)"
                try:
                    s = re.search(j.upper(), user_in.upper()).group(1)
                    suffix = currencies[k][i]
                except AttributeError as e:
                    pass
        elif k == "only":
            for i in p:
                j = "(.*)" + i
                try:
                    s = re.search(j.upper(), user_in.upper()).group(1)
                    if s != None:
                        suffix = currencies[k][i]
                        break
                except AttributeError as e:
                    pass
    if suffix != None:
        parts = re.findall(f, user_in)
        whole = cardinals_orig.main(parts[0])
        response = suffix + " " + whole
        if len(parts) > 1: 
            frac = cardinals_orig.main(parts[1])
            response += " ne nusu " + frac
        
        print(response, end='')
        return response

def start(f):
    return main(f)

if __name__ == "__main__":
    items = ""
    for i in sys.argv[1:]:
        items += i
    main(items)