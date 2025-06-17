from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'message' : 'Home Page'}
    return render(request, 'index.html', context)