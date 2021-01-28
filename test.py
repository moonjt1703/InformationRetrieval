from xml.dom import minidom
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import re
import sim_functions

import glob

stemmer = PorterStemmer()
stopwords = set(stopwords.words("english"))


def doc_Preprocessing(values):
    myprocessedList = []
    wnl = WordNetLemmatizer()
    values = re.sub(r'\d+', '', values)
    values = values.lower()
    values = re.sub(r"\n", " ", values)
    values = values.lower()
    translator = str.maketrans('', '', string.punctuation)
    values=values.translate(translator)
    tokensList = word_tokenize(values)
    for token in tokensList:
        foo = wnl.lemmatize(token)
        foo = stemmer.stem(token)
        if foo not in stopwords:
            myprocessedList.append(foo)
   #print(myprocessedList)
    return myprocessedList


filenames = glob.glob('./Data/XML_file/Samples for test/*.xml')

processed_value = []
my_dict = dict()
def xmlparser():
    for filename in filenames:

        mydoc = minidom.parse (filename)
        items = mydoc.getElementsByTagName ('link')
        ids = mydoc.getElementsByTagName ('id')
        for elem in items:
            if elem.firstChild:
                values = elem.firstChild.data
                processed_value = doc_Preprocessing (values)
                for value in processed_value:
                    key = ids [0].firstChild.data
                    # print(values)
                    # print(key)
                    if key not in my_dict:
                        my_dict [key] = []
                    my_dict [key].append (value)


    return my_dict
print(xmlparser())


def queryParser():
    with open ('Data/queries.txt') as f:
        queries = []
        lines = ''.join (f.readlines ())
        queries = [x.rstrip ().split () for x in lines.split ('\n') [:-1]]

    return queries
        # my_dict[int(ids[1].firstChild.data)] = values

#print(my_dict.values())
#print(my_dict.keys())print(sim_functions.tfidf(my_dict.values()))

# print(ids[1].firstChild.data)
# print(items.length)
# list.append(ids[1].firstChild.data)
# print(ids[1].firstChild.data)


"""ValuesList.append(elem.firstChild.data)
list.append(elem.firstChild.data)"""
# print(elem.firstChild.data)

# text="I LOVE life live living is beautiful beauty \n lover \t you are my lover  "
# text=my_dict.items()

# doc_Preprocessing(text)
