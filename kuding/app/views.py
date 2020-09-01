import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'app/index.html')

def pdf_view(request):
    if request.method == 'GET':
        return render(request, 'app/viewer.html')
    elif request.method == 'POST':
        text = {
                'title' : request.POST.get("search", None),
                'content' :request.POST.get("title", None) 
               }
        return render(request, 'app/viewer.html', text)
        #return render(request, 'app/index.html')

# def result(request):
# # #    search_key = request.GET['search_key'] 
# # #    context = {'search_key':search_key} 
# # #    return render(request,'result/result.html',context)
# #     if request.is_ajax():
# #         return render(request,'result/result.html')
# #     else:
# #         return render(request,'result/result.html')
#     pass
@csrf_exempt
def post_result(request):
    if request.method == 'POST':
        keyword = request.POST.get('search_key', None)

        keywords={'keyword': keyword}
        # return render(request, 'app/viewer.html', keyword)
        # return HttpResponse(keyword)
        return JsonResponse(keywords)
    else:
        message = "임시 데이터. 적절하게 수정할 필요가 있다."

        context = {'secret_key': message }
        return JsonResponse(context)
#def searchText(request):
#   if request.method == 'GET':
#        pass
#    elif request.method == 'POST':
               
