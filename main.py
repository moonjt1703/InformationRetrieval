from QueryRunner import QueryProcessor
from search_engine import *
import string
#from generateRunLTN_mainLTN import QueryProcessor
#from SearchEngineForElements import *
import operator


def main():

    path = 'OutPut/run_bm_article.txt'
    runsFile = open(path, "w")

    queries = queryParser()
    corpus = parse_XMLFiles()
    #print(parse_XMLFiles())
    proc = QueryProcessor(queries, corpus)
    #print(proc)
    results = proc.run()
    print(results)

    for query in results:
        temp = dict(sorted(results[query].items(), key = lambda item: item[1], reverse = True))
        count = 0
        for doc_id in temp:
            runsFile.write("{} {} {} {} {} {} {} \n".format(query.strip(), "Q0", doc_id.strip(), count+1,temp[doc_id], "Mounia","/article[0]"))
            count += 1
            if count == 1500:
                break


if __name__ == '__main__':
    main()