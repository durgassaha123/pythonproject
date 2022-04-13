from django.shortcuts import render, redirect
from .models import passwords,mydetails,myservices,myskills,mylanguage,myknowledge,social,myproject,myfriend,mymusic,myicons,countrys,state,continents,currentacy,language
from django.http import HttpResponse, JsonResponse
import urllib3
from sys import stdout
from urllib.request import urlopen
import re
import requests
from bs4 import BeautifulSoup
import os
import json
import webbrowser
import datetime
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets,permissions,generics
from .serializers import PasswordsSerializer,MydetailsSerializer,MyservicesSerializer,MyskillSerializer,MylanguageSerializer,MyknowledgeSerializer,SocialSerializer,MyprojectSerializer,MyfriendSerializer,MymusicSerializer,MyiconsSerializer
from . import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
import random
import array

sociallink = [
    {
        "title": "",
        "name": "Portfolio",
        "category": "website",
        "active": "active",
        "desc": "The term “portfolio” refers to any combination of financial assets such as stocks, bonds and cash. Portfolios may be held by individual investors or managed by financial professionals, hedge funds, banks and other financial institutions."
    },
    {
        "title": "password",
        "name": "Password Generator",
        "category": "software",
        "active": "",
        "desc": "Strong Password Generator to create secure passwords that are impossible to crack on your device without sending them across the Internet, and learn over 40 tricks to keep your passwords, accounts and documents safe."
    },
    {
        "title": "converter",
        "name": "Unit Converter",
        "category": "software",
        "active": "",
        "desc": "A unit is a measurement of a quantity that is defined or adopted by tradition or law. Other quantities can be expressed as a multiple of the unit."
    },
    {
        "title": "contact_form_btn",
        "name": "Contact Form",
        "category": "project",
        "active": "",
        "desc": "A page on a website that allows users to communicate with the site owner. The page has fields for filling in name, address and type of comment."
    },
    {
        "title": "CV",
        "name": "Resume / CV",
        "category": "software",
        "active": "",
        "desc": "A resume, sometimes spelled resume, called a CV in English outside North America, is a document created and used by a person to present their background, skills, and accomplishments. Résumés can be used for a variety of reasons, but most often they are used to secure new employment."
    },
    {
        "title": "GallerySlider",
        "name": "Gallery Slider",
        "category": "project",
        "active": "",
        "desc": "They rotate on an axis where the image is always facing you. A gallery is usually where all images are available to see... but that doesn't mean a slider or carousel can't show all the images either."
    }
]

Copyright = {'name':'TheKoushikDurgas' , 'link':'http://thekoushikdurgas.in/' , 'year':datetime.datetime.now().strftime("%Y")}

navlink = [
    {'active': "active",'title': "Dashboard",'icon': "far fa-gauge fa-fw",'link': "/", 'collapse':False},
    {'active': "",'title': "Lists",'icon': "fas fa-list-check fa-fw",'link': "javascript:void(0)", 'collapse':True,
    'collapselink':[
        {'active': "",'title': "Password",'icon': "fad fa-key fa-fw",'link': "/passwordlist"},
    ]},
    {'active': "",'title': "Projects",'icon': "fal fa-laptop-code fa-fw",'link': "javascript:void(0)", 'collapse':True,
    'collapselink':[
        {'active': "",'title': "Password Generator",'icon': "fad fa-key fa-fw",'link': "/passwordgenerator"},
        {'active': "",'title': "CSV Edit & Display",'icon': "fad fa-key fa-fw",'link': "/csv"},
    ]},
]

# def insertdata(request):
#         for i in sociallink:
#             cl=myproject(title=i['title'],name=i['name'],category=i['category'],desc=i['desc'])
#             cl.save()
#         return HttpResponse("<h1>Inserted</h1>")
    
class PasswordViewSet(generics.ListCreateAPIView):
    queryset = passwords.objects.all()
    serializer_class = PasswordsSerializer

class MydetailsViewSet(generics.ListCreateAPIView):
    queryset = mydetails.objects.all()
    serializer_class = MydetailsSerializer

class MyservicesViewSet(generics.ListCreateAPIView):
    queryset = myservices.objects.all()
    serializer_class = MyservicesSerializer

class MyskillViewSet(generics.ListCreateAPIView):
    queryset = myskills.objects.all()
    serializer_class = MyskillSerializer

class MylanguageViewSet(generics.ListCreateAPIView):
    queryset = mylanguage.objects.all()
    serializer_class = MylanguageSerializer

class MyknowledgeViewSet(generics.ListCreateAPIView):
    queryset = myknowledge.objects.all()
    serializer_class = MyknowledgeSerializer

class SocialViewSet(generics.ListCreateAPIView):
    queryset = social.objects.all()
    serializer_class = SocialSerializer

class MusicViewSet(generics.ListCreateAPIView):
    queryset = mymusic.objects.all()
    serializer_class = MymusicSerializer

