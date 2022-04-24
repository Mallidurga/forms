from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import *

def insert_topic(request):
    if request.method=='POST':
        #print(request.POST)
        #TN=request.POST['topic']
        TN=request.POST.get('topic')
        print(TN)
        T=Topic.objects.get_or_create(topic_name=TN)[0]
        T.save()
        return HttpResponse('Topic data is insert successfully')
    return render(request,'insert_topic.html')

def insert_webpage(request):
    if request.method=='POST':
        #print(request.POST)
        #TN=request.POST['topic']
        w=request.POST.get('webpage')
        print(w)
        T=Topic.objects.get_or_create(topic_name=T)[0]
        T.save()
        WN=request.POST['name']
        WU=request.POST['url']
        w=insert_webpage.objects.get_or_create(topic_name=w,name=WN,url=WU)[0]
        w.save()
        return HttpResponse('Webpage data is insert successfully')
    return render(request,'insert_webpage.html')
