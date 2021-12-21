'''
LUGANDA TEXT NORMALIZATION MODULE
=================================

RANGES.PY
============

HOW IT WORKS:
-------------
This sub-module takes in one input; two numbers seperated by a hyphen e.g 12-15 and converts the hyphento Luganda representation .
'''
import re , sys
k = re.compile(r'\d+(\s)?-(\s)?\d+(?:[\s.,])?\d*')

def main(m):
    if re.search(k,m):
        g = re.sub('-',' ku ', m)
        return g
        
def start(f):
    try:
        return main(f)
    except Exception as e:
        print(f)

if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            print (main(sys.argv[1]), end = '')
    except Exception as e:
        print(sys.argv[1], end='')