
class RunsOutput:
    def __init__(self, results,groupe="Mounia", step="05",numero_run="01", function="bm25", article="article"):
        self.results=results
        self.groupe=groupe
        self.step=step
        self.numero_run=numero_run
        self.function=function
        self.article=article
        self.initiateRun()


    def initiateRun(self,path='OutPut/RunsOutPut.txt'):

        runsFile = open(path, "w")
        for query in self.results:
            temp = dict(sorted(self.results[query].items(), key=lambda item: item[1], reverse=True))
            count = 0
            for doc_id in temp:
                runsFile.write("{} {} {} {} {} {} {} \n ".format(query.strip(), "Q0", doc_id.strip(), temp[doc_id], self.groupe, "/article[1]"))
                count += 1
                if count == 1500:
                    break


