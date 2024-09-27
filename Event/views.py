from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def Hello(req):
    return HttpResponse("Hello 5TWIN2")