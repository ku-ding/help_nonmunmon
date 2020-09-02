import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from . import search
from django.contrib.auth.decorators import login_required
from elasticsearch import Elasticsearch
from datetime import datetime
import pprint


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
        title = request.POST.get('search_title', None)
        content = request.POST.get('search_content', None)
        
        data = search.searchDataContent(title,content)
        
        keywords =[]
        for i in range(0,4):
            keywords.append({
                   'title': data['hits']['hits'][i]['_source']['title'],
                   'content' : data['hits']['hits'][i]['_source']['content']
            })

            
       # pprint.pprint(keywords, indent=5)

        return JsonResponse(list(keywords), safe=False)
    # Fail to POST data
    else:
        message = "잘못된 접근입니다."
        context = {'secret_key': message }
        return JsonResponse(context)

#searching data from HTML
@csrf_exempt
def post_data(request):
    if request.method == 'POST':
        title = request.POST.get('title_data', None)
        content = request.POST.get('content_data', None)

    #return HttpResponse(data)              
