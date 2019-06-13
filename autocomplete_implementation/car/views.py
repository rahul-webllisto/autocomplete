from django.shortcuts import render, HttpResponse

from .models import Car
# Create your views here.
import json

def home(request):
    return render(request,'home.html')




def autocompleteModel(request):    
    search_qs = Car.objects.filter(name__startswith=request.GET['term'])
    results = []
    for r in search_qs:
        results.append(r.name)               
    data = json.dumps(results)
    return HttpResponse(data, content_type='application/json')
