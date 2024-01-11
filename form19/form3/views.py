from django.shortcuts import render
from django.http import HttpResponse
# create an http response on html code
def home(request):
    return render(request, 'index.html')  # request is the data that

