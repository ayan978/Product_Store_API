import json
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Product
from products.serializers import ProductSerializer
from django.http import HttpResponse

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    # instance = Product.objects.all().order_by('?').first()
    # data = {}
    # if instance:
    #     data =  ProductSerializer(instance).data

    # return Response(data)

    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid():
        data = serializer.data

    return Response(data)



