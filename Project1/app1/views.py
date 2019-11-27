from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json

def showHuman(request):
    d1 = {
        "idno":101,
        "name":"Ravi",
        "salary":185000.00
    }
    # sending HTML as HttpResponse
    return render(request,"index.html",d1)

def showApp(request):
    d1 = {
        "idno": 101,
        "name": "Ravi",
        "salary": 185000.00
    }
    # converting dict to json
    json_data = json.dumps(d1)
    # sending json as HttpResponse
    return HttpResponse(json_data,content_type="application/json")


def showJsonApp(request):
    d1 = {
        "idno": 101,
        "name": "Ravi",
        "salary": 185000.00,
        "status" : True,
        "contactno":9052492329
    }
    # sending json as JsonResponse
    return JsonResponse(d1)