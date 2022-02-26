from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    context = {}
    bookList = Book.objects.all()
    context['bookList'] = bookList
    print(bookList)
    return render(request, 'book/index.html', context)

