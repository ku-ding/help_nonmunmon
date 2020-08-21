from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'app/index.html')

def pdf_view(request):
    if request.method == 'GET':
        return render(request, 'app/viewer.html')
    elif request.method == 'POST':
        text = request.POST.get("search", None)
        return HttpResponse(text)
        #return render(request, 'app/index.html')

#def searchText(request):
#   if request.method == 'GET':
#        pass
#    elif request.method == 'POST':
        
        
