from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
import re
nltk.download('punkt')
from textstat import textstat
import openpyxl

with open("StopWords_Auditor.txt","r")as s:
    stop_words_1 = s.read()
    #print(stop_words_1)

with open("StopWords_Currencies.txt","r")as t:
    stop_words_2 = t.read()
    #print(stop_words_2)

with open("StopWords_DatesandNumbers.txt","r")as u:
    stop_words_3 = u.read()
    #print(stop_words_3)


with open("StopWords_Generic.txt","r")as v:
    stop_words_4 = v.read()
    #print(stop_words_4)

with open("StopWords_GenericLong.txt","r")as w:
    stop_words_5 = w.read()
    #print(stop_words_5)

with open("StopWords_Geographic.txt","r")as x:
    stop_words_6 = x.read()
    #print(stop_words_6)

with open("StopWords_Names.txt","r")as y:
    stop_words_7 = y.read()
    #print(stop_words_7)

with open("blackassign0001.txt","r") as f:
    text = f.read()

with open("positive-words.txt","r") as f:
    posit_text = f.read()

with open("negative-words.txt","r") as f:
    negat_text = f.read()
    

from nltk.tokenize import word_tokenize
tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
#print(tokenize_words)
#print(positive_text)
#print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                 without_stop_words.append(words)

#print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if  word in positive_text:
        positive_score =positive_score + 1

#print(positive_score)

negative_score = 0

for word in Filtered_text:
    if  word in negative_text:
        negative_score =negative_score - 1
        
negative_score = negative_score * -1
#print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
#print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text)+0.000001)
#print(subjective_score)

#average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
#print(average_sentence_length)

#percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
#print(percentage_of_complex_words)


#fog index
fog_index = 0.4*(average_sentence_length + percentage_of_complex_words)
#print(fog_index)

#average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
#print(average_number_of_words_per_sentence)

#complex word count
complex_word_count = (textstat.polysyllabcount(text))

#word count
stop_words = set(stopwords.words('english'))

pure_text =[]
for word in stop_words:
    if word not in  text:
        pure_text.append(word)
pure = str(pure_text)

word_count =  textstat.lexicon_count(pure, removepunct=True)
#print(word_count)

#syllable count
syllable_count = textstat.syllable_count(text)
#print(syllable_count)

#pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
#print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))


#average word length

average_word_length = textstat.avg_character_per_word(text)
#print(average_word_length)

workbook = openpyxl.Workbook()
sheet = workbook.active
sheet['A1'.title()] = 'URL_ID'
sheet['B1'.title()] = 'URL'
sheet['C1'.title()] = 'POSITIVE SCORE'
sheet['D1'.title()] = 'NEGATIVE SCORE'
sheet['E1'.title()] = 'POLARITY SCORE'
sheet['F1'.title()] = 'SUBJECTIVE SCORE'
sheet['G1'.title()] = 'AVG SENTENCE LENGTH'
sheet['H1'.title()] = 'PERCENTAGE OF COMPLEX WORDS'
sheet['I1'.title()] = 'FOG INDEX'
sheet['J1'.title()] = 'AVG NUMBER OF WORDS PER SENTENCE'
sheet['K1'.title()] = 'COMPLEX WORD COUNT'
sheet['L1'.title()] = 'WORD COUNT'
sheet['M1'.title()] = 'SYLLABLE PER WORD'
sheet['N1'.title()] = 'PERSONAL PRONOUNS'
sheet['O1'.title()] = 'AVG WORD LENGTH'

sheet['A2'].value = "blackassign0001"
sheet['B2'].hyperlink = 'https://insights.blackcoffer.com/rising-it-cities-and-its-impact-on-the-economy-environment-infrastructure-and-city-life-by-the-year-2040-2/'
sheet['C2'].value = positive_score
sheet['D2'].value = negative_score
sheet['E2'].value = polarity
sheet['F2'].value = subjective_score
sheet['G2'].value = average_sentence_length
sheet['H2'].value = percentage_of_complex_words
sheet['I2'].value = fog_index
sheet['J2'].value = average_number_of_words_per_sentence
sheet['K2'].value = complex_word_count
sheet['L2'].value = word_count
sheet['M2'].value = syllable_count
sheet['N2'].value = pronouns_count
sheet['O2'].value = average_word_length





#------------------TEXT - 2-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0002.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A3'].value = "blackassign0002"
sheet['B3'].hyperlink = 'https://insights.blackcoffer.com/rising-it-cities-and-their-impact-on-the-economy-environment-infrastructure-and-city-life-in-future/'
sheet['C3'].value = positive_score
sheet['D3'].value = negative_score
sheet['E3'].value = polarity
sheet['F3'].value = subjective_score
sheet['G3'].value = average_sentence_length
sheet['H3'].value = percentage_of_complex_words
sheet['I3'].value = fog_index
sheet['J3'].value = average_number_of_words_per_sentence
sheet['K3'].value = complex_word_count
sheet['L3'].value = word_count
sheet['M3'].value = syllable_count
sheet['N3'].value = pronouns_count
sheet['O3'].value = average_word_length

#------------------TEXT - 3-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0003.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A4'].value = "blackassign0003"
sheet['B4'].hyperlink = 'https://insights.blackcoffer.com/internet-demands-evolution-communication-impact-and-2035s-alternative-pathways/'
sheet['C4'].value = positive_score
sheet['D4'].value = negative_score
sheet['E4'].value = polarity
sheet['F4'].value = subjective_score
sheet['G4'].value = average_sentence_length
sheet['H4'].value = percentage_of_complex_words
sheet['I4'].value = fog_index
sheet['J4'].value = average_number_of_words_per_sentence
sheet['K4'].value = complex_word_count
sheet['L4'].value = word_count
sheet['M4'].value = syllable_count
sheet['N4'].value = pronouns_count
sheet['O4'].value = average_word_length

workbook.save("Output Data Structure.xlsx")


#------------------TEXT - 3-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0004.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A5'].value = "blackassign0004"
sheet['B5'].hyperlink = 'https://insights.blackcoffer.com/rise-of-cybercrime-and-its-effect-in-upcoming-future/'
sheet['C5'].value = positive_score
sheet['D5'].value = negative_score
sheet['E5'].value = polarity
sheet['F5'].value = subjective_score
sheet['G5'].value = average_sentence_length
sheet['H5'].value = percentage_of_complex_words
sheet['I5'].value = fog_index
sheet['J5'].value = average_number_of_words_per_sentence
sheet['K5'].value = complex_word_count
sheet['L5'].value = word_count
sheet['M5'].value = syllable_count
sheet['N5'].value = pronouns_count
sheet['O5'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0005.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A6'].value = "blackassign0005"
sheet['B6'].hyperlink = 'https://insights.blackcoffer.com/ott-platform-and-its-impact-on-the-entertainment-industry-in-future/'
sheet['C6'].value = positive_score
sheet['D6'].value = negative_score
sheet['E6'].value = polarity
sheet['F6'].value = subjective_score
sheet['G6'].value = average_sentence_length
sheet['H6'].value = percentage_of_complex_words
sheet['I6'].value = fog_index
sheet['J6'].value = average_number_of_words_per_sentence
sheet['K6'].value = complex_word_count
sheet['L6'].value = word_count
sheet['M6'].value = syllable_count
sheet['N6'].value = pronouns_count
sheet['O6'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0006.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A7'].value = "blackassign0006"
sheet['B7'].hyperlink = 'https://insights.blackcoffer.com/the-rise-of-the-ott-platform-and-its-impact-on-the-entertainment-industry-by-2040/'
sheet['C7'].value = positive_score
sheet['D7'].value = negative_score
sheet['E7'].value = polarity
sheet['F7'].value = subjective_score
sheet['G7'].value = average_sentence_length
sheet['H7'].value = percentage_of_complex_words
sheet['I7'].value = fog_index
sheet['J7'].value = average_number_of_words_per_sentence
sheet['K7'].value = complex_word_count
sheet['L7'].value = word_count
sheet['M7'].value = syllable_count
sheet['N7'].value = pronouns_count
sheet['O7'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0007.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A8'].value = "blackassign0007"
sheet['B8'].hyperlink = 'https://insights.blackcoffer.com/rise-of-cyber-crime-and-its-effects/'
sheet['C8'].value = positive_score
sheet['D8'].value = negative_score
sheet['E8'].value = polarity
sheet['F8'].value = subjective_score
sheet['G8'].value = average_sentence_length
sheet['H8'].value = percentage_of_complex_words
sheet['I8'].value = fog_index
sheet['J8'].value = average_number_of_words_per_sentence
sheet['K8'].value = complex_word_count
sheet['L8'].value = word_count
sheet['M8'].value = syllable_count
sheet['N8'].value = pronouns_count
sheet['O8'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0008.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A9'].value = "blackassign0008"
sheet['B9'].hyperlink = 'https://insights.blackcoffer.com/rise-of-internet-demand-and-its-impact-on-communications-and-alternatives-by-the-year-2035-2/'
sheet['C9'].value = positive_score
sheet['D9'].value = negative_score
sheet['E9'].value = polarity
sheet['F9'].value = subjective_score
sheet['G9'].value = average_sentence_length
sheet['H9'].value = percentage_of_complex_words
sheet['I9'].value = fog_index
sheet['J9'].value = average_number_of_words_per_sentence
sheet['K9'].value = complex_word_count
sheet['L9'].value = word_count
sheet['M9'].value = syllable_count
sheet['N9'].value = pronouns_count
sheet['O9'].value = average_word_length

workbook.save("Output Data Structure.xlsx")




#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0009.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A10'].value = "blackassign0009"
sheet['B10'].hyperlink = 'https://insights.blackcoffer.com/rise-of-cybercrime-and-its-effect-by-the-year-2040-2/'
sheet['C10'].value = positive_score
sheet['D10'].value = negative_score
sheet['E10'].value = polarity
sheet['F10'].value = subjective_score
sheet['G10'].value = average_sentence_length
sheet['H10'].value = percentage_of_complex_words
sheet['I10'].value = fog_index
sheet['J10'].value = average_number_of_words_per_sentence
sheet['K10'].value = complex_word_count
sheet['L10'].value = word_count
sheet['M10'].value = syllable_count
sheet['N10'].value = pronouns_count
sheet['O10'].value = average_word_length

workbook.save("Output Data Structure.xlsx")


#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0010.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A11'].value = "blackassign0010"
sheet['B11'].hyperlink = 'https://insights.blackcoffer.com/rise-of-cybercrime-and-its-effect-by-the-year-2040/'
sheet['C11'].value = positive_score
sheet['D11'].value = negative_score
sheet['E11'].value = polarity
sheet['F11'].value = subjective_score
sheet['G11'].value = average_sentence_length
sheet['H11'].value = percentage_of_complex_words
sheet['I11'].value = fog_index
sheet['J11'].value = average_number_of_words_per_sentence
sheet['K11'].value = complex_word_count
sheet['L11'].value = word_count
sheet['M11'].value = syllable_count
sheet['N11'].value = pronouns_count
sheet['O11'].value = average_word_length

workbook.save("Output Data Structure.xlsx")


#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0011.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A12'].value = "blackassign0011"
sheet['B12'].hyperlink = 'https://insights.blackcoffer.com/rise-of-internet-demand-and-its-impact-on-communications-and-alternatives-by-the-year-2035/'
sheet['C12'].value = positive_score
sheet['D12'].value = negative_score
sheet['E12'].value = polarity
sheet['F12'].value = subjective_score
sheet['G12'].value = average_sentence_length
sheet['H12'].value = percentage_of_complex_words
sheet['I12'].value = fog_index
sheet['J12'].value = average_number_of_words_per_sentence
sheet['K12'].value = complex_word_count
sheet['L12'].value = word_count
sheet['M12'].value = syllable_count
sheet['N12'].value = pronouns_count
sheet['O12'].value = average_word_length

workbook.save("Output Data Structure.xlsx")


#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0012.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A13'].value = "blackassign0012"
sheet['B13'].hyperlink = 'https://insights.blackcoffer.com/rise-of-telemedicine-and-its-impact-on-livelihood-by-2040-3-2/'
sheet['C13'].value = positive_score
sheet['D13'].value = negative_score
sheet['E13'].value = polarity
sheet['F13'].value = subjective_score
sheet['G13'].value = average_sentence_length
sheet['H13'].value = percentage_of_complex_words
sheet['I13'].value = fog_index
sheet['J13'].value = average_number_of_words_per_sentence
sheet['K13'].value = complex_word_count
sheet['L13'].value = word_count
sheet['M13'].value = syllable_count
sheet['N13'].value = pronouns_count
sheet['O13'].value = average_word_length

workbook.save("Output Data Structure.xlsx")


#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0013.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A14'].value = "blackassign0013"
sheet['B14'].hyperlink = 'https://insights.blackcoffer.com/rise-of-e-health-and-its-impact-on-humans-by-the-year-2030/'
sheet['C14'].value = positive_score
sheet['D14'].value = negative_score
sheet['E14'].value = polarity
sheet['F14'].value = subjective_score
sheet['G14'].value = average_sentence_length
sheet['H14'].value = percentage_of_complex_words
sheet['I14'].value = fog_index
sheet['J14'].value = average_number_of_words_per_sentence
sheet['K14'].value = complex_word_count
sheet['L14'].value = word_count
sheet['M14'].value = syllable_count
sheet['N14'].value = pronouns_count
sheet['O14'].value = average_word_length

workbook.save("Output Data Structure.xlsx")


#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0014.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A15'].value = "blackassign0014"
sheet['B15'].hyperlink = 'https://insights.blackcoffer.com/rise-of-e-health-and-its-imapct-on-humans-by-the-year-2030-2/'
sheet['C15'].value = positive_score
sheet['D15'].value = negative_score
sheet['E15'].value = polarity
sheet['F15'].value = subjective_score
sheet['G15'].value = average_sentence_length
sheet['H15'].value = percentage_of_complex_words
sheet['I15'].value = fog_index
sheet['J15'].value = average_number_of_words_per_sentence
sheet['K15'].value = complex_word_count
sheet['L15'].value = word_count
sheet['M15'].value = syllable_count
sheet['N15'].value = pronouns_count
sheet['O15'].value = average_word_length

workbook.save("Output Data Structure.xlsx")


#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0015.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A16'].value = "blackassign0015"
sheet['B16'].hyperlink = 'https://insights.blackcoffer.com/rise-of-telemedicine-and-its-impact-on-livelihood-by-2040-2/'
sheet['C16'].value = positive_score
sheet['D16'].value = negative_score
sheet['E16'].value = polarity
sheet['F16'].value = subjective_score
sheet['G16'].value = average_sentence_length
sheet['H16'].value = percentage_of_complex_words
sheet['I16'].value = fog_index
sheet['J16'].value = average_number_of_words_per_sentence
sheet['K16'].value = complex_word_count
sheet['L16'].value = word_count
sheet['M16'].value = syllable_count
sheet['N16'].value = pronouns_count
sheet['O16'].value = average_word_length

workbook.save("Output Data Structure.xlsx")


#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0016.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A17'].value = "blackassign0016"
sheet['B17'].hyperlink = 'https://insights.blackcoffer.com/rise-of-telemedicine-and-its-impact-on-livelihood-by-2040-2-2/'
sheet['C17'].value = positive_score
sheet['D17'].value = negative_score
sheet['E17'].value = polarity
sheet['F17'].value = subjective_score
sheet['G17'].value = average_sentence_length
sheet['H17'].value = percentage_of_complex_words
sheet['I17'].value = fog_index
sheet['J17'].value = average_number_of_words_per_sentence
sheet['K17'].value = complex_word_count
sheet['L17'].value = word_count
sheet['M17'].value = syllable_count
sheet['N17'].value = pronouns_count
sheet['O17'].value = average_word_length

workbook.save("Output Data Structure.xlsx")


#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0017.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A18'].value = "blackassign0017"
sheet['B18'].hyperlink = 'https://insights.blackcoffer.com/rise-of-chatbots-and-its-impact-on-customer-support-by-the-year-2040/'
sheet['C18'].value = positive_score
sheet['D18'].value = negative_score
sheet['E18'].value = polarity
sheet['F18'].value = subjective_score
sheet['G18'].value = average_sentence_length
sheet['H18'].value = percentage_of_complex_words
sheet['I18'].value = fog_index
sheet['J18'].value = average_number_of_words_per_sentence
sheet['K18'].value = complex_word_count
sheet['L18'].value = word_count
sheet['M18'].value = syllable_count
sheet['N18'].value = pronouns_count
sheet['O18'].value = average_word_length

workbook.save("Output Data Structure.xlsx")


#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0018.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A19'].value = "blackassign0018"
sheet['B19'].hyperlink = 'https://insights.blackcoffer.com/rise-of-e-health-and-its-imapct-on-humans-by-the-year-2030/'
sheet['C19'].value = positive_score
sheet['D19'].value = negative_score
sheet['E19'].value = polarity
sheet['F19'].value = subjective_score
sheet['G19'].value = average_sentence_length
sheet['H19'].value = percentage_of_complex_words
sheet['I19'].value = fog_index
sheet['J19'].value = average_number_of_words_per_sentence
sheet['K19'].value = complex_word_count
sheet['L19'].value = word_count
sheet['M19'].value = syllable_count
sheet['N19'].value = pronouns_count
sheet['O19'].value = average_word_length

workbook.save("Output Data Structure.xlsx")


#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0019.txt", "r", encoding="utf-8") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A20'].value = "blackassign0019"
sheet['B20'].hyperlink = 'https://insights.blackcoffer.com/how-does-marketing-influence-businesses-and-consumers/'
sheet['C20'].value = positive_score
sheet['D20'].value = negative_score
sheet['E20'].value = polarity
sheet['F20'].value = subjective_score
sheet['G20'].value = average_sentence_length
sheet['H20'].value = percentage_of_complex_words
sheet['I20'].value = fog_index
sheet['J20'].value = average_number_of_words_per_sentence
sheet['K20'].value = complex_word_count
sheet['L20'].value = word_count
sheet['M20'].value = syllable_count
sheet['N20'].value = pronouns_count
sheet['O20'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0020.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A21'].value = "blackassign0020"
sheet['B21'].hyperlink = 'https://insights.blackcoffer.com/how-advertisement-increase-your-market-value/'
sheet['C21'].value = positive_score
sheet['D21'].value = negative_score
sheet['E21'].value = polarity
sheet['F21'].value = subjective_score
sheet['G21'].value = average_sentence_length
sheet['H21'].value = percentage_of_complex_words
sheet['I21'].value = fog_index
sheet['J21'].value = average_number_of_words_per_sentence
sheet['K21'].value = complex_word_count
sheet['L21'].value = word_count
sheet['M21'].value = syllable_count
sheet['N21'].value = pronouns_count
sheet['O21'].value = average_word_length

workbook.save("Output Data Structure.xlsx")


#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0021.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A22'].value = "blackassign0021"
sheet['B22'].hyperlink = 'https://insights.blackcoffer.com/negative-effects-of-marketing-on-society/'
sheet['C22'].value = positive_score
sheet['D22'].value = negative_score
sheet['E22'].value = polarity
sheet['F22'].value = subjective_score
sheet['G22'].value = average_sentence_length
sheet['H22'].value = percentage_of_complex_words
sheet['I22'].value = fog_index
sheet['J22'].value = average_number_of_words_per_sentence
sheet['K22'].value = complex_word_count
sheet['L22'].value = word_count
sheet['M22'].value = syllable_count
sheet['N22'].value = pronouns_count
sheet['O22'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0022.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A23'].value = "blackassign0022"
sheet['B23'].hyperlink = 'https://insights.blackcoffer.com/how-advertisement-marketing-affects-business/'
sheet['C23'].value = positive_score
sheet['D23'].value = negative_score
sheet['E23'].value = polarity
sheet['F23'].value = subjective_score
sheet['G23'].value = average_sentence_length
sheet['H23'].value = percentage_of_complex_words
sheet['I23'].value = fog_index
sheet['J23'].value = average_number_of_words_per_sentence
sheet['K23'].value = complex_word_count
sheet['L23'].value = word_count
sheet['M23'].value = syllable_count
sheet['N23'].value = pronouns_count
sheet['O23'].value = average_word_length

workbook.save("Output Data Structure.xlsx")


#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0023.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A24'].value = "blackassign0023"
sheet['B24'].hyperlink = 'https://insights.blackcoffer.com/rising-it-cities-will-impact-the-economy-environment-infrastructure-and-city-life-by-the-year-2035/'
sheet['C24'].value = positive_score
sheet['D24'].value = negative_score
sheet['E24'].value = polarity
sheet['F24'].value = subjective_score
sheet['G24'].value = average_sentence_length
sheet['H24'].value = percentage_of_complex_words
sheet['I24'].value = fog_index
sheet['J24'].value = average_number_of_words_per_sentence
sheet['K24'].value = complex_word_count
sheet['L24'].value = word_count
sheet['M24'].value = syllable_count
sheet['N24'].value = pronouns_count
sheet['O24'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0024.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A25'].value = "blackassign0024"
sheet['B25'].hyperlink = 'https://insights.blackcoffer.com/rise-of-ott-platform-and-its-impact-on-entertainment-industry-by-the-year-2030/'
sheet['C25'].value = positive_score
sheet['D25'].value = negative_score
sheet['E25'].value = polarity
sheet['F25'].value = subjective_score
sheet['G25'].value = average_sentence_length
sheet['H25'].value = percentage_of_complex_words
sheet['I25'].value = fog_index
sheet['J25'].value = average_number_of_words_per_sentence
sheet['K25'].value = complex_word_count
sheet['L25'].value = word_count
sheet['M25'].value = syllable_count
sheet['N25'].value = pronouns_count
sheet['O25'].value = average_word_length

workbook.save("Output Data Structure.xlsx")


#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0025.txt", "r" , encoding="utf-8") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A26'].value = "blackassign0025"
sheet['B26'].hyperlink = 'https://insights.blackcoffer.com/rise-of-electric-vehicles-and-its-impact-on-livelihood-by-2040/'
sheet['C26'].value = positive_score
sheet['D26'].value = negative_score
sheet['E26'].value = polarity
sheet['F26'].value = subjective_score
sheet['G26'].value = average_sentence_length
sheet['H26'].value = percentage_of_complex_words
sheet['I26'].value = fog_index
sheet['J26'].value = average_number_of_words_per_sentence
sheet['K26'].value = complex_word_count
sheet['L26'].value = word_count
sheet['M26'].value = syllable_count
sheet['N26'].value = pronouns_count
sheet['O26'].value = average_word_length

workbook.save("Output Data Structure.xlsx")


#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0026.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A27'].value = "blackassign0026"
sheet['B27'].hyperlink = 'https://insights.blackcoffer.com/rise-of-electric-vehicle-and-its-impact-on-livelihood-by-the-year-2040/'
sheet['C27'].value = positive_score
sheet['D27'].value = negative_score
sheet['E27'].value = polarity
sheet['F27'].value = subjective_score
sheet['G27'].value = average_sentence_length
sheet['H27'].value = percentage_of_complex_words
sheet['I27'].value = fog_index
sheet['J27'].value = average_number_of_words_per_sentence
sheet['K27'].value = complex_word_count
sheet['L27'].value = word_count
sheet['M27'].value = syllable_count
sheet['N27'].value = pronouns_count
sheet['O27'].value = average_word_length

workbook.save("Output Data Structure.xlsx")


#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0027.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A28'].value = "blackassign0027"
sheet['B28'].hyperlink = 'https://insights.blackcoffer.com/oil-prices-by-the-year-2040-and-how-it-will-impact-the-world-economy/'
sheet['C28'].value = positive_score
sheet['D28'].value = negative_score
sheet['E28'].value = polarity
sheet['F28'].value = subjective_score
sheet['G28'].value = average_sentence_length
sheet['H28'].value = percentage_of_complex_words
sheet['I28'].value = fog_index
sheet['J28'].value = average_number_of_words_per_sentence
sheet['K28'].value = complex_word_count
sheet['L28'].value = word_count
sheet['M28'].value = syllable_count
sheet['N28'].value = pronouns_count
sheet['O28'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0028.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A29'].value = "blackassign0028"
sheet['B29'].hyperlink = 'https://insights.blackcoffer.com/an-outlook-of-healthcare-by-the-year-2040-and-how-it-will-impact-human-lives/'
sheet['C29'].value = positive_score
sheet['D29'].value = negative_score
sheet['E29'].value = polarity
sheet['F29'].value = subjective_score
sheet['G29'].value = average_sentence_length
sheet['H29'].value = percentage_of_complex_words
sheet['I29'].value = fog_index
sheet['J29'].value = average_number_of_words_per_sentence
sheet['K29'].value = complex_word_count
sheet['L29'].value = word_count
sheet['M29'].value = syllable_count
sheet['N29'].value = pronouns_count
sheet['O29'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0029.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A30'].value = "blackassign0029"
sheet['B30'].hyperlink = 'https://insights.blackcoffer.com/ai-in-healthcare-to-improve-patient-outcomes/'
sheet['C30'].value = positive_score
sheet['D30'].value = negative_score
sheet['E30'].value = polarity
sheet['F30'].value = subjective_score
sheet['G30'].value = average_sentence_length
sheet['H30'].value = percentage_of_complex_words
sheet['I30'].value = fog_index
sheet['J30'].value = average_number_of_words_per_sentence
sheet['K30'].value = complex_word_count
sheet['L30'].value = word_count
sheet['M30'].value = syllable_count
sheet['N30'].value = pronouns_count
sheet['O30'].value = average_word_length

workbook.save("Output Data Structure.xlsx")


#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0030.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A31'].value = "blackassign0030"
sheet['B31'].hyperlink = 'https://insights.blackcoffer.com/what-if-the-creation-is-taking-over-the-creator/'
sheet['C31'].value = positive_score
sheet['D31'].value = negative_score
sheet['E31'].value = polarity
sheet['F31'].value = subjective_score
sheet['G31'].value = average_sentence_length
sheet['H31'].value = percentage_of_complex_words
sheet['I31'].value = fog_index
sheet['J31'].value = average_number_of_words_per_sentence
sheet['K31'].value = complex_word_count
sheet['L31'].value = word_count
sheet['M31'].value = syllable_count
sheet['N31'].value = pronouns_count
sheet['O31'].value = average_word_length

workbook.save("Output Data Structure.xlsx")


#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0031.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A32'].value = "blackassign0031"
sheet['B32'].hyperlink = 'https://insights.blackcoffer.com/what-jobs-will-robots-take-from-humans-in-the-future/'
sheet['C32'].value = positive_score
sheet['D32'].value = negative_score
sheet['E32'].value = polarity
sheet['F32'].value = subjective_score
sheet['G32'].value = average_sentence_length
sheet['H32'].value = percentage_of_complex_words
sheet['I32'].value = fog_index
sheet['J32'].value = average_number_of_words_per_sentence
sheet['K32'].value = complex_word_count
sheet['L32'].value = word_count
sheet['M32'].value = syllable_count
sheet['N32'].value = pronouns_count
sheet['O32'].value = average_word_length

workbook.save("Output Data Structure.xlsx")


#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0032.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A33'].value = "blackassign0032"
sheet['B33'].hyperlink = 'https://insights.blackcoffer.com/will-machine-replace-the-human-in-the-future-of-work/'
sheet['C33'].value = positive_score
sheet['D33'].value = negative_score
sheet['E33'].value = polarity
sheet['F33'].value = subjective_score
sheet['G33'].value = average_sentence_length
sheet['H33'].value = percentage_of_complex_words
sheet['I33'].value = fog_index
sheet['J33'].value = average_number_of_words_per_sentence
sheet['K33'].value = complex_word_count
sheet['L33'].value = word_count
sheet['M33'].value = syllable_count
sheet['N33'].value = pronouns_count
sheet['O33'].value = average_word_length

workbook.save("Output Data Structure.xlsx")


#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0033.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A34'].value = "blackassign0033"
sheet['B34'].hyperlink = 'https://insights.blackcoffer.com/will-ai-replace-us-or-work-with-us/'
sheet['C34'].value = positive_score
sheet['D34'].value = negative_score
sheet['E34'].value = polarity
sheet['F34'].value = subjective_score
sheet['G34'].value = average_sentence_length
sheet['H34'].value = percentage_of_complex_words
sheet['I34'].value = fog_index
sheet['J34'].value = average_number_of_words_per_sentence
sheet['K34'].value = complex_word_count
sheet['L34'].value = word_count
sheet['M34'].value = syllable_count
sheet['N34'].value = pronouns_count
sheet['O34'].value = average_word_length

workbook.save("Output Data Structure.xlsx")


#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0034.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A35'].value = "blackassign0034"
sheet['B35'].hyperlink = 'https://insights.blackcoffer.com/man-and-machines-together-machines-are-more-diligent-than-humans-blackcoffe/'
sheet['C35'].value = positive_score
sheet['D35'].value = negative_score
sheet['E35'].value = polarity
sheet['F35'].value = subjective_score
sheet['G35'].value = average_sentence_length
sheet['H35'].value = percentage_of_complex_words
sheet['I35'].value = fog_index
sheet['J35'].value = average_number_of_words_per_sentence
sheet['K35'].value = complex_word_count
sheet['L35'].value = word_count
sheet['M35'].value = syllable_count
sheet['N35'].value = pronouns_count
sheet['O35'].value = average_word_length

workbook.save("Output Data Structure.xlsx")


#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0035.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A36'].value = "blackassign0035"
sheet['B36'].hyperlink = 'https://insights.blackcoffer.com/in-future-or-in-upcoming-years-humans-and-machines-are-going-to-work-together-in-every-field-of-work/'
sheet['C36'].value = positive_score
sheet['D36'].value = negative_score
sheet['E36'].value = polarity
sheet['F36'].value = subjective_score
sheet['G36'].value = average_sentence_length
sheet['H36'].value = percentage_of_complex_words
sheet['I36'].value = fog_index
sheet['J36'].value = average_number_of_words_per_sentence
sheet['K36'].value = complex_word_count
sheet['L36'].value = word_count
sheet['M36'].value = syllable_count
sheet['N36'].value = pronouns_count
sheet['O36'].value = average_word_length

workbook.save("Output Data Structure.xlsx")


#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0037.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A38'].value = "blackassign0037"
sheet['B38'].hyperlink = 'https://insights.blackcoffer.com/how-machine-learning-will-affect-your-business/'
sheet['C38'].value = positive_score
sheet['D38'].value = negative_score
sheet['E38'].value = polarity
sheet['F38'].value = subjective_score
sheet['G38'].value = average_sentence_length
sheet['H38'].value = percentage_of_complex_words
sheet['I38'].value = fog_index
sheet['J38'].value = average_number_of_words_per_sentence
sheet['K38'].value = complex_word_count
sheet['L38'].value = word_count
sheet['M38'].value = syllable_count
sheet['N38'].value = pronouns_count
sheet['O38'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0038.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A39'].value = "blackassign0038"
sheet['B39'].hyperlink = 'https://insights.blackcoffer.com/deep-learning-impact-on-areas-of-e-learning/'
sheet['C39'].value = positive_score
sheet['D39'].value = negative_score
sheet['E39'].value = polarity
sheet['F39'].value = subjective_score
sheet['G39'].value = average_sentence_length
sheet['H39'].value = percentage_of_complex_words
sheet['I39'].value = fog_index
sheet['J39'].value = average_number_of_words_per_sentence
sheet['K39'].value = complex_word_count
sheet['L39'].value = word_count
sheet['M39'].value = syllable_count
sheet['N39'].value = pronouns_count
sheet['O39'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0039.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A40'].value = "blackassign0039"
sheet['B40'].hyperlink = 'https://insights.blackcoffer.com/how-to-protect-future-data-and-its-privacy-blackcoffer/'
sheet['C40'].value = positive_score
sheet['D40'].value = negative_score
sheet['E40'].value = polarity
sheet['F40'].value = subjective_score
sheet['G40'].value = average_sentence_length
sheet['H40'].value = percentage_of_complex_words
sheet['I40'].value = fog_index
sheet['J40'].value = average_number_of_words_per_sentence
sheet['K40'].value = complex_word_count
sheet['L40'].value = word_count
sheet['M40'].value = syllable_count
sheet['N40'].value = pronouns_count
sheet['O40'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0040.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A41'].value = "blackassign0040"
sheet['B41'].hyperlink = 'https://insights.blackcoffer.com/how-machines-ai-automations-and-robo-human-are-effective-in-finance-and-banking/'
sheet['C41'].value = positive_score
sheet['D41'].value = negative_score
sheet['E41'].value = polarity
sheet['F41'].value = subjective_score
sheet['G41'].value = average_sentence_length
sheet['H41'].value = percentage_of_complex_words
sheet['I41'].value = fog_index
sheet['J41'].value = average_number_of_words_per_sentence
sheet['K41'].value = complex_word_count
sheet['L41'].value = word_count
sheet['M41'].value = syllable_count
sheet['N41'].value = pronouns_count
sheet['O41'].value = average_word_length

workbook.save("Output Data Structure.xlsx")




#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0041.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A42'].value = "blackassign0041"
sheet['B42'].hyperlink = 'https://insights.blackcoffer.com/ai-human-robotics-machine-future-planet-blackcoffer-thinking-jobs-workplace/'
sheet['C42'].value = positive_score
sheet['D42'].value = negative_score
sheet['E42'].value = polarity
sheet['F42'].value = subjective_score
sheet['G42'].value = average_sentence_length
sheet['H42'].value = percentage_of_complex_words
sheet['I42'].value = fog_index
sheet['J42'].value = average_number_of_words_per_sentence
sheet['K42'].value = complex_word_count
sheet['L42'].value = word_count
sheet['M42'].value = syllable_count
sheet['N42'].value = pronouns_count
sheet['O42'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0042.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A43'].value = "blackassign0042"
sheet['B43'].hyperlink = 'https://insights.blackcoffer.com/how-ai-will-change-the-world-blackcoffer/'
sheet['C43'].value = positive_score
sheet['D43'].value = negative_score
sheet['E43'].value = polarity
sheet['F43'].value = subjective_score
sheet['G43'].value = average_sentence_length
sheet['H43'].value = percentage_of_complex_words
sheet['I43'].value = fog_index
sheet['J43'].value = average_number_of_words_per_sentence
sheet['K43'].value = complex_word_count
sheet['L43'].value = word_count
sheet['M43'].value = syllable_count
sheet['N43'].value = pronouns_count
sheet['O43'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0043.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A44'].value = "blackassign0043"
sheet['B44'].hyperlink = 'https://insights.blackcoffer.com/future-of-work-how-ai-has-entered-the-workplace/'
sheet['C44'].value = positive_score
sheet['D44'].value = negative_score
sheet['E44'].value = polarity
sheet['F44'].value = subjective_score
sheet['G44'].value = average_sentence_length
sheet['H44'].value = percentage_of_complex_words
sheet['I44'].value = fog_index
sheet['J44'].value = average_number_of_words_per_sentence
sheet['K44'].value = complex_word_count
sheet['L44'].value = word_count
sheet['M44'].value = syllable_count
sheet['N44'].value = pronouns_count
sheet['O44'].value = average_word_length

workbook.save("Output Data Structure.xlsx")


#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0044.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A45'].value = "blackassign0044"
sheet['B45'].hyperlink = 'https://insights.blackcoffer.com/ai-tool-alexa-google-assistant-finance-banking-tool-future/'
sheet['C45'].value = positive_score
sheet['D45'].value = negative_score
sheet['E45'].value = polarity
sheet['F45'].value = subjective_score
sheet['G45'].value = average_sentence_length
sheet['H45'].value = percentage_of_complex_words
sheet['I45'].value = fog_index
sheet['J45'].value = average_number_of_words_per_sentence
sheet['K45'].value = complex_word_count
sheet['L45'].value = word_count
sheet['M45'].value = syllable_count
sheet['N45'].value = pronouns_count
sheet['O45'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0045.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A46'].value = "blackassign0045"
sheet['B46'].hyperlink = 'https://insights.blackcoffer.com/ai-healthcare-revolution-ml-technology-algorithm-google-analytics-industrialrevolution/'
sheet['C46'].value = positive_score
sheet['D46'].value = negative_score
sheet['E46'].value = polarity
sheet['F46'].value = subjective_score
sheet['G46'].value = average_sentence_length
sheet['H46'].value = percentage_of_complex_words
sheet['I46'].value = fog_index
sheet['J46'].value = average_number_of_words_per_sentence
sheet['K46'].value = complex_word_count
sheet['L46'].value = word_count
sheet['M46'].value = syllable_count
sheet['N46'].value = pronouns_count
sheet['O46'].value = average_word_length

workbook.save("Output Data Structure.xlsx")




#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0046.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A47'].value = "blackassign0046"
sheet['B47'].hyperlink = 'https://insights.blackcoffer.com/all-you-need-to-know-about-online-marketing/'
sheet['C47'].value = positive_score
sheet['D47'].value = negative_score
sheet['E47'].value = polarity
sheet['F47'].value = subjective_score
sheet['G47'].value = average_sentence_length
sheet['H47'].value = percentage_of_complex_words
sheet['I47'].value = fog_index
sheet['J47'].value = average_number_of_words_per_sentence
sheet['K47'].value = complex_word_count
sheet['L47'].value = word_count
sheet['M47'].value = syllable_count
sheet['N47'].value = pronouns_count
sheet['O47'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0047.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A48'].value = "blackassign0047"
sheet['B48'].hyperlink = 'https://insights.blackcoffer.com/evolution-of-advertising-industry/'
sheet['C48'].value = positive_score
sheet['D48'].value = negative_score
sheet['E48'].value = polarity
sheet['F48'].value = subjective_score
sheet['G48'].value = average_sentence_length
sheet['H48'].value = percentage_of_complex_words
sheet['I48'].value = fog_index
sheet['J48'].value = average_number_of_words_per_sentence
sheet['K48'].value = complex_word_count
sheet['L48'].value = word_count
sheet['M48'].value = syllable_count
sheet['N48'].value = pronouns_count
sheet['O48'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0048.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A49'].value = "blackassign0048"
sheet['B49'].hyperlink = 'https://insights.blackcoffer.com/how-data-analytics-can-help-your-business-respond-to-the-impact-of-covid-19/'
sheet['C49'].value = positive_score
sheet['D49'].value = negative_score
sheet['E49'].value = polarity
sheet['F49'].value = subjective_score
sheet['G49'].value = average_sentence_length
sheet['H49'].value = percentage_of_complex_words
sheet['I49'].value = fog_index
sheet['J49'].value = average_number_of_words_per_sentence
sheet['K49'].value = complex_word_count
sheet['L49'].value = word_count
sheet['M49'].value = syllable_count
sheet['N49'].value = pronouns_count
sheet['O49'].value = average_word_length

workbook.save("Output Data Structure.xlsx")




#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0050.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A51'].value = "blackassign0050"
sheet['B51'].hyperlink = 'https://insights.blackcoffer.com/environmental-impact-of-the-covid-19-pandemic-lesson-for-the-future/'
sheet['C51'].value = positive_score
sheet['D51'].value = negative_score
sheet['E51'].value = polarity
sheet['F51'].value = subjective_score
sheet['G51'].value = average_sentence_length
sheet['H51'].value = percentage_of_complex_words
sheet['I51'].value = fog_index
sheet['J51'].value = average_number_of_words_per_sentence
sheet['K51'].value = complex_word_count
sheet['L51'].value = word_count
sheet['M51'].value = syllable_count
sheet['N51'].value = pronouns_count
sheet['O51'].value = average_word_length

workbook.save("Output Data Structure.xlsx")


#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0051.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A52'].value = "blackassign0051"
sheet['B52'].hyperlink = 'https://insights.blackcoffer.com/how-data-analytics-and-ai-are-used-to-halt-the-covid-19-pandemic/'
sheet['C52'].value = positive_score
sheet['D52'].value = negative_score
sheet['E52'].value = polarity
sheet['F52'].value = subjective_score
sheet['G52'].value = average_sentence_length
sheet['H52'].value = percentage_of_complex_words
sheet['I52'].value = fog_index
sheet['J52'].value = average_number_of_words_per_sentence
sheet['K52'].value = complex_word_count
sheet['L52'].value = word_count
sheet['M52'].value = syllable_count
sheet['N52'].value = pronouns_count
sheet['O52'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0052.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A53'].value = "blackassign0052"
sheet['B53'].hyperlink = 'https://insights.blackcoffer.com/difference-between-artificial-intelligence-machine-learning-statistics-and-data-mining/'
sheet['C53'].value = positive_score
sheet['D53'].value = negative_score
sheet['E53'].value = polarity
sheet['F53'].value = subjective_score
sheet['G53'].value = average_sentence_length
sheet['H53'].value = percentage_of_complex_words
sheet['I53'].value = fog_index
sheet['J53'].value = average_number_of_words_per_sentence
sheet['K53'].value = complex_word_count
sheet['L53'].value = word_count
sheet['M53'].value = syllable_count
sheet['N53'].value = pronouns_count
sheet['O53'].value = average_word_length

workbook.save("Output Data Structure.xlsx")





#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0053.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A54'].value = "blackassign0053"
sheet['B54'].hyperlink = 'https://insights.blackcoffer.com/how-python-became-the-first-choice-for-data-science/'
sheet['C54'].value = positive_score
sheet['D54'].value = negative_score
sheet['E54'].value = polarity
sheet['F54'].value = subjective_score
sheet['G54'].value = average_sentence_length
sheet['H54'].value = percentage_of_complex_words
sheet['I54'].value = fog_index
sheet['J54'].value = average_number_of_words_per_sentence
sheet['K54'].value = complex_word_count
sheet['L54'].value = word_count
sheet['M54'].value = syllable_count
sheet['N54'].value = pronouns_count
sheet['O54'].value = average_word_length

workbook.save("Output Data Structure.xlsx")




#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0054.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A55'].value = "blackassign0054"
sheet['B55'].hyperlink = 'https://insights.blackcoffer.com/how-google-fit-measure-heart-and-respiratory-rates-using-a-phone/'
sheet['C55'].value = positive_score
sheet['D55'].value = negative_score
sheet['E55'].value = polarity
sheet['F55'].value = subjective_score
sheet['G55'].value = average_sentence_length
sheet['H55'].value = percentage_of_complex_words
sheet['I55'].value = fog_index
sheet['J55'].value = average_number_of_words_per_sentence
sheet['K55'].value = complex_word_count
sheet['L55'].value = word_count
sheet['M55'].value = syllable_count
sheet['N55'].value = pronouns_count
sheet['O55'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0055.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A56'].value = "blackassign0055"
sheet['B56'].hyperlink = 'https://insights.blackcoffer.com/what-is-the-future-of-mobile-apps/'
sheet['C56'].value = positive_score
sheet['D56'].value = negative_score
sheet['E56'].value = polarity
sheet['F56'].value = subjective_score
sheet['G56'].value = average_sentence_length
sheet['H56'].value = percentage_of_complex_words
sheet['I56'].value = fog_index
sheet['J56'].value = average_number_of_words_per_sentence
sheet['K56'].value = complex_word_count
sheet['L56'].value = word_count
sheet['M56'].value = syllable_count
sheet['N56'].value = pronouns_count
sheet['O56'].value = average_word_length

workbook.save("Output Data Structure.xlsx")





#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0056.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A57'].value = "blackassign0056"
sheet['B57'].hyperlink = 'https://insights.blackcoffer.com/impact-of-ai-in-health-and-medicine/'
sheet['C57'].value = positive_score
sheet['D57'].value = negative_score
sheet['E57'].value = polarity
sheet['F57'].value = subjective_score
sheet['G57'].value = average_sentence_length
sheet['H57'].value = percentage_of_complex_words
sheet['I57'].value = fog_index
sheet['J57'].value = average_number_of_words_per_sentence
sheet['K57'].value = complex_word_count
sheet['L57'].value = word_count
sheet['M57'].value = syllable_count
sheet['N57'].value = pronouns_count
sheet['O57'].value = average_word_length

workbook.save("Output Data Structure.xlsx")




#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0057.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A58'].value = "blackassign0057"
sheet['B58'].hyperlink = 'https://insights.blackcoffer.com/telemedicine-what-patients-like-and-dislike-about-it/'
sheet['C58'].value = positive_score
sheet['D58'].value = negative_score
sheet['E58'].value = polarity
sheet['F58'].value = subjective_score
sheet['G58'].value = average_sentence_length
sheet['H58'].value = percentage_of_complex_words
sheet['I58'].value = fog_index
sheet['J58'].value = average_number_of_words_per_sentence
sheet['K58'].value = complex_word_count
sheet['L58'].value = word_count
sheet['M58'].value = syllable_count
sheet['N58'].value = pronouns_count
sheet['O58'].value = average_word_length

workbook.save("Output Data Structure.xlsx")




#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0058.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A59'].value = "blackassign0058"
sheet['B59'].hyperlink = 'https://insights.blackcoffer.com/how-we-forecast-future-technologies/'
sheet['C59'].value = positive_score
sheet['D59'].value = negative_score
sheet['E59'].value = polarity
sheet['F59'].value = subjective_score
sheet['G59'].value = average_sentence_length
sheet['H59'].value = percentage_of_complex_words
sheet['I59'].value = fog_index
sheet['J59'].value = average_number_of_words_per_sentence
sheet['K59'].value = complex_word_count
sheet['L59'].value = word_count
sheet['M59'].value = syllable_count
sheet['N59'].value = pronouns_count
sheet['O59'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0059.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A60'].value = "blackassign0059"
sheet['B60'].hyperlink = 'https://insights.blackcoffer.com/can-robots-tackle-late-life-loneliness/'
sheet['C60'].value = positive_score
sheet['D60'].value = negative_score
sheet['E60'].value = polarity
sheet['F60'].value = subjective_score
sheet['G60'].value = average_sentence_length
sheet['H60'].value = percentage_of_complex_words
sheet['I60'].value = fog_index
sheet['J60'].value = average_number_of_words_per_sentence
sheet['K60'].value = complex_word_count
sheet['L60'].value = word_count
sheet['M60'].value = syllable_count
sheet['N60'].value = pronouns_count
sheet['O60'].value = average_word_length

workbook.save("Output Data Structure.xlsx")





#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0060.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A61'].value = "blackassign0060"
sheet['B61'].hyperlink = 'https://insights.blackcoffer.com/embedding-care-robots-into-society-socio-technical-considerations/'
sheet['C61'].value = positive_score
sheet['D61'].value = negative_score
sheet['E61'].value = polarity
sheet['F61'].value = subjective_score
sheet['G61'].value = average_sentence_length
sheet['H61'].value = percentage_of_complex_words
sheet['I61'].value = fog_index
sheet['J61'].value = average_number_of_words_per_sentence
sheet['K61'].value = complex_word_count
sheet['L61'].value = word_count
sheet['M61'].value = syllable_count
sheet['N61'].value = pronouns_count
sheet['O61'].value = average_word_length

workbook.save("Output Data Structure.xlsx")




#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0061.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A62'].value = "blackassign0061"
sheet['B62'].hyperlink = 'https://insights.blackcoffer.com/management-challenges-for-future-digitalization-of-healthcare-services/'
sheet['C62'].value = positive_score
sheet['D62'].value = negative_score
sheet['E62'].value = polarity
sheet['F62'].value = subjective_score
sheet['G62'].value = average_sentence_length
sheet['H62'].value = percentage_of_complex_words
sheet['I62'].value = fog_index
sheet['J62'].value = average_number_of_words_per_sentence
sheet['K62'].value = complex_word_count
sheet['L62'].value = word_count
sheet['M62'].value = syllable_count
sheet['N62'].value = pronouns_count
sheet['O62'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0062.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A63'].value = "blackassign0062"
sheet['B63'].hyperlink = 'https://insights.blackcoffer.com/are-we-any-closer-to-preventing-a-nuclear-holocaust/'
sheet['C63'].value = positive_score
sheet['D63'].value = negative_score
sheet['E63'].value = polarity
sheet['F63'].value = subjective_score
sheet['G63'].value = average_sentence_length
sheet['H63'].value = percentage_of_complex_words
sheet['I63'].value = fog_index
sheet['J63'].value = average_number_of_words_per_sentence
sheet['K63'].value = complex_word_count
sheet['L63'].value = word_count
sheet['M63'].value = syllable_count
sheet['N63'].value = pronouns_count
sheet['O63'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0063.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A64'].value = "blackassign0063"
sheet['B64'].hyperlink = 'https://insights.blackcoffer.com/will-technology-eliminate-the-need-for-animal-testing-in-drug-development/'
sheet['C64'].value = positive_score
sheet['D64'].value = negative_score
sheet['E64'].value = polarity
sheet['F64'].value = subjective_score
sheet['G64'].value = average_sentence_length
sheet['H64'].value = percentage_of_complex_words
sheet['I64'].value = fog_index
sheet['J64'].value = average_number_of_words_per_sentence
sheet['K64'].value = complex_word_count
sheet['L64'].value = word_count
sheet['M64'].value = syllable_count
sheet['N64'].value = pronouns_count
sheet['O64'].value = average_word_length

workbook.save("Output Data Structure.xlsx")


                                
                            
#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0064.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A65'].value = "blackassign0064"
sheet['B65'].hyperlink = 'https://insights.blackcoffer.com/will-we-ever-understand-the-nature-of-consciousness/'
sheet['C65'].value = positive_score
sheet['D65'].value = negative_score
sheet['E65'].value = polarity
sheet['F65'].value = subjective_score
sheet['G65'].value = average_sentence_length
sheet['H65'].value = percentage_of_complex_words
sheet['I65'].value = fog_index
sheet['J65'].value = average_number_of_words_per_sentence
sheet['K65'].value = complex_word_count
sheet['L65'].value = word_count
sheet['M65'].value = syllable_count
sheet['N65'].value = pronouns_count
sheet['O65'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0065.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A66'].value = "blackassign0065"
sheet['B66'].hyperlink = 'https://insights.blackcoffer.com/will-we-ever-colonize-outer-space/'
sheet['C66'].value = positive_score
sheet['D66'].value = negative_score
sheet['E66'].value = polarity
sheet['F66'].value = subjective_score
sheet['G66'].value = average_sentence_length
sheet['H66'].value = percentage_of_complex_words
sheet['I66'].value = fog_index
sheet['J66'].value = average_number_of_words_per_sentence
sheet['K66'].value = complex_word_count
sheet['L66'].value = word_count
sheet['M66'].value = syllable_count
sheet['N66'].value = pronouns_count
sheet['O66'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0066.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A67'].value = "blackassign0066"
sheet['B67'].hyperlink = 'https://insights.blackcoffer.com/what-is-the-chance-homo-sapiens-will-survive-for-the-next-500-years/'
sheet['C67'].value = positive_score
sheet['D67'].value = negative_score
sheet['E67'].value = polarity
sheet['F67'].value = subjective_score
sheet['G67'].value = average_sentence_length
sheet['H67'].value = percentage_of_complex_words
sheet['I67'].value = fog_index
sheet['J67'].value = average_number_of_words_per_sentence
sheet['K67'].value = complex_word_count
sheet['L67'].value = word_count
sheet['M67'].value = syllable_count
sheet['N67'].value = pronouns_count
sheet['O67'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0067.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A68'].value = "blackassign0067"
sheet['B68'].hyperlink = 'https://insights.blackcoffer.com/why-does-your-business-need-a-chatbot/'
sheet['C68'].value = positive_score
sheet['D68'].value = negative_score
sheet['E68'].value = polarity
sheet['F68'].value = subjective_score
sheet['G68'].value = average_sentence_length
sheet['H68'].value = percentage_of_complex_words
sheet['I68'].value = fog_index
sheet['J68'].value = average_number_of_words_per_sentence
sheet['K68'].value = complex_word_count
sheet['L68'].value = word_count
sheet['M68'].value = syllable_count
sheet['N68'].value = pronouns_count
sheet['O68'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0068.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A69'].value = "blackassign0068"
sheet['B69'].hyperlink = 'https://insights.blackcoffer.com/how-you-lead-a-project-or-a-team-without-any-technical-expertise/'
sheet['C69'].value = positive_score
sheet['D69'].value = negative_score
sheet['E69'].value = polarity
sheet['F69'].value = subjective_score
sheet['G69'].value = average_sentence_length
sheet['H69'].value = percentage_of_complex_words
sheet['I69'].value = fog_index
sheet['J69'].value = average_number_of_words_per_sentence
sheet['K69'].value = complex_word_count
sheet['L69'].value = word_count
sheet['M69'].value = syllable_count
sheet['N69'].value = pronouns_count
sheet['O69'].value = average_word_length

workbook.save("Output Data Structure.xlsx")


#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0069.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A70'].value = "blackassign0069"
sheet['B70'].hyperlink = 'https://insights.blackcoffer.com/can-you-be-great-leader-without-technical-expertise/'
sheet['C70'].value = positive_score
sheet['D70'].value = negative_score
sheet['E70'].value = polarity
sheet['F70'].value = subjective_score
sheet['G70'].value = average_sentence_length
sheet['H70'].value = percentage_of_complex_words
sheet['I70'].value = fog_index
sheet['J70'].value = average_number_of_words_per_sentence
sheet['K70'].value = complex_word_count
sheet['L70'].value = word_count
sheet['M70'].value = syllable_count
sheet['N70'].value = pronouns_count
sheet['O70'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0070.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A71'].value = "blackassign0070"
sheet['B71'].hyperlink = 'https://insights.blackcoffer.com/how-does-artificial-intelligence-affect-the-environment/'
sheet['C71'].value = positive_score
sheet['D71'].value = negative_score
sheet['E71'].value = polarity
sheet['F71'].value = subjective_score
sheet['G71'].value = average_sentence_length
sheet['H71'].value = percentage_of_complex_words
sheet['I71'].value = fog_index
sheet['J71'].value = average_number_of_words_per_sentence
sheet['K71'].value = complex_word_count
sheet['L71'].value = word_count
sheet['M71'].value = syllable_count
sheet['N71'].value = pronouns_count
sheet['O71'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0071.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A72'].value = "blackassign0071"
sheet['B72'].hyperlink = 'https://insights.blackcoffer.com/how-to-overcome-your-fear-of-making-mistakes-2/'
sheet['C72'].value = positive_score
sheet['D72'].value = negative_score
sheet['E72'].value = polarity
sheet['F72'].value = subjective_score
sheet['G72'].value = average_sentence_length
sheet['H72'].value = percentage_of_complex_words
sheet['I72'].value = fog_index
sheet['J72'].value = average_number_of_words_per_sentence
sheet['K72'].value = complex_word_count
sheet['L72'].value = word_count
sheet['M72'].value = syllable_count
sheet['N72'].value = pronouns_count
sheet['O72'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0072.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A73'].value = "blackassign0072"
sheet['B73'].hyperlink = 'https://insights.blackcoffer.com/is-perfection-the-greatest-enemy-of-productivity/'
sheet['C73'].value = positive_score
sheet['D73'].value = negative_score
sheet['E73'].value = polarity
sheet['F73'].value = subjective_score
sheet['G73'].value = average_sentence_length
sheet['H73'].value = percentage_of_complex_words
sheet['I73'].value = fog_index
sheet['J73'].value = average_number_of_words_per_sentence
sheet['K73'].value = complex_word_count
sheet['L73'].value = word_count
sheet['M73'].value = syllable_count
sheet['N73'].value = pronouns_count
sheet['O73'].value = average_word_length

workbook.save("Output Data Structure.xlsx")


#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0073.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A74'].value = "blackassign0073"
sheet['B74'].hyperlink = 'https://insights.blackcoffer.com/global-financial-crisis-2008-causes-effects-and-its-solution/s'
sheet['C74'].value = positive_score
sheet['D74'].value = negative_score
sheet['E74'].value = polarity
sheet['F74'].value = subjective_score
sheet['G74'].value = average_sentence_length
sheet['H74'].value = percentage_of_complex_words
sheet['I74'].value = fog_index
sheet['J74'].value = average_number_of_words_per_sentence
sheet['K74'].value = complex_word_count
sheet['L74'].value = word_count
sheet['M74'].value = syllable_count
sheet['N74'].value = pronouns_count
sheet['O74'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0074.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A75'].value = "blackassign0074"
sheet['B75'].hyperlink = 'https://insights.blackcoffer.com/gender-diversity-and-equality-in-the-tech-industry/'
sheet['C75'].value = positive_score
sheet['D75'].value = negative_score
sheet['E75'].value = polarity
sheet['F75'].value = subjective_score
sheet['G75'].value = average_sentence_length
sheet['H75'].value = percentage_of_complex_words
sheet['I75'].value = fog_index
sheet['J75'].value = average_number_of_words_per_sentence
sheet['K75'].value = complex_word_count
sheet['L75'].value = word_count
sheet['M75'].value = syllable_count
sheet['N75'].value = pronouns_count
sheet['O75'].value = average_word_length

workbook.save("Output Data Structure.xlsx")


#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0075.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A76'].value = "blackassign0075"
sheet['B76'].hyperlink = 'https://insights.blackcoffer.com/how-to-overcome-your-fear-of-making-mistakes/'
sheet['C76'].value = positive_score
sheet['D76'].value = negative_score
sheet['E76'].value = polarity
sheet['F76'].value = subjective_score
sheet['G76'].value = average_sentence_length
sheet['H76'].value = percentage_of_complex_words
sheet['I76'].value = fog_index
sheet['J76'].value = average_number_of_words_per_sentence
sheet['K76'].value = complex_word_count
sheet['L76'].value = word_count
sheet['M76'].value = syllable_count
sheet['N76'].value = pronouns_count
sheet['O76'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0076.txt", "r", encoding="utf-8") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A77'].value = "blackassign0076"
sheet['B77'].hyperlink = 'https://insights.blackcoffer.com/how-small-business-can-survive-the-coronavirus-crisis/'
sheet['C77'].value = positive_score
sheet['D77'].value = negative_score
sheet['E77'].value = polarity
sheet['F77'].value = subjective_score
sheet['G77'].value = average_sentence_length
sheet['H77'].value = percentage_of_complex_words
sheet['I77'].value = fog_index
sheet['J77'].value = average_number_of_words_per_sentence
sheet['K77'].value = complex_word_count
sheet['L77'].value = word_count
sheet['M77'].value = syllable_count
sheet['N77'].value = pronouns_count
sheet['O77'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0077.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A78'].value = "blackassign0077"
sheet['B78'].hyperlink = 'https://insights.blackcoffer.com/impacts-of-covid-19-on-vegetable-vendors-and-food-stalls/'
sheet['C78'].value = positive_score
sheet['D78'].value = negative_score
sheet['E78'].value = polarity
sheet['F78'].value = subjective_score
sheet['G78'].value = average_sentence_length
sheet['H78'].value = percentage_of_complex_words
sheet['I78'].value = fog_index
sheet['J78'].value = average_number_of_words_per_sentence
sheet['K78'].value = complex_word_count
sheet['L78'].value = word_count
sheet['M78'].value = syllable_count
sheet['N78'].value = pronouns_count
sheet['O78'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0078.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A79'].value = "blackassign0078"
sheet['B79'].hyperlink = 'https://insights.blackcoffer.com/impacts-of-covid-19-on-vegetable-vendors/'
sheet['C79'].value = positive_score
sheet['D79'].value = negative_score
sheet['E79'].value = polarity
sheet['F79'].value = subjective_score
sheet['G79'].value = average_sentence_length
sheet['H79'].value = percentage_of_complex_words
sheet['I79'].value = fog_index
sheet['J79'].value = average_number_of_words_per_sentence
sheet['K79'].value = complex_word_count
sheet['L79'].value = word_count
sheet['M79'].value = syllable_count
sheet['N79'].value = pronouns_count
sheet['O79'].value = average_word_length

workbook.save("Output Data Structure.xlsx")




#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0079.txt", "r",  encoding="utf-8") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A80'].value = "blackassign0079"
sheet['B80'].hyperlink = 'https://insights.blackcoffer.com/impact-of-covid-19-pandemic-on-tourism-aviation-industries/'
sheet['C80'].value = positive_score
sheet['D80'].value = negative_score
sheet['E80'].value = polarity
sheet['F80'].value = subjective_score
sheet['G80'].value = average_sentence_length
sheet['H80'].value = percentage_of_complex_words
sheet['I80'].value = fog_index
sheet['J80'].value = average_number_of_words_per_sentence
sheet['K80'].value = complex_word_count
sheet['L80'].value = word_count
sheet['M80'].value = syllable_count
sheet['N80'].value = pronouns_count
sheet['O80'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0080.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A81'].value = "blackassign0080"
sheet['B81'].hyperlink = 'https://insights.blackcoffer.com/impact-of-covid-19-pandemic-on-sports-events-around-the-world/'
sheet['C81'].value = positive_score
sheet['D81'].value = negative_score
sheet['E81'].value = polarity
sheet['F81'].value = subjective_score
sheet['G81'].value = average_sentence_length
sheet['H81'].value = percentage_of_complex_words
sheet['I81'].value = fog_index
sheet['J81'].value = average_number_of_words_per_sentence
sheet['K81'].value = complex_word_count
sheet['L81'].value = word_count
sheet['M81'].value = syllable_count
sheet['N81'].value = pronouns_count
sheet['O81'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0081.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A82'].value = "blackassign0081"
sheet['B82'].hyperlink = 'https://insights.blackcoffer.com/changing-landscape-and-emerging-trends-in-the-indian-it-ites-industry/'
sheet['C82'].value = positive_score
sheet['D82'].value = negative_score
sheet['E82'].value = polarity
sheet['F82'].value = subjective_score
sheet['G82'].value = average_sentence_length
sheet['H82'].value = percentage_of_complex_words
sheet['I82'].value = fog_index
sheet['J82'].value = average_number_of_words_per_sentence
sheet['K82'].value = complex_word_count
sheet['L82'].value = word_count
sheet['M82'].value = syllable_count
sheet['N82'].value = pronouns_count
sheet['O82'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0082.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A83'].value = "blackassign0082"
sheet['B83'].hyperlink = 'https://insights.blackcoffer.com/online-gaming-adolescent-online-gaming-effects-demotivated-depression-musculoskeletal-and-psychosomatic-symptoms/'
sheet['C83'].value = positive_score
sheet['D83'].value = negative_score
sheet['E83'].value = polarity
sheet['F83'].value = subjective_score
sheet['G83'].value = average_sentence_length
sheet['H83'].value = percentage_of_complex_words
sheet['I83'].value = fog_index
sheet['J83'].value = average_number_of_words_per_sentence
sheet['K83'].value = complex_word_count
sheet['L83'].value = word_count
sheet['M83'].value = syllable_count
sheet['N83'].value = pronouns_count
sheet['O83'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0083.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A84'].value = "blackassign0083"
sheet['B84'].hyperlink = 'https://insights.blackcoffer.com/human-rights-outlook/'
sheet['C84'].value = positive_score
sheet['D84'].value = negative_score
sheet['E84'].value = polarity
sheet['F84'].value = subjective_score
sheet['G84'].value = average_sentence_length
sheet['H84'].value = percentage_of_complex_words
sheet['I84'].value = fog_index
sheet['J84'].value = average_number_of_words_per_sentence
sheet['K84'].value = complex_word_count
sheet['L84'].value = word_count
sheet['M84'].value = syllable_count
sheet['N84'].value = pronouns_count
sheet['O84'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0084.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A85'].value = "blackassign0084"
sheet['B85'].hyperlink = 'https://insights.blackcoffer.com/how-voice-search-makes-your-business-a-successful-business/'
sheet['C85'].value = positive_score
sheet['D85'].value = negative_score
sheet['E85'].value = polarity
sheet['F85'].value = subjective_score
sheet['G85'].value = average_sentence_length
sheet['H85'].value = percentage_of_complex_words
sheet['I85'].value = fog_index
sheet['J85'].value = average_number_of_words_per_sentence
sheet['K85'].value = complex_word_count
sheet['L85'].value = word_count
sheet['M85'].value = syllable_count
sheet['N85'].value = pronouns_count
sheet['O85'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0085.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A86'].value = "blackassign0085"
sheet['B86'].hyperlink = 'https://insights.blackcoffer.com/how-the-covid-19-crisis-is-redefining-jobs-and-services/'
sheet['C86'].value = positive_score
sheet['D86'].value = negative_score
sheet['E86'].value = polarity
sheet['F86'].value = subjective_score
sheet['G86'].value = average_sentence_length
sheet['H86'].value = percentage_of_complex_words
sheet['I86'].value = fog_index
sheet['J86'].value = average_number_of_words_per_sentence
sheet['K86'].value = complex_word_count
sheet['L86'].value = word_count
sheet['M86'].value = syllable_count
sheet['N86'].value = pronouns_count
sheet['O86'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0086.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A87'].value = "blackassign0086"
sheet['B87'].hyperlink = 'https://insights.blackcoffer.com/how-to-increase-social-media-engagement-for-marketers/'
sheet['C87'].value = positive_score
sheet['D87'].value = negative_score
sheet['E87'].value = polarity
sheet['F87'].value = subjective_score
sheet['G87'].value = average_sentence_length
sheet['H87'].value = percentage_of_complex_words
sheet['I87'].value = fog_index
sheet['J87'].value = average_number_of_words_per_sentence
sheet['K87'].value = complex_word_count
sheet['L87'].value = word_count
sheet['M87'].value = syllable_count
sheet['N87'].value = pronouns_count
sheet['O87'].value = average_word_length

workbook.save("Output Data Structure.xlsx")




#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0087.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A88'].value = "blackassign0087"
sheet['B88'].hyperlink = 'https://insights.blackcoffer.com/impacts-of-covid-19-on-streets-sides-food-stalls/'
sheet['C88'].value = positive_score
sheet['D88'].value = negative_score
sheet['E88'].value = polarity
sheet['F88'].value = subjective_score
sheet['G88'].value = average_sentence_length
sheet['H88'].value = percentage_of_complex_words
sheet['I88'].value = fog_index
sheet['J88'].value = average_number_of_words_per_sentence
sheet['K88'].value = complex_word_count
sheet['L88'].value = word_count
sheet['M88'].value = syllable_count
sheet['N88'].value = pronouns_count
sheet['O88'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0088.txt", "r",  encoding="utf-8") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A89'].value = "blackassign0088"
sheet['B89'].hyperlink = 'https://insights.blackcoffer.com/coronavirus-impact-on-energy-markets-2/'
sheet['C89'].value = positive_score
sheet['D89'].value = negative_score
sheet['E89'].value = polarity
sheet['F89'].value = subjective_score
sheet['G89'].value = average_sentence_length
sheet['H89'].value = percentage_of_complex_words
sheet['I89'].value = fog_index
sheet['J89'].value = average_number_of_words_per_sentence
sheet['K89'].value = complex_word_count
sheet['L89'].value = word_count
sheet['M89'].value = syllable_count
sheet['N89'].value = pronouns_count
sheet['O89'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0089.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A90'].value = "blackassign0089"
sheet['B90'].hyperlink = 'https://insights.blackcoffer.com/coronavirus-impact-on-the-hospitality-industry-5/'
sheet['C90'].value = positive_score
sheet['D90'].value = negative_score
sheet['E90'].value = polarity
sheet['F90'].value = subjective_score
sheet['G90'].value = average_sentence_length
sheet['H90'].value = percentage_of_complex_words
sheet['I90'].value = fog_index
sheet['J90'].value = average_number_of_words_per_sentence
sheet['K90'].value = complex_word_count
sheet['L90'].value = word_count
sheet['M90'].value = syllable_count
sheet['N90'].value = pronouns_count
sheet['O90'].value = average_word_length

workbook.save("Output Data Structure.xlsx")


#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0090.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A91'].value = "blackassign0090"
sheet['B91'].hyperlink = 'https://insights.blackcoffer.com/lessons-from-the-past-some-key-learnings-relevant-to-the-coronavirus-crisis-4/'
sheet['C91'].value = positive_score
sheet['D91'].value = negative_score
sheet['E91'].value = polarity
sheet['F91'].value = subjective_score
sheet['G91'].value = average_sentence_length
sheet['H91'].value = percentage_of_complex_words
sheet['I91'].value = fog_index
sheet['J91'].value = average_number_of_words_per_sentence
sheet['K91'].value = complex_word_count
sheet['L91'].value = word_count
sheet['M91'].value = syllable_count
sheet['N91'].value = pronouns_count
sheet['O91'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0091.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A92'].value = "blackassign0091"
sheet['B92'].hyperlink = 'https://insights.blackcoffer.com/estimating-the-impact-of-covid-19-on-the-world-of-work-2/'
sheet['C92'].value = positive_score
sheet['D92'].value = negative_score
sheet['E92'].value = polarity
sheet['F92'].value = subjective_score
sheet['G92'].value = average_sentence_length
sheet['H92'].value = percentage_of_complex_words
sheet['I92'].value = fog_index
sheet['J92'].value = average_number_of_words_per_sentence
sheet['K92'].value = complex_word_count
sheet['L92'].value = word_count
sheet['M92'].value = syllable_count
sheet['N92'].value = pronouns_count
sheet['O92'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0092.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A93'].value = "blackassign0092"
sheet['B93'].hyperlink = 'https://insights.blackcoffer.com/estimating-the-impact-of-covid-19-on-the-world-of-work-3/'
sheet['C93'].value = positive_score
sheet['D93'].value = negative_score
sheet['E93'].value = polarity
sheet['F93'].value = subjective_score
sheet['G93'].value = average_sentence_length
sheet['H93'].value = percentage_of_complex_words
sheet['I93'].value = fog_index
sheet['J93'].value = average_number_of_words_per_sentence
sheet['K93'].value = complex_word_count
sheet['L93'].value = word_count
sheet['M93'].value = syllable_count
sheet['N93'].value = pronouns_count
sheet['O93'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0093.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A94'].value = "blackassign0093"
sheet['B94'].hyperlink = 'https://insights.blackcoffer.com/travel-and-tourism-outlook/'
sheet['C94'].value = positive_score
sheet['D94'].value = negative_score
sheet['E94'].value = polarity
sheet['F94'].value = subjective_score
sheet['G94'].value = average_sentence_length
sheet['H94'].value = percentage_of_complex_words
sheet['I94'].value = fog_index
sheet['J94'].value = average_number_of_words_per_sentence
sheet['K94'].value = complex_word_count
sheet['L94'].value = word_count
sheet['M94'].value = syllable_count
sheet['N94'].value = pronouns_count
sheet['O94'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0094.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A95'].value = "blackassign0094"
sheet['B95'].hyperlink = 'https://insights.blackcoffer.com/gaming-disorder-and-effects-of-gaming-on-health/'
sheet['C95'].value = positive_score
sheet['D95'].value = negative_score
sheet['E95'].value = polarity
sheet['F95'].value = subjective_score
sheet['G95'].value = average_sentence_length
sheet['H95'].value = percentage_of_complex_words
sheet['I95'].value = fog_index
sheet['J95'].value = average_number_of_words_per_sentence
sheet['K95'].value = complex_word_count
sheet['L95'].value = word_count
sheet['M95'].value = syllable_count
sheet['N95'].value = pronouns_count
sheet['O95'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0095.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A96'].value = "blackassign0095"
sheet['B96'].hyperlink = 'https://insights.blackcoffer.com/what-is-the-repercussion-of-the-environment-due-to-the-covid-19-pandemic-situation/'
sheet['C96'].value = positive_score
sheet['D96'].value = negative_score
sheet['E96'].value = polarity
sheet['F96'].value = subjective_score
sheet['G96'].value = average_sentence_length
sheet['H96'].value = percentage_of_complex_words
sheet['I96'].value = fog_index
sheet['J96'].value = average_number_of_words_per_sentence
sheet['K96'].value = complex_word_count
sheet['L96'].value = word_count
sheet['M96'].value = syllable_count
sheet['N96'].value = pronouns_count
sheet['O96'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0096.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A97'].value = "blackassign0096"
sheet['B97'].hyperlink = 'https://insights.blackcoffer.com/what-is-the-repercussion-of-the-environment-due-to-the-covid-19-pandemic-situation-2/'
sheet['C97'].value = positive_score
sheet['D97'].value = negative_score
sheet['E97'].value = polarity
sheet['F97'].value = subjective_score
sheet['G97'].value = average_sentence_length
sheet['H97'].value = percentage_of_complex_words
sheet['I97'].value = fog_index
sheet['J97'].value = average_number_of_words_per_sentence
sheet['K97'].value = complex_word_count
sheet['L97'].value = word_count
sheet['M97'].value = syllable_count
sheet['N97'].value = pronouns_count
sheet['O97'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0097.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A98'].value = "blackassign0097"
sheet['B98'].hyperlink = 'https://insights.blackcoffer.com/impact-of-covid-19-pandemic-on-office-space-and-co-working-industries/'
sheet['C98'].value = positive_score
sheet['D98'].value = negative_score
sheet['E98'].value = polarity
sheet['F98'].value = subjective_score
sheet['G98'].value = average_sentence_length
sheet['H98'].value = percentage_of_complex_words
sheet['I98'].value = fog_index
sheet['J98'].value = average_number_of_words_per_sentence
sheet['K98'].value = complex_word_count
sheet['L98'].value = word_count
sheet['M98'].value = syllable_count
sheet['N98'].value = pronouns_count
sheet['O98'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0098.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A99'].value = "blackassign0098"
sheet['B99'].hyperlink = 'https://insights.blackcoffer.com/contribution-of-handicrafts-visual-arts-literature-in-the-indian-economy/'
sheet['C99'].value = positive_score
sheet['D99'].value = negative_score
sheet['E99'].value = polarity
sheet['F99'].value = subjective_score
sheet['G99'].value = average_sentence_length
sheet['H99'].value = percentage_of_complex_words
sheet['I99'].value = fog_index
sheet['J99'].value = average_number_of_words_per_sentence
sheet['K99'].value = complex_word_count
sheet['L99'].value = word_count
sheet['M99'].value = syllable_count
sheet['N99'].value = pronouns_count
sheet['O99'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0099.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A100'].value = "blackassign0099"
sheet['B100'].hyperlink = 'https://insights.blackcoffer.com/how-covid-19-is-impacting-payment-preferences/'
sheet['C100'].value = positive_score
sheet['D100'].value = negative_score
sheet['E100'].value = polarity
sheet['F100'].value = subjective_score
sheet['G100'].value = average_sentence_length
sheet['H100'].value = percentage_of_complex_words
sheet['I100'].value = fog_index
sheet['J100'].value = average_number_of_words_per_sentence
sheet['K100'].value = complex_word_count
sheet['L100'].value = word_count
sheet['M100'].value = syllable_count
sheet['N100'].value = pronouns_count
sheet['O100'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



#------------------Next - file-----------------


with open("StopWords_Auditor.txt", "r") as s:
    stop_words_1 = s.read()
    # print(stop_words_1)

with open("StopWords_Currencies.txt", "r") as t:
    stop_words_2 = t.read()
    # print(stop_words_2)

with open("StopWords_DatesandNumbers.txt", "r") as u:
    stop_words_3 = u.read()
    # print(stop_words_3)

with open("StopWords_Generic.txt", "r") as v:
    stop_words_4 = v.read()
    # print(stop_words_4)

with open("StopWords_GenericLong.txt", "r") as w:
    stop_words_5 = w.read()
    # print(stop_words_5)

with open("StopWords_Geographic.txt", "r") as x:
    stop_words_6 = x.read()
    # print(stop_words_6)

with open("StopWords_Names.txt", "r") as y:
    stop_words_7 = y.read()
    # print(stop_words_7)

with open("blackassign0100.txt", "r") as f:
    text = f.read()

with open("positive-words.txt", "r") as f:
    posit_text = f.read()

with open("negative-words.txt", "r") as f:
    negat_text = f.read()

from nltk.tokenize import word_tokenize

tokenize_words = word_tokenize(text)
positive_text = str(word_tokenize(posit_text))
negative_text = str(word_tokenize(negat_text))
# print(tokenize_words)
# print(positive_text)
# print(negative_text)

without_stop_words = []
for words in tokenize_words:
    if words not in stop_words_1:
        if words not in stop_words_2:
            if words not in stop_words_3:
                if words not in stop_words_4:
                    if words not in stop_words_5:
                        if words not in stop_words_6:
                            if words not in stop_words_7:
                                without_stop_words.append(words)

# print(without_stop_words)

Filtered_text = str(without_stop_words)

positive_score = 0

for word in Filtered_text:
    if word in positive_text:
        positive_score = positive_score + 1

# print(positive_score)

negative_score = 0

for word in Filtered_text:
    if word in negative_text:
        negative_score = negative_score - 1

negative_score = negative_score * -1
# print(negative_score)


blob = TextBlob(Filtered_text)
polarity = blob.sentiment.polarity
# print(polarity)


subjective_score = (positive_score + negative_score) / (len(Filtered_text) + 0.000001)
# print(subjective_score)

# average sentence length
average_sentence_length = textstat.avg_sentence_length(text)
# print(average_sentence_length)

# percentage of complex words
number_of_complex_words = textstat.difficult_words(text)
number_of_words = textstat.lexicon_count(text, removepunct=True)
percentage_of_complex_words = number_of_complex_words / number_of_words
# print(percentage_of_complex_words)


# fog index
fog_index = 0.4 * (average_sentence_length + percentage_of_complex_words)
# print(fog_index)

# average number of words per sentence
total_number_sentence = textstat.sentence_count(text)
average_number_of_words_per_sentence = number_of_words / total_number_sentence
# print(average_number_of_words_per_sentence)

# complex word count
complex_word_count = (textstat.polysyllabcount(text))

# word count
stop_words = set(stopwords.words('english'))

pure_text = []
for word in stop_words:
    if word not in text:
        pure_text.append(word)
pure = str(pure_text)

word_count = textstat.lexicon_count(pure, removepunct=True)
# print(word_count)

# syllable count
syllable_count = textstat.syllable_count(text)
# print(syllable_count)

# pronoun count

pronouns = []
pronoun1 = re.findall(r"\bWe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bwe\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bI\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bmy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bMy\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bOurs\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bours\b", text)
pronouns.append(pronoun1)

pronoun1 = re.findall(r"\bus\b", text)
pronouns.append(pronoun1)
main_pronouns = str(pronouns)
# print(main_pronouns)

pronouns_count = (textstat.lexicon_count(main_pronouns, removepunct=True))

# average word length

average_word_length = textstat.avg_character_per_word(text)
# print(average_word_length)


sheet['A101'].value = "blackassign0100"
sheet['B101'].hyperlink = 'https://insights.blackcoffer.com/how-will-covid-19-affect-the-world-of-work-2/'
sheet['C101'].value = positive_score
sheet['D101'].value = negative_score
sheet['E101'].value = polarity
sheet['F101'].value = subjective_score
sheet['G101'].value = average_sentence_length
sheet['H101'].value = percentage_of_complex_words
sheet['I101'].value = fog_index
sheet['J101'].value = average_number_of_words_per_sentence
sheet['K101'].value = complex_word_count
sheet['L101'].value = word_count
sheet['M101'].value = syllable_count
sheet['N101'].value = pronouns_count
sheet['O101'].value = average_word_length

workbook.save("Output Data Structure.xlsx")



sheet['A37'].value = "blackassign0036"
sheet['B37'].hyperlink = 'https://insights.blackcoffer.com/how-neural-networks-can-be-applied-in-various-areas-in-the-future/'
sheet['C37'].value = 'page not found'
sheet['D37'].value = 'page not found'
sheet['E37'].value = 'page not found'
sheet['E37'].value = 'page not found'
sheet['F37'].value = 'page not found'
sheet['G37'].value = 'page not found'
sheet['H37'].value = 'page not found'
sheet['I37'].value = 'page not found'
sheet['J37'].value = 'page not found'
sheet['K37'].value = 'page not found'
sheet['L37'].value = 'page not found'
sheet['M37'].value = 'page not found'
sheet['N37'].value = 'page not found'
sheet['O37'].value = 'page not found'

workbook.save("Output Data Structure.xlsx")


sheet['A50'].value = "blackassign0049"
sheet['B50'].hyperlink = 'https://insights.blackcoffer.com/how-neural-networks-can-be-applied-in-various-areas-in-the-future/'
sheet['C50'].value = 'page not found'
sheet['D50'].value = 'page not found'
sheet['E50'].value = 'page not found'
sheet['E50'].value = 'page not found'
sheet['F50'].value = 'page not found'
sheet['G50'].value = 'page not found'
sheet['H50'].value = 'page not found'
sheet['I50'].value = 'page not found'
sheet['J50'].value = 'page not found'
sheet['K50'].value = 'page not found'
sheet['L50'].value = 'page not found'
sheet['M50'].value = 'page not found'
sheet['N50'].value = 'page not found'
sheet['O50'].value = 'page not found'

workbook.save("Output Data Structure.xlsx")


