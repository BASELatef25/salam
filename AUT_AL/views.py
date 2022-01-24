from django.http import response
from django.shortcuts import redirect, render
from django.urls.resolvers import CheckURLMixin
from . models import *
# Create your views here.
def home (request):
    parameter=homeslids.objects.all()
    news1=news.objects.all()
    context={'slid':parameter,'news':news1}
    return render(request,'AUT_AL.html',context)
def AUT_Intercultural_Program (request):
    add=AUTIP.objects.all()
    add2=Portfolio_Modals.objects.all()
    context={'adds':add,'Portfolio':add2}
    return render(request,'AUT_Intercultural_Program.html',context)
def About (request):
    img=images.objects.all()
    add2=Portfolio_Modals.objects.all()
    context={'images':img,'Portfolio':add2}
    return render(request,'About.html',context)
def Apply (request):
    if request.method=='POST':
        Regist = Registration.objects.create(
            fname = request.POST["fname"],
            lname = request.POST["lname"],
            email = request.POST["email"],
            phoneno = request.POST["phoneno"],
            pirthday = request.POST["pirthday"],
            address = request.POST["address"],
            level = request.POST["level"],
        )
        Regist.save()
    return render(request,'Apply_Now.html')
def Blog (request):
    bloges=blog.objects.all()
    return render(request,'bloges.html',{'blogs':bloges})
def newsv (request):
    x=news.objects.all()
    return render(request,'news.html',{'news':x})
def blogshowe (request):
    bloges=blog.objects.all()
    return render(request,'blogshowe.html',{'blogs':bloges})
def whyautip (request):
    why1=why.objects.all()
    return render(request,'whyautip.html',{'data':why1})
def academic (request):
    teacher = faculty_members.objects.all()

    return render(request,'academic.html',{'parameter2':teacher})

def dashbord_login (request):
    
    if request.method =='POST':
        a = 'abc',
        b = 'abc',
        z = request.POST["user"],
        x = request.POST["password"],
        if (a == z) and (b == x):
            request.session['check'] = 0
            response = redirect('/123/dashbord')
            return response
                
        
    return render(request,'dashbord_login.html')


def dashbord (request):
    if request.session['check'] == 0:
        return render(request,'dashbord.html')
    else:
        response = redirect('/123')
        return response

#dashbord
def dvieworders (request):
    if request.session['check'] == 0:
        orders=Registration.objects.all()
        return render(request,'dview_orders.html',{'data1':orders})
    else:
        response = redirect('/123')
        return response

def dhome (request):
    parameter=homeslids.objects.all()
    if request.method=='POST':
        slid = homeslids.objects.create(
            title = request.POST["title"],
            pragrapg = request.POST["text"],
            link = request.POST["link"],
            image = request.FILES["image"],
        )
        slid.save()
    return render(request,'dhome.html',{'slid':parameter})

def deleteslid (request,id):
    vdelete=homeslids.objects.get(id=id)
    vdelete.delete()
    return redirect('/123/dashbord/dhome/')

#dSalamProgram

def dSalamProgram (request):
    if request.method=='POST':
        Course = AUTIP.objects.create(
            title = request.POST["Title"],
            subtitle = request.POST["Subtitle"],
            text = request.POST["Text"],
        )
        Course.save()
    return render(request,'dSalamProgram.html')