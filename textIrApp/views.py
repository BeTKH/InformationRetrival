from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .customLibraries import cleanQuery


from .createTDM import tdm, allTerms
from .customLibraries import query_documents


@csrf_exempt
def getQueryText(requestIndex):

    requestDict = requestIndex.POST

    print(requestDict)

    # queryText = str(requestDict["userRequest"])

    # queryTexList = queryText.split()

    # queryText_clean = cleanQuery(queryTexList)

    # print(queryText)
    # print(queryText_clean)

    # # execute the query
    # queryResult = query_documents(tdm, allTerms, queryText_clean)

    # print(queryResult)
    # return queryText
    return render(requestIndex, 'tdmTempltes/index.html')


#  acceptUserQuery is triggered by the form action on the index.html


@csrf_exempt
def acceptUserQuery(request):
    # print(request.POST)
    # return render(request, 'tdmTempltes/submit.html')
    return HttpResponse("submitted")