class MyprojectViewSet(generics.ListCreateAPIView):
    queryset = myproject.objects.all()
    serializer_class = MyprojectSerializer
    def get_queryset(self):
        id = self.request.query_params.get('id')
        if(id == None):
            queryset = myproject.objects.all()
        else:
            queryset = myproject.objects.filter(id=id)
        return queryset

class MyfriendViewSet(generics.ListCreateAPIView):
    queryset = myfriend.objects.all()
    serializer_class = MyfriendSerializer

class MyiconsViewSet(generics.ListCreateAPIView):
    queryset = myicons.objects.all()
    serializer_class = MyiconsSerializer

class countrysViewSet(generics.ListCreateAPIView):
    queryset = countrys.objects.all()
    serializer_class = serializers.countrysSerializer

class StateViewSet(generics.ListCreateAPIView):
    queryset = state.objects.all()
    serializer_class = serializers.StateSerializer
    def get_queryset(self):
        country = self.request.query_params.get('country')
        if(country == None):
            queryset = state.objects.all()
        else:
            queryset = state.objects.filter(countrys=country)
        return queryset

class continentsViewSet(generics.ListCreateAPIView):
    queryset = continents.objects.all()
    serializer_class = serializers.continentsSerializer

class CurrentacyViewSet(generics.ListCreateAPIView):
    queryset = currentacy.objects.all()
    serializer_class = serializers.CurrentacySerializer

class LanguageViewSet(generics.ListCreateAPIView):
    queryset = language.objects.all()
    serializer_class = serializers.LanguageSerializer
    
# @api_view([..])
# @permission_classes((permissions.AllowAny,))    
class passwordjson(APIView):
    def get(self, request):
        passwordlist = {}
        for i in range(6,128):
            passwordlist[i] = strongpassword(i)
        passwordlist[256] = strongpassword(256)
        passwordlist[512] = strongpassword(512)
        passwordlist[1024] = strongpassword(1024)
        passwordlist[2048] = strongpassword(2048)
        return JsonResponse(passwordlist, safe = False)

# @permission_classes((permissions.AllowAny,))     
class custompassword(APIView):
    def get(self, request,lenght):
        return JsonResponse({lenght: strongpassword(lenght)}, safe = False)

def strongpassword(MAX_LEN):
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
    SYMBOLS = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '}', '{', '[', ']', '=', '<', '>', '/', ',', '.']
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
    passl = random.choice(DIGITS) + random.choice(UPCASE_CHARACTERS) + random.choice(LOCASE_CHARACTERS) + random.choice(SYMBOLS)
    for x in range(MAX_LEN):
        passl = passl + random.choice(COMBINED_LIST)
        passlist = array.array('u', passl)
        random.shuffle(passlist)
    return "".join(passlist)[:MAX_LEN]

def navbarclear(a):
    for i in a:
        i['active'] = ""
        if(i['collapse']):
            for j in i['collapselink']:
                j['active'] = ""  
                
def clearactive(d):
    durgas1['id'] +=1
    navbarclear(navlink)
    if(len(d) == 1):
        durgas1['title'] = durgas1['pagetitle'] = navlink[d[0]]['title']
        durgas1['title1'] = ""
        navlink[d[0]]['active'] = 'mm-active active-no-child'
    else:
        durgas1['title'] = navlink[d[0]]['title']
        durgas1['title1'] = durgas1['pagetitle'] = navlink[d[0]]['collapselink'][d[1]]['title']
        navlink[d[0]]['active'] = 'mm-active'
        navlink[d[0]]['collapselink'][d[1]]['active'] = 'mm-active'
    
# def home(request):
#     clearactive([0])
#     return render(request, 'Main/index.html', {'durgas1': durgas1})
    
def passwordlist(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        link = request.POST.get('link')
        username = request.POST.get('username')
        subject =  request.POST.get('subject')
        password = request.POST.get('autopasswordgenatorinput')
        passwordcu = passwords(email = email, link = link, username = username, subject = subject, password = password)
        passwordcu.save()
    clearactive([1,0])
    durgas1['requirements']['password'] = passwords.objects.all()
    return render(request, 'Main/passwordlist.html', {'durgas1': durgas1})
    
def passwordgenerator(request):
    clearactive([2,0])
    return render(request, 'Main/passwordgenerator.html', {'durgas1': durgas1})

# def csv(request):
#     clearactive([2,1])
#     return render(request, 'Main/csv.html', {'durgas1': durgas1})

durgas1 = {
    'id': 0,
    'name': "Koushik",
    'picname': "title.jpg",
    'title': "",
    'title1': "",
    'pagetitle': "",
    'title2': False,
    'gearbox': ['one', 'two', 'three'],
    'sunlight': range(12),
    'sociallink': sociallink,
    'navlink': navlink,
    'error': "",
    'Copyright': Copyright,
    'requirements': {}
}