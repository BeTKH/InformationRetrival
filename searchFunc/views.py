from django.shortcuts import render, get_object_or_404
from django.contrib.postgres.search import SearchVector
from .models import Document

# Create your views here.


def search(request):
    query = request.GET.get('q')
    if query:
        results = Document.objects.annotate(search=SearchVector(
            'content')).filter(search=query).order_by('-search')
    else:
        results = Document.objects.none()

    return render(request, 'search/search_results.html', {'results': results, 'query': query})


def results(request):

    # gets all movie objects in the DB i.e. SELECT * FROM DOCUMENTS WHERE title = 'Atomic Habits';
    # Document.objects.filter(title='Atomic habits')

    # gets all document objects in the DB i.e. SELECT * FROM DOCUMENTS;
    Documents = Document.objects.all()

    # get a list of titles
    # Titles = ', '.join([d.title for d in Documents])

    # retrun the titles
    # return HttpResponse(Titles)
    return render(request, 'search/results.html', {'Documents': Documents})


def getDocument(request, doc_id):

    # docID = Document.objects.get(pk=doc_id)

    # better way: returns 404 if content not found
    docID = get_object_or_404(Document, pk=doc_id)
    return render(request, 'search/docid.html', {'docID': docID})
