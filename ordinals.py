'''
LUGANDA TEXT NORMALIZATION MODULE
=================================

ORDINALS.PY
============

HOW IT WORKS:
-------------
This sub-module takes in one input; a number with a prefix and converts them into Luganda representation using the cards list.

'''

import cardinals_orig, re, sys, romannumeral, cardinals

cards = [
    ["asooka","ogusooka","erisooka","ekisooka","akasooka","okusooka"],
    ["ow'okubiri","ogw'okubiri","ery'okubiri","eky'okubiri","ak'okubiri","okw'okubiri","olw'okubiri",
    "ey'okubiri"],
    ["ow'okusatu","ogw'okusatu","ery'okusatu","eky'okusatu","ak'okusatu","okw'okusatu","olw'okusatu",
    "ey'okusatu"],
    ["ow'okuna","ogw'okuna","ery'okuna","eky'okuna","ak'okuna","okw'okuna","olw'okuna",
    "ey'okuna"],
    ["ow'okutaano","ogw'okutaano","ery'okutaano","eky'okutaano","ak'okutaano","okw'okutaano","olw'okutaano",
    "ey'okutaano"],
    ["ow'omukaaga","ogw'omukaaga","ery'omukaaga","eky'omukaaga","ak'omukaaga","okw'omukaaga","olw'omukaaga",
    "ey'omukaaga"],
    ["ow'omusanvu","ogw'omusanvu","ery'omusanvu","eky'omusanvu","ak'omusanvu","okw'omusanvu","olw'omusanvu",
    "ey'omusanvu"],
    ["ow'omunaana","ogw'omunaana","ery'omunaana","eky'omunaana","ak'omunaana","okw'omunaana","olw'omunaana",
    "ey'omunaana"],
    ["ow'omwenda","ogw'omwenda","ery'omwenda","eky'omwenda","ak'omwenda","okw'omwenda","olw'omwenda",
    "ey'omwenda"]
]

noun_classes = [
  '^om',
  '^er',
  '^ek',
  '^aka',
  '^oku',
  '^ogu',
  '^olu'
]

# english_regex = re.compile(r'(\d+(st|nd|rd|th)\s[a-zA-Z]+)')
wordchars = re.compile(r'([a-zA-Z0-9]+)')

def main(n):
      # num = int(re.findall(re.compile(r'\d+'),n)[0])
      num = romannumeral.rtn.romanToInt(n)
      if not isinstance(num, int):
            return num
      # print(num)
      # eng_word = re.findall(re.compile(r'[a-zA-Z]+'),n)[1]
      # print(eng_word)
      lug_num = cardinals_orig.main(num)
      # print(lug_num)
      if num == 1:
            return "omubereberye"
      elif num == 2 or num == 3:
            lug_num = "oku" + lug_num
            return " ow'" + lug_num
      elif num == 4:
            return "owokuna"
      elif num == 5:
            lug_num = "oku" + lug_num
            return " ow'" + lug_num
      elif 6 <= num <= 9:
            lug_num = "o" + lug_num
            return " ow'" + lug_num
      elif 10 <= num <= 19:
            lug_num = "e" + lug_num
            return " ow'" + lug_num
      elif num >= 20:
            # return " ow'" + lug_num
            return "ow'" + cardinals.get_response_from_noun_class_1(num)

def start(txt):
      words = re.findall(wordchars, str(txt))
      final_result = ""
      for word in words:
            result = main(word)
            final_result = re.sub(word, result, str(txt))
      return final_result

if __name__ == "__main__":
#   p = re.findall(english_regex, sys.argv[1])
  # print(p[0][0])
  print(start(sys.argv[1]))
  # print(p)
  # for i in range(len(p[0])):
