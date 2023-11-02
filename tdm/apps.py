from django.apps import AppConfig


"""
add complete path to this class in textITApp/settings.py 
under 'Application definition' list


INSTALLED_APPS = [ ..., 'searchFunc.apps.SearchfuncConfig','tdm.apps.TdmConfig']

"""


class TdmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tdm'
