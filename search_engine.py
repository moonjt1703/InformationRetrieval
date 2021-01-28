from xml.dom import minidom
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import re
import glob


# Starting The preprocessing

stemmer = PorterStemmer()
stopwords = set(stopwords.words("english"))


def doc_Preprocessing(values):
    myprocessedList = []
    wnl = WordNetLemmatizer()
    values = re.sub(r'\d+', '', values)
    values = values.lower()
    values = re.sub(r"\n", " ", values)
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
#my_texts_dictionnary = dict()

"""
def parse_TextFiles():
    with open('Data/Text_file/Text_Only_Ascii_Coll_MWI_NoSem', encoding="utf8") as file:
        my_upgraded_textfile = ET.fromstringlist(["<documents>", str(file.read()), "</documents>"])
        for i in range(len(my_upgraded_textfile)):
            my_texts_dictionnary[int(my_upgraded_textfile[i][0].text)] = doc_Preprocessing(
                my_upgraded_textfile[i][0].tail)
            # print(my_texts_dictionnary.items())
            return my_texts_dictionnary.items()


# print(parse_TextFiles())

"""

def getText(nodelist):
    rc = []

    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.nodeValue)

    return ''.join(rc)

def handleTok(tokenlist):
    texts = ""
    for token in tokenlist:

        texts += " "+getText(token.childNodes)
        #texts += " " + getText (token.childNodes)


    return texts


def parse_XMLFiles():
    filenames = glob.glob('./Data/XML_file/coll/*.xml')
    my_xmldict = {}
    for filename in filenames:
        values=[]
        mydoc = minidom.parse(filename)
        article = mydoc.getElementsByTagName('link')
        ids = mydoc.getElementsByTagName('id')
        texts = handleTok(article)
        processedText = doc_Preprocessing(texts)
        if processedText !=[] :
            #for text in processedText:
            # values.append(text)
            values.extend(processedText)
            if values !=[] :
                key = ids [0].firstChild.data
                my_xmldict.update ({key: values})


        print(my_xmldict)


    return my_xmldict


#print(parse_XMLFiles())

def queryParser():
    with open('Data/queries.txt') as f:
        lines = ''.join(f.readlines())
        queries = [x.rstrip().split() for x in lines.split('\n')[:-1]]

    return queries

"""
if __name__ == '__main__':
    print(queryParser())
"""

dictionarry = dict()


def get_doc(doc_id):
    dictionarry.get(doc_id)


def get_dict_size(dic):
    return len(dic)
