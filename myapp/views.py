from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def counter(request):
    words = request.GET['words']
    total_words = len(words.split())
    return render(request, 'counter.html', {'total':total_words})