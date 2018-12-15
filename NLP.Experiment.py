# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 08:54:57 2018

@author: dibyendu.baksi
"""

import nltk
from nltk import tokenize
#from nltk.corpus import PlaintextCorpusReader

"""
corp = PlaintextCorpusReader(r'.','Corpus.txt', encoding='latin-1')
text = nltk.Text(corp.words())
"""
 
#READ THE PAPER FROM A TEXT FILE
file = open('Corpus.txt', 'r')
f = file.read()

#p = "Good morning Dr. Adams. The patient is waiting for you in room number 3."
#Sentences extracted in 'sentences' array of strings and 
#a particular 'sentence' is printed
sentences = tokenize.sent_tokenize(f)
sentence = sentences[8]
print(sentence)
#'sentence' TOKENIZEd
text = nltk.Text(nltk.word_tokenize(sentence))
#'sentence' POS TAGGED
text_pos = nltk.pos_tag(text)

match = text.concordance('prevalence')
#DEFINE TAG PATTERNS
grammar = "NP: {<DT>?<JJ>*<NN>}"

#INSTANTIATE PARSER
cp = nltk.RegexpParser(grammar)

#PARSE 
result = cp.parse(text_pos)

#PRINT AND DISPLAY PARSE TREE
print(result)
result.draw()
"""
sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"), ("dog", "NN"), ("barked", "VBD"), ("at", "IN"), ("the", "DT"), ("cat", "NN")]
grammar = "NP: {<DT>?<JJ>*<NN>}"
cp=nltk.RegexpParser(grammar)
res = cp.parse(sentence)
print(res)
res.draw()
"""
