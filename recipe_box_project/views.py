"""
Purpose: Render HTML web pages
"""
from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    # return HttpResponse('home_view')
    return render(request, 'home_page.html')


def about_view(request):
    return HttpResponse('about_view')


