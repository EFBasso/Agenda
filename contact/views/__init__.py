# flake8: noqa
from .contact_views import *
from .contact_forms import *

"""
Estes arquivos são importados aqui para "enganar" o django como 
a views pois estando no __init__.py é priorizado seu uso.

Observe que ao importar tudo que existe em dois módulos é muito importante
verificar se não há dois nomes iguais que possam colidir !!!
"""