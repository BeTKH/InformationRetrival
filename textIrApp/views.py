from django.shortcuts import render, get_object_or_404
from tdm.models import Documents
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


from .customLibraries import cleanQuery, query_documents, orderByRelevance
from .createTDM import tdm, allTerms


@csrf_exempt
def getQueryText(requestIndex):

    if requestIndex.method == 'POST':

        requestDict = requestIndex.POST

        queryText = str(requestDict["userRequest"])

        queryText_clean = cleanQuery(queryText.split())

        print(queryText_clean)

        # execute the query

        documentScoreArray = query_documents(tdm, allTerms, queryText_clean)

        fileNames_score = orderByRelevance(documentScoreArray)

        print(fileNames_score)

        # get all document attributes from the database
        dbDocumentFilelds = Documents.objects.all

        # return queryText

        return render(requestIndex, 'tdmTempltes/index.html', {'fileNames_scores_': fileNames_score, 'dbDocumentFilelds_': dbDocumentFilelds})
        # return render(requestIndex, 'tdmTempltes/index.html')
    else:
        return render(requestIndex, 'tdmTempltes/index.html')


def getDocumentDetails_ir(requestDetails, pkkk):

    # 'docID' is a primary key field in the Documents
    # docID=pkkk will assign the primary key to the pkkk argument

    docDetails_ir = get_object_or_404(Documents, pk=pkkk)
    return render(requestDetails, 'tdmTempltes/documentDetails.html', {'docDetails_ir_': docDetails_ir})
