from django.shortcuts import render, get_object_or_404
from django.contrib.postgres.search import SearchVector
from .models import Document


"""
view functionas litrally create "what we are going to view/see" on the browser

each view function typically used to render a sigle html page, 
but it is also possible to render multiple pages in one view function
"""


def searchResults(request):

    # gets all document objects in the searchFunc i.e. SELECT * FROM DOCUMENTS;
    docResults = Document.objects.all()

    # Documents_ is used in results.html to render the contents
    return render(request, 'search/results.html', {'docResults_': docResults})


def getDocumentDetails(requestDetails, pkkk_):

    # better way: returns 404 if content not found
    # pk = pkkk_ assigns the primary key of the document to  pkkk_
    # pkkk_ is then used in the urlpatterns

    docDetail = get_object_or_404(Document, pk=pkkk_)

    # 'docDetail_' will be used in the document_details.html to render contents
    return render(requestDetails, 'search/document_details.html', {'docDetail_': docDetail})


def search(request):
    query = request.GET.get('q')
    if query:
        results = Document.objects.annotate(search=SearchVector(
            'content')).filter(search=query).order_by('-search')
    else:
        results = Document.objects.none()

    return render(request, 'search/search_results.html', {'results': results, 'query': query})
