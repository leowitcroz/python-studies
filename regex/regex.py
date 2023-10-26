#Load Book
import re

with open ("miracle_in_the_andes.txt","r",encoding="utf-8") as file:
    book = file.read()


# print(book.count('Chapter'))

#with Regex

# How many chapters?


pattern = re.compile('Chapter [0-9]+')

findings = re.findall(pattern,book)
print(len(findings))

# Which are the senteces which love are used?

patter_word = re.compile('[A-Z]{1}[^.]*[^a-zA-Z]+love[^a-zA-Z]+[^.]*.') #^. means everything but a period

finded_senteces = re.findall(patter_word,book)

# print(finded_senteces)

# Wha are most used words?

patter_most_used_word = re.compile('[a-zA-Z]+')

words_used = re.findall(patter_most_used_word, book.lower())

d ={}

for word in words_used:
    if word in d.keys():
        d[word] = d[word] + 1
    else:
        d[word] = 1
    
d_list = [(value,key) for (key,value) in d.items()]



print(sorted(d_list, reverse=True))


