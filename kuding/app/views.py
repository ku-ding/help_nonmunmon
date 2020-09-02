import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from . import search
from django.contrib.auth.decorators import login_required

# main window
def index(request):
    return render(request, 'app/index.html')

# nonmun page
@login_required #only to success login
def pdf_view(request):
    if request.method == 'GET':
        id ={'id':request.user}
        print(id['id'])
        return render(request, 'app/viewer.html',id)
        
    elif request.method == 'POST':
        text = {
                'title' : request.POST.get("search", None),
                'content' :request.POST.get("title", None) 
               }
        return render(request, 'app/viewer.html', text)

#searched data to HTML
@csrf_exempt
def post_result(request):
    # success  to POST data
    if request.method == 'POST':
        keyword = request.POST.get('search_key', None)
        keywords={'keyword': keyword}
        print(keywords['keyword'])
        return JsonResponse(keywords)
    # Fail to POST data
    else:
        message = "잘못된 접근입니다."
        context = {'secret_key': message }
        return JsonResponse(context)

#searching data from HTML
@csrf_exempt
def post_data(request):
    if request.method == 'POST':
        data = request.POST.get('title_data', None)
    return HttpResponse(data)              
