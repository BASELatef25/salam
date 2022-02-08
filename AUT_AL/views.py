from django.http import response
from django.shortcuts import redirect, render
from django.urls.resolvers import CheckURLMixin
from . models import *








#Admission************************
def Tuition (request):
    return render(request,'Tuition.html')
def Admission_Overview (request):
    return render(request,'Admission_Overview.html')
def Academic_Calendar (request):
    return render(request,'academemic_Calender.html')

def Apply2 (request):
    return render(request,'Apply_Now2.html')
def Apply3 (request):
    return render(request,'Apply_Now3.html')
def Apply4 (request):
    return render(request,'Apply_Now4.html')
def Apply (request):
    return render(request,'Apply_Now.html')
def Payment (request):
    return render(request,'Payment.html')






#why salam************************
def Overview (request):
    return render(request,'Overview.html')
def Our_campus (request):
    parameter=homeslids.objects.all()
    return render(request,'Our-campus.html',{'slid':parameter})
def staff (request):
    return render(request,'staff.html')
#accademoic************************
def our_programs (request):
    return render(request,'our_programs.html')
def supplementary_courses_and_activities (request):
    return render(request,'supplementary_courses_and_activities.html')
def Private_Tutoring (request):
    return render(request,'Private_Tutoring.html')
# Create your views here.
def Popular_tourism_places (request):
    return render(request,'Popular_tourism_places.html')

def contact_us (request):
    return render(request,'contact_us.html')
def Safty (request):
    return render(request,'Safty.html')
def Travel_and_Visas (request):
    return render(request,'Travel_and_Visas.html')
#home************************************
def home (request):
    return render(request,'Getting_Around_in_Aqaba.html')
def Recreation_an_Activities (request):
    return render(request,'Recreation_an_Activities.html')
def Health_and_Wellness (request):
    return render(request,'Health_and_Wellness.html')
def Getting_Around_in_Aqaba (request):
    parameter=homeslids.objects.all()
    news1=news.objects.all()
    context={'slid':parameter,'news':news1}
    return render(request,'AUT_AL.html',context)
def AUT_Intercultural_Program (request):
    add=AUTIP.objects.all()
    add2=Portfolio_Modals.objects.all()
    add3=why.objects.all()
    context={'adds':add,'Portfolio':add2,'data':add3}
    return render(request,'AUT_Intercultural_Program.html',context)
def About (request):
    img=images.objects.all()
    add2=Portfolio_Modals.objects.all()
    context={'images':img,'Portfolio':add2}
    return render(request,'About.html',context)

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
    parameter=AUTIP.objects.all()
    if request.method=='POST':
        Course = AUTIP.objects.create(
            title = request.POST["Title"],
            subtitle = request.POST["Subtitle"],
            text = request.POST["Text"],
        )
        Course.save()
    return render(request,'dSalamProgram.html',{'course':parameter})

def deletecourse (request,id):
    qdelete=AUTIP.objects.get(id=id)
    qdelete.delete()
    return redirect('/123/dashbord/dSalamProgram/')
