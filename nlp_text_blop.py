# -*- coding: utf-8 -*-
"""nlp text blop.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jB8U20I1T7cMszZaLwPR5SQqZ1MdplPc
"""

from textblob import TextBlob

def convert (string):
  li = list(string.split())
  return li

str1= input("Enter your word : ")
words=convert(str1)
corrected_words = []

for i in words :
  corrected_words.append(TextBlob(i))
  
print ("wrong words : ", words )
print("corrected words are : ")

for i in corrected_words :
  print(i.correct(), end=" ")

!pip install gingerit
!pip install streamlit

from gingerit.gingerit import GingerIt
import streamlit as st

st.title('Grammar & spell checker in Python')
text = st.text_area("Enter Text:", value='', height=None, max_chars=None)
parser = GingerIt()

if st.button('Correct statement'):
    if text == '':
        st.write('Please enter text for checking')
    else:
        result_dict = parser.parse(text)
        st.markdown('Corrected statement - ' + str(result_dict["result"]))
else:pass

!pip install streamlit

!pip install pyspellchecker

from spellchecker import SpellChecker
     

spell = SpellChecker()
     

misspelled = spell.unknown(['Welcomo', 'to', 'AI', 'Sciences'])
     

all_words = ['Welcomo', 'to', 'AI', 'Sciences']
     


     
{'welcomo'}

for word in misspelled:
  print(spell.candidates(word))
     
{'welcome'}

while True:
  word = input("Enter the word:")
  if word in spell:
    print("'{} is spelled  correctly".format(word))
  else:
    correct_word=spell.correction(word)