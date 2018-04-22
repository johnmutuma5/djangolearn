from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def index_json(request):
    msg = json.dumps({"msg": "Hello"})
    response = HttpResponse(msg)
    response['content-type'] = 'applciation/json'
    return response

def posts_index(request):
    ctx = {'title': 'Django Learning - A quick guide'}
    return render(request, 'posts/index.html', ctx)
