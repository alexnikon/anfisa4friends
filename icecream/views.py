from django.http import HttpResponse
from .models import icecream_db


def icecream_list(request):
    icecreams = ''
    
    return HttpResponse(f'Cписок сортов мороженого: {icecreams}')
 