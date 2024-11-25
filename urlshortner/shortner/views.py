from django.shortcuts import render,redirect
import uuid
from .models import Url
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request,'index.html')
    
def create(request):
    if request.method == "POST":
        sent = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=sent,uuid=uid)
        new_url.save()
        return HttpResponse(uid)
        # return render(request,'index.html',{'data':uid})

    
def go(request,pk):
    url_details = Url.objects.get(uuid=pk)
    if url_details:
        return redirect('https://'+url_details.link)
    else:
        HttpResponse('Not Found !')