from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from AUT_AL.views import *
from AUT_AL import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',home),
    url(r'^about/$',About),







    
    #Admission************************
    url(r'^apply/$',Apply),
    url(r'^apply2/$',Apply2),
    url(r'^apply3/$',Apply3),
    url(r'^apply4/$',Apply4),
    url(r'^Academic_Calendar/$',Academic_Calendar),
    url(r'^Admission_Overview/$',Admission_Overview),
    url(r'^Tuition/$',Tuition),
    url(r'^Payment/$',Payment),














    #why salam******************
    url(r'^Overview/$',Overview),
    url(r'^Our-campus/$',Our_campus),
    url(r'^staff/$',staff),













    #Academic******************
    url(r'^our_programs/$',AUT_Intercultural_Program),
    url(r'^supplementary_courses_and_activities/$',supplementary_courses_and_activities),
    url(r'^Private_Tutoring/$',Private_Tutoring),









    #*********************
    url(r'^Safty/$',Safty),
    url(r'^Travel_and_Visas/$',Travel_and_Visas),
    url(r'^Getting_Around_in_Aqaba/$',Getting_Around_in_Aqaba),
    url(r'^Recreation_an_Activities/$',Recreation_an_Activities),
    url(r'^Health_and_Wellness/$',Health_and_Wellness),
    url(r'^contact_us/$',contact_us),
    url(r'^Popular_tourism_places/$',Popular_tourism_places),
    url(r'^Salam_Program/$',AUT_Intercultural_Program),
    url(r'^blog/$',Blog),
    url(r'^whySalam_Program/$',whyautip),
    url(r'^123/dashbord/$',dashbord),
    url(r'^123/$',dashbord_login),
    url(r'^news/$',newsv),
    url(r'^academic/$',academic),
    url(r'^123/dashbord/dview_orders/$',dvieworders),
    url(r'^123/dashbord/dhome/$',dhome),
    url(r'^123/dashbord/dSalamProgram/$',dSalamProgram),
    url(r'^delete/(?P<id>\d+)/$', deleteslid , name="delete_slide"),
    url(r'^delete/(?P<id>\d+)/$', deletecourse , name="delete_course"),
    #url(r'^delete/(?P<pk>\d+)/$', 'note.views.NoteDelete.as_view()', name="delete_note"),


]

