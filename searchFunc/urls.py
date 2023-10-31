from django.urls import path
from . import views


"""
create objects that map url end points to view functions 
( this mapping is called url configuration)
"""

app_name = 'search'

urlpatterns = [

    path('', views.results, name='results'),
    path('', views.search, name='search'),
    path('<int:doc_id>', views.getDocument, name='detail')

]
