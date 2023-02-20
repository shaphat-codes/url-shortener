from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . serializers import *
from . models import *
from django.shortcuts import redirect


# Create your views here.


@api_view(['POST'])
def PostLink(request):
    if request.method == 'POST':
        serializer = ShortenerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



def redirect_view(request, encoded):
    url = Link.objects.get(encoded=encoded)
    
    response = redirect(f"{url.target_url}")
    return response