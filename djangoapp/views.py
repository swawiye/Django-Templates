from django.shortcuts import render

# Create your views here.
def home(request):
    #context = {'message' : 'Home Page'}
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')