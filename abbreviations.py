'''
LUGANDA TEXT NORMALIZATION MODULE
=================================

ABBREVIATIONS.PY
============

HOW IT WORKS:
-------------
This sub-module takes in one input; an abbreviation and expands it to its full Luganda representation using dictionaries.
'''
import sys

std = {
'Polof.':'Pulofeesa',
'Owek.':'owekitibwa', 
'Mw.' : 'Mwami',
'Omw.': 'Mwami',
'Omuky.':'Mukyala',
"n'omuky." : "Mukyala",
'Okjz':'Okugeza',
'Gavt' : 'Gavumenti',
'Gavt.' : 'Gavumenti',

'Fr.':'Faaza',
'Rev.':'Omwawule',
'Sr.':'Ssa',
'Br.':'Bulaaza',
'Pr.':'Musumba',
'Dr.':'Dokita',
'Gen.':'Jenero',
'Maj.':'Meeja',
'Col.':'KKano',
'Capt.':'Kaputeeni',
'Lt.':'Lutenanti',
'Brig.':'Buligeediya',
'Pvt.':'Pulayiveeti',

'TV':'Tivvi',
'CD':'Ssidi',
'DVD':'Ddivvidi',
'Rm':'Ekisenge',
'U-17': "Abali wansi w'emyaka kkumi na musanvu",
'U-18' : "Abali wansi w'emyaka kkumi na munaana",
'U-19' : "Abali wansi w'emyaka kkumi na mwenda",
'U-21' : "Abali wansi w'emyaka abiri mu gumu",
'U-23' : "Abali wansi w'emyaka abiri mu ssatu",
'P.7' : "ekibiina ky'omusanvu",
'P.6' : "ekibiina ky'omusanvu",
'M7' : 'Museveni',
'S.6' : "Senior ey'omukaaga"


}

abbreviations = {

'CBS':'Kyabbassa',
'FM':'Ffamma',
'NEMA': 'Nema',
'BUCADEF':'Bukadeefu',
'KCCA':'Kessissi E',
'UN':'Yu Eni',
'DP':'Ddippi',
"Gav't.":"Gavumenti",
'Gavt' : 'Gavumenti',
'M7':'Museveni',
'UPC':'Yuppissi',
'UPM': 'Yyupyemu',
'NRM':'Enaleemu',
'FDC':'Efuddissi',
'JEEMA':'Jeema',
'PLE':'Pyelo I',
'UCE':'Yussi I ',
'USE':'YusiI',
'UACE':'Yu ESsi I',
'UPE':'Yuppi I',
'NATO':'Nato',
'UTODA': 'Yutoda',
'URA':'Yu Ala E',
'UNRA':'Yunula',
'KCC':'Kessissi',


'U-17': "Abali wansi w'emyaka kkumi na musanvu",
'U-18' : "Abali wansi w'emyaka kkumi na munaana",
'U-19' : "Abali wansi w'emyaka kkumi na mwenda",
'U-21' : "Abali wansi w'emyaka abiri mu gumu",
'U-23' : "Abali wansi w'emyaka abiri mu ssatu",
'P.7' : "Ekibiina ky'omusanvu" ,
'P.6' : "Ekibiina ky'omusanvu"



}

import csv

def csv_file_reading(f):
      with open('abbreviations.csv') as fileobj:
        abbs = csv.reader(fileobj,delimiter=',',doublequote=False,quoting=csv.QUOTE_NONE)
        abbs = list(abbs)
        # print(abbs)
        s = f
        for line in abbs:
              if f == line[0]: 
                    # print(line[1],end='')
                    s = line[1]
                    break
        return s

def start(f):
    return csv_file_reading(f)
  # for key, value in abbreviations.items():
  #   if f == key:
  #     return(value)

#checks for abbreviation in the above std and abbreviations dictionaries
if __name__ == "__main__":
    s = csv_file_reading(sys.argv[1])
    print(s)
  # abb = sys.argv[1]
  # for key, value in abbreviations.items():
  #   if abb == key:
  #     print (value, end = '')