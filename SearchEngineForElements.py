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
    values = values.translate(translator)
    tokensList = word_tokenize(values)
    for token in tokensList:
        foo = wnl.lemmatize(token)
        foo = stemmer.stem(foo)
        if foo not in stopwords:
            myprocessedList.append(foo)
    # print(myprocessedList)
    return myprocessedList


# Parsing TextFiles

# list =[]
my_texts_dictionnary = dict()


def parse_TextFiles():
    with open('Data/Text_file/Text_Only_Ascii_Coll_MWI_NoSem', encoding="utf8") as file:
        my_upgraded_textfile = ET.fromstringlist(["<documents>", str(file.read()), "</documents>"])
        for i in range(len(my_upgraded_textfile)):
            my_texts_dictionnary[int(my_upgraded_textfile[i][0].text)] = doc_Preprocessing(
                my_upgraded_textfile[i][0].tail)
            # print(my_texts_dictionnary.items())
            return my_texts_dictionnary.items()


# print(parse_TextFiles())


def parse_XMLFiles():
    filenames = glob.glob('./Data/XML_file/coll/*.xml')
    my_xmldict = dict()
    for filename in filenames:

        mydoc = minidom.parse(filename)
        items = mydoc.getElementsByTagName('link')
        ids = mydoc.getElementsByTagName('id')
        for elem in items:
            if elem.firstChild.data:
                values = elem.firstChild.data
                processed_value = doc_Preprocessing(values)
                for value in processed_value:
                    key = ids[0].firstChild.data
                    if key not in my_xmldict:
                        my_xmldict[key] = []
                    my_xmldict[key].append(value)
        print(my_xmldict)

    return my_xmldict


print(parse_XMLFiles())


def queryParser():
    with open('Data/queries.txt') as f:
        queries = []
        lines = ''.join(f.readlines())
        queries = [x.rstrip().split() for x in lines.split('\n')[:-1]]

    return queries


#if __name__ == '__main__':
   # print(queryParser())

"""
dictionarry = dict()


def get_doc(doc_id):
    dictionarry.get(doc_id)


def get_dict_size(dictionarry):
    return len(dictionarry)"""
