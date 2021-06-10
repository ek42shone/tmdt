import json

from django.contrib.auth.models import User
from django.core import serializers
from django.http import JsonResponse

# Create your views here.
from staff.models import Product


def index(request):
    if request.method == 'GET':
        data=User.objects.all()
        test1 = serializers.serialize("json", data)
    return JsonResponse({"test":test1}, content_type="application/json",status=200);

def getProduct(request):
    if request.method=='GET':
        data=serializers.serialize("json",Product.objects.all())
    return JsonResponse({"test": data}, content_type="application/json", status=200);