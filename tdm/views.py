from django.shortcuts import render, get_object_or_404

from .models import Document


# views functions
def queryResults(requestDocs):

    # get all documents in the tdm
    documents = Document.objects.all

    # render(request, template_name, context=None, content_type=None, status=None, using=None)
    # context is dictionary of values to add to the template
    # the key of the context ('tdmDocs_') is used in the template

    return render(requestDocs, 'tdmTempltes/filesInDB.html', {'documents_': documents})


def getDocumentDetails_tdm(requestDetails, pkkk):

    # 'docID' is a primary key field in the Documents
    # docID=pkkk will assign the primary key to the pkkk argument

    docDetails_tdm = get_object_or_404(Document, pk=pkkk)
    return render(requestDetails, 'tdmTempltes/documentDetails.html', {'docDetails_tdm_': docDetails_tdm})
