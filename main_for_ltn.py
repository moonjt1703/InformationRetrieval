from search_engine import *
import string
from generateRunLTN_mainLTN import QueryProcessor

import operator


def main():

    path = 'OutPut/run_ltn_test.txt'
    runsFile = open(path, "w")

    queries = queryParser()
    corpus = parse_XMLFiles()
    proc = QueryProcessor(queries, corpus)
    print(proc)
    results = proc.run()

    for query in results:
        temp = dict(sorted(results[query].items(), key = lambda item: item[1], reverse = True))
        count = 0
        for doc_id in temp:
            #print(query.strip())
            #print(doc_id.strip())
            #print(temp[doc_id])
            runsFile.write("{} {} {} {} {} {} {} \n".format(query.strip(), "Q0", doc_id.strip(), count+1,temp[doc_id], "Mounia","/article[1]"))
            count += 1
            if count == 1500:
                break


if __name__ == '__main__':
    main()