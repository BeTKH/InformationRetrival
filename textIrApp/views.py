from django.shortcuts import render, get_object_or_404
from tdm.models import Document
from django.views.decorators.csrf import csrf_exempt


from .customLibraries import clean_Text, query_documents, orderByRelevance
from .createTDM import tdm, allTerms, tdm_tf, tdm_tfidf


@csrf_exempt
def getQueryText(requestIndex):

    if requestIndex.method == 'POST':

        requestDict = requestIndex.POST
        queryText = str(requestDict["userRequest"])

        print(queryText)

        # execute the query with tdm
        # documentScoreArray = query_documents(tdm, allTerms, queryText, idf_=False)

        # execute the query with tdm_tfidf
        documentScoreArray = query_documents(
            tdm, allTerms, queryText, idf_=True)

        fileNames_score = orderByRelevance(documentScoreArray)

        print(fileNames_score)

        # get all document attributes from the database
        dbDocumentFilelds = Document.objects.all

        return render(requestIndex, 'tdmTempltes/index.html', {'fileNames_scores_': fileNames_score,
                                                               'dbDocumentFilelds_': dbDocumentFilelds})
        # return render(requestIndex, 'tdmTempltes/index.html')
    else:
        return render(requestIndex, 'tdmTempltes/index.html')


def getDocumentDetails_ir(requestDetails, pkkk):

    # 'docID' is a primary key field in the Documents
    # docID=pkkk will assign the primary key to the pkkk argument

    docDetails_ir = get_object_or_404(Document, pk=pkkk)
    return render(requestDetails, 'tdmTempltes/documentDetails.html', {'docDetails_ir_': docDetails_ir})
