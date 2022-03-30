from django.shortcuts import render


# Create your views here.

def index(request):
    x = {'name':'ali', 'age':25}
    return render(request, 'templates/pages/index.html', x)