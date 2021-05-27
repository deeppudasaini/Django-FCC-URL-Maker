from django.shortcuts import render

# Create your views here.
def HomePage(reques):
    return render(request,'index.html')