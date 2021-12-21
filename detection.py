'''
LUGANDA TEXT NORMALIZATION MODULE
=================================

DETECTION.PY (DETECTION AND CONVERSION MODULE)
============

HOW IT WORKS:
-------------

This program is the core component of the normalization module.
It takes two arguments as input i.e. the input plain-text file to normalize
and the output directory where the normalised text will be written.

It then sequentially calls upon different sub-modules to perform the normalization
depending on what the sub-module does e.g. the time sub-module, time.py, is called
to convert non-standard time representations in the input file into standard Luganda
time representation.
The resulting output from each sub-module is then fed into the next sub-module in the
call sequence.

Finally, the resulting output is then written into a new plain-text file which will
be saved in the output directory specified by the user.

As the modules normalize the text, the tokens they convert are detected
with the use of regular expressions, and stored in lists to be printed later for
debugging purposes.

Example invocation:
python detection.py f luganda-txt.txt
python detection.py 'ffe abasinga'
'''

import pyperclip, re ,os, subprocess, os.path

# REGULAR EXPRESSIONS USED TO DETECT NON-STANDARD TEXT

phoneRegex2 = re.compile(r'(\+?[0-9]{1,3}[\s\-]?[0-9]{2,3}[\s\-]?[0-9]{3}[\s\-]?[0-9]{3}|[0-9]{4}[\s\-]?[0-9]{3}[\s\-]?[0-9]{3})')

dateRegex = re.compile(r'(\d{1,2}\s\w{3}\.?\s\d{4}|\d{1,2}[\/\-]+\d{1,2}[\/\-]+\d{2,4}|\d{1,2}\w{2}\s\w{3}\.?\s\d{4})')

#timeRegex = re.compile(r'\d{1,2}:\d{2}')
timeRegex = re.compile(r'\d{1,2}:\d{2}(:\d{2})?')

dollarRegex = re.compile(r'\$\d(?:\d+(?:[.,]?\d*)*)+|\€\d(?:\d+(?:[.,]?\d*)*)+|\£\d(?:\d+(?:[.,]?\d*)*)+')

currencyRegex = re.compile(r'(?:[A-Z]{3}\s)(?:\d+(?:[.,]?\d*)*)')

shillingRegex = re.compile(r'(?:\d+(?:[.,]?\d*)*)\/-|(?:\d+(?:[.,]?\d*)*)\/=')

percentageRegex = re.compile(r'\d+%|\d+.\d+%')

rangeRegex = re.compile(r'\d+-\d+(?:[\s.,])?\d*')

nounClassRegex = re.compile(r'([a-zA-Z]+)\s(\d{2,}\.\d{2,}|\d{2,}\.\d|\d\.\d{2,}|\d\.\d|\d{2,}|\d)')

numberRegex = re.compile(r'\d+')

measurementRegex = re.compile(r'(\d+\.\d+|\d+)(\s)?(\'|ft|miles|cc|inch|[kKHDdcm]?[mglL])')

abbRegex = re.compile(r'\b(?:[a-z]*[A-Z][a-z]*){2,}')

numberplateRegex = re.compile(r'([A-Z]{2,3}\s?\d+[A-Z]{1})')

import sys
import date, ranges, lugandatime, currency, phonenumber, measurement, abbreviations, ordinals, cardinals, cardinals_orig

