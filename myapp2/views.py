from django.shortcuts import render

# Create your views here.
def future(request):
    return render(request, 'myapp2/home.html')

def a(request):
    return render(request, 'myapp2/a.html')