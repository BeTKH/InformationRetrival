from django.shortcuts import render, get_list_or_404
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

        return render(requestIndex, 'tdmTempltes/queryResults_top.html', {'fileNames_score_': fileNames_score, 'dbDocumentFilelds_': dbDocumentFilelds})
        # return render(requestIndex, 'tdmTempltes/index.html')
    else:
        return render(requestIndex, 'tdmTempltes/index.html')
