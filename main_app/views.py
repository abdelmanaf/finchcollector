from django.shortcuts import render

from django.http import request



def finches_index(request):
  return render(request, 'finches/index.html', {'finches': finches})

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')