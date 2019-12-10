from django.shortcuts import render
from django.http import HttpResponse
import requests
import bs4

# Create your views here.
def home(request):
    # return HttpResponse('Hello,World')
    # names=['Dixya','Jyoti']

    # d={
    #     'name':names,
    #     'college':'St.Xaviers'
    # }

   
    page=requests.get('https://fabpedigree.com/james/mathmen.htm')
    soup=bs4.BeautifulSoup(page.content,'html.parser')
    nm=[]
    for names in soup.findAll('a'):
        if names.parent.name==('li'):
            nm.append(names.text)
    
    d={
        'names':nm
    }
    return render(request,'home.html',context=d)
    
def bootcamp(request):
    return HttpResponse('<h1>Hello Bootcamp</h1>')