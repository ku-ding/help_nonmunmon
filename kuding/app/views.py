from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')

def pdf_view(request):
    return render(request, 'app/viewer.html')
