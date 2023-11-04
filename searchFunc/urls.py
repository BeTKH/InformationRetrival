from django.urls import path
from . import views


"""
urls.py maps url end points to view functions ( aka url configuration)

the mapping is done using path() function

path() takes:

    - route ( e.g. '')
    - mapping to the function ( e.g. 'views.searchResults')
    - name 

"""

app_name = 'search'

urlpatterns = [

    path('', views.searchResults, name='results'),
    path('', views.search, name='search'),
    path('<int:pkkk_>', views.getDocumentDetails, name='detail')

]

"""
pkkk_ : 

- an argument in a view function getDocumentDetails(requestDetails, pkkk_):

- takes: requestDetails & pkk_
- returns: 



"""
