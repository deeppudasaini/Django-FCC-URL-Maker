from django.shortcuts import render, redirect
import uuid
from django.http import HttpResponse
from .models import URL
# Create your views here.
def HomePage(request):
    return render(request,'index.html')
def createLink(request):
    if request.method=='POST':
        link=request.POST['link']
        uid=str(uuid.uuid4())[:5]
        new_url=URL(link=link,uuid=uid)
        new_url.save()
        return  HttpResponse(uid)

def go(request, pk):
    url_details = URL.objects.get(uuid=pk)
    return redirect('https://'+ url_details.link)