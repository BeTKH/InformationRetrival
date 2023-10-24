from django.shortcuts import render
from .models import Document, TFIDF
from django.db.models import F


def search(request):
    if 'q' in request.GET:
        query = request.GET['q']
        results = Document.objects.filter(tfidf__term=query).annotate(
            relevance_score=F('tfidf__tfidf_score')
        ).order_by('-relevance_score')

        return render(request, 'search_results.html', {'results': results, 'query': query})
    return render(request, 'search.html')
