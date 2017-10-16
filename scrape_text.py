import urllib
from bs4 import BeautifulSoup
import re
import random

#bank
words = []
joined = " "

#extractor, display text
url = raw_input("enter full url for extraction: ")
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
[x.extract() for x in soup.find_all('script')]
text = soup.get_text(" ", strip=True)
print text
print " "

loop = 1
while loop == 1:
    #inputter
    input = raw_input("analyze: ")
    #analyzer
    if input != "":
        regex = r'[^.?!]*(?<=[.?\s!])'+input+'(?=[\s.?!])[^.?!]*[.?!]'
        result = re.findall(regex, text)
        print result
    if input == "":
        regex = r'([A-Z][^\.!?]*[\.!?])'
        result = re.findall(regex, text)
        sentence = random.choice(result)
        print sentence
    #adder
    final_input = raw_input("select: ")
    words.append(final_input)
    #shower
    print words
    #exiter
    if input == "  ":
        print " "
        print " ".join(words)
        print " "
        loop = 0
