from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


from .customLibraries import cleanQuery, query_documents
from .createTDM import tdm, allTerms


@csrf_exempt
def getQueryText(requestIndex):

    if requestIndex.method == 'POST':

        requestDict = requestIndex.POST

        queryText = str(requestDict["userRequest"])

        queryText_clean = cleanQuery(queryText.split())

        print(queryText_clean)

        # execute the query
        queryResult = query_documents(tdm, allTerms, queryText_clean)

        print(queryResult)
        # return queryText

        return HttpResponse("Received a POST request")

    else:
        return render(requestIndex, 'tdmTempltes/index.html')
