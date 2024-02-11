from django.shortcuts import render

# Create your views here.
def Pune(request):
    return render(request,'pune.html')
def Noida(request):
    return render(request,'noida.html')
