
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def super_type_list(response):
    
    
    return Response('ok') 
