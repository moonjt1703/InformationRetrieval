from xml.dom import minidom
import xml.etree.ElementTree as ET
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import re
import glob
import sim_functions

# Starting The preprocessing

stemmer = PorterStemmer ()
stopwords = set (stopwords.words ("english"))


def doc_Preprocessing(values):
    myprocessedList = []
    wnl = WordNetLemmatizer ()
    for value in values:
        value = re.sub (r'\d+', '', value)
        value = value.lower ()
        value = re.sub (r"\n", " ", value)
        value = value.lower ()
        translator = str.maketrans ('', '', string.punctuation)
        value = value.translate (translator)
        tokensList = word_tokenize (value)
        for token in tokensList:
            foo = wnl.lemmatize (token)
            foo = stemmer.stem (foo)
            if foo not in stopwords:
                myprocessedList.append (foo)
    return myprocessedList


# Parsing TextFiles

# list =[]
my_texts_dictionnary = dict ()


def parse_XMLFiles():
    filenames = glob.glob ('./Data/XML_file/coll/*.xml')
    my_xmldict = dict ()
    for filename in filenames:
        values = []
        processed_value = []
        mydoc = minidom.parse (filename)
        items = mydoc.getElementsByTagName ('bdy')
        ids = mydoc.getElementsByTagName ('id')
        for elem in items:
            for elem in elem.childNodes:
                if elem.nodeType==elem.TEXT_NODE:
                    values.append (elem.nodeValue)
                    processed_value.append (doc_Preprocessing (values))
        if processed_value != []:
            for value in processed_value:
                key = ids [0].firstChild.data
                if value != []:
                    my_xmldict.update ({key: value})
    print (my_xmldict)
    return my_xmldict


print (parse_XMLFiles ())


def queryParser():
    with open ('Data/queries.txt') as f:
        queries = []
        lines = ''.join (f.readlines ())
        queries = [x.rstrip ().split () for x in lines.split ('\n') [:-1]]

    return queries