def main(isFile, g=None, errors="ignore"):

    logString = ""
    if isFile:
        # Find matches in clipboard text.
        if g:
            path = g
        else:
            path=sys.argv[2]
        inputtext = path
        # INPUT PLAIN-TEXT FILE TO BE NORMALIZED
        src_file=os.path.basename(path)
        fo = open(path, 'r', errors='ignore').read()
    else:
        if g:
            fo = g
        else:
            # fo = sys.argv[2]
            fo = sys.argv[1]
        inputtext = fo

    pyperclip.copy(fo)
    text = str(pyperclip.paste())
    fo = text
    # matches = []
    phoneMatches = []
    dateMatches = []
    timeMatches = []
    currencyMatches = []
    percentageMatches = []
    rangeMatches = []
    measurementMatches = []
    abbsMatches = []
    nounClassMatches = []
    numbersMatches = []

    # NORMALIZATION CALL SEQUENCE
    q = "==================INPUT: " + inputtext + "============================="
    print(q)
    logString += q + "\n"
    for groups in dateRegex.findall(fo):
        print(groups)
        logString += groups + "\n"
        #result = subprocess.check_output(['python', 'date.py', groups])
        result = date.start(groups)
        #result = str(result, 'utf-8')
        print(result)
        logString += result + "\n"
        fo = re.sub(groups, result, str(fo))
        dateMatches.append(groups)

    for groups in rangeRegex.findall(fo):
        print(groups)
        logString += groups + "\n"
        #result = subprocess.check_output(['python', 'ranges.py', groups])
        result = ranges.start(groups)
        #result = str(result, 'utf-8')
        print(result)
        logString += result + "\n"
        fo = re.sub(groups, result, str(fo))
        rangeMatches.append(groups)

    for groups in timeRegex.findall(fo):
        print(groups)
        logString += groups + "\n"
        #result = subprocess.check_output(['python', 'lugandatime.py', groups])
        result = lugandatime.start(groups)
        #result = str(result, 'utf-8')
        print(result)
        logString += result + "\n"
        fo = re.sub(groups, result, str(fo))
        timeMatches.append(groups)

    for groups in dollarRegex.findall(fo):
        print(groups)
        logString += groups + "\n"
        #result = subprocess.check_output(['python', 'currency.py', groups])
        result = currency.start(groups)
        #result = str(result, 'utf-8')
        print(result)
        logString += result + "\n"
        fo = re.sub(groups, result, str(fo))
        currencyMatches.append(groups)

    for groups in currencyRegex.findall(fo):
        print(groups)
        logString += groups + "\n"
        #result = subprocess.check_output(['python', 'currency.py', groups])
        result = currency.start(groups)
        #result = str(result, 'utf-8')
        if result == None:
            result = ""
        print(result)
        logString += result + "\n"
        fo = fo.replace(groups, result)
        # fo = re.sub(groups, result, str(fo))
        currencyMatches.append(groups)

    for groups in shillingRegex.findall(fo):
        print(groups)
        logString += groups + "\n"
        #result = subprocess.check_output(['python', 'currency.py', groups])
        result = currency.start(groups)
        #result = str(result, 'utf-8')
        print(result)
        logString += result + "\n"
        fo = re.sub(groups, result, str(fo))
        currencyMatches.append(groups)

    for groups in measurementRegex.findall(fo):
        s = groups[0] + groups[1] + groups[2]
        print(s)
        logString += s + "\n"
        #result = subprocess.check_output(['python', 'measurement.py', s])
        result = measurement.start(s)
        #result = str(result, 'utf-8')
        print(result)
        logString += result + "\n"
        fo = re.sub(s, result, str(fo))
        measurementMatches.append(s)

    for groups in abbRegex.findall(fo):
        print(groups)
        logString += groups + "\n"
        #result = subprocess.check_output(['python', 'abbreviations.py', groups])
        result = abbreviations.start(groups)
        #result = str(result, 'utf-8')
        print(result)
        if result == None:
            result = ""
        logString += result + "\n"
        fo = re.sub(groups, result, str(fo))
        abbsMatches.append(groups)

    for groups in phoneRegex2.findall(fo):
        print(groups)
        logString += groups + "\n"
        #result = subprocess.ch eck_output(['python', 'phonenumber.py', groups])
        result = phonenumber.start(groups)
        #result = str(result, 'utf-8')
        print(result)
        logString += result + "\n"
        fo = fo.replace(groups, result)
        phoneMatches.append(groups)

    #for key, value in abbreviations.std.items():
        #fo = fo.replace(key,value)
        #fo = abbreviations.start(fo)

    # normalizing math symbols
    fo = fo.replace("+", "ggattako")
    # fo = fo.replace("-", "gyakko")
    fo = fo.replace("x", "emirundi")
    fo = fo.replace("=", "ofuna")

    for groups in nounClassRegex.findall(fo):
        s = groups[0] + " " + groups[1]
        print(s)
        logString += s + "\n"
        #result = subprocess.check_output(['python', 'cardinals.py', s])
        result = cardinals.start(s)
        #result = str(result, 'utf-8')
        print(result)
        logString += result + "\n"
        fo = re.sub(s, result, str(fo))
        nounClassMatches.append(s)

    for groups in numberRegex.findall(fo):
        s = str(groups)
        print(s)
        logString += s + "\n"
        result = cardinals_orig.start(s)
        print(result)
        logString += result + "\n"
        fo = re.sub(s, result, str(fo))
        numbersMatches.append(s)

    fo = ordinals.start(fo)

    # PRINT DETECTED TOKENS (FOR DEBUGGING)

    if len(phoneMatches) > 0:
        pyperclip.copy('\n'.join(phoneMatches))
        pd = 'PHONE NUMBERS DETECTED:'
        print(pd)
        logString += pd + "\n"
        print('\n'.join(phoneMatches))
        logString += '\n'.join(phoneMatches)

    if len(dateMatches) > 0:
        pyperclip.copy('\n'.join(dateMatches))
        pd = 'DATES DETECTED:'
        print(pd)
        logString += pd + "\n"
        print('\n'.join(dateMatches))
        logString += '\n'.join(dateMatches)

    if len(timeMatches) > 0:
        pyperclip.copy('\n'.join(timeMatches))
        pd = 'TIME DETECTED:'
        print(pd)
        logString += pd + "\n"
        print('\n'.join(timeMatches))
        logString += '\n'.join(timeMatches)

    if len(currencyMatches) > 0:
        pyperclip.copy('\n'.join(currencyMatches))
        pd = 'CURRENCIES DETECTED:'
        print(pd)
        logString += pd + "\n"
        print('\n'.join(currencyMatches))
        logString += '\n'.join(currencyMatches)

    if len(measurementMatches) > 0:
        pyperclip.copy('\n'.join(measurementMatches))
        pd = 'MEASUREMENTS DETECTED:'
        print(pd)
        logString += pd + "\n"
        print('\n'.join(measurementMatches))
        logString += '\n'.join(measurementMatches)

    if len(percentageMatches) > 0:
        pyperclip.copy('\n'.join(percentageMatches))
        pd = 'PERCENTAGES DETECTED:'
        print(pd)
        logString += pd + "\n"
        print('\n'.join(percentageMatches))
        logString += '\n'.join(percentageMatches)

    if len(rangeMatches) > 0:
        pyperclip.copy('\n'.join(rangeMatches))
        pd = 'RANGES DETECTED:'
        print(pd)
        logString += pd + "\n"
        print('\n'.join(rangeMatches))
        logString += '\n'.join(rangeMatches)

    if len(abbsMatches) > 0:
        pyperclip.copy('\n'.join(abbsMatches))
        pd = 'ABBREVIATIONS DETECTED:'
        print(pd)
        logString += pd + "\n"
        print('\n'.join(abbsMatches))
        logString += '\n'.join(abbsMatches)

    if len(nounClassMatches) > 0:
        pyperclip.copy('\n'.join(nounClassMatches))
        pd = 'NOUN CLASSES DETECTED:'
        print(pd)
        logString += pd + "\n"
        print('\n'.join(nounClassMatches))
        logString += '\n'.join(nounClassMatches)

    if len(numbersMatches) > 0:
        pyperclip.copy('\n'.join(numbersMatches))
        pd = 'NUMBERS DETECTED:'
        print(pd)
        logString += pd + "\n"
        print('\n'.join(numbersMatches))
        logString += '\n'.join(numbersMatches)

    else:
        pd = 'Nothing was found.'
        print(pd)
        logString += pd + "\n"

    # WRITE NORMALIZED TEXT TO OUTPUT DIRECTORY
    if isFile:
        dest_dir = os.path.dirname(path)
        #dest_dir=sys.argv[2]
        p=os.path.join(dest_dir, 'normalised-'+src_file)
        with open(p, 'w') as file:
            file.write(fo)
        logString += "\nNormalization Done\n"
        return logString
    else:
        response = ">>>>>>>>>>>: " + fo
        print(response)
        return response

def start(isFile, g):
    return main(isFile, g)

if __name__ == "__main__":
    isFile = False
    if len(sys.argv) > 1:
        if sys.argv[1] == "f":
            isFile = True
    main(isFile)
