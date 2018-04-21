from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def index(request):
    msg = json.dumps({"msg": "Hello"})
    response = HttpResponse(msg)
    response['content-type'] = 'applciation/json'
    return response
