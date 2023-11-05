from django.urls import path
from . import views

"""
map url end points to view functions ( aka url configuration)

give the mapping a name
"""

appName = 'tdm'

urlpatterns = [
    path('', views.queryResults, name='queryResult'),
    path('<int:pkkk>', views.getDocumentDetails_tdm, name='documentDetails_'),
]
