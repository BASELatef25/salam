from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from AUT_AL.views import *
from AUT_AL import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',home),
    url(r'^about/$',About),
    url(r'^Popular_tourism_places/$',Popular_tourism_places),
    url(r'^Salam_Program/$',AUT_Intercultural_Program),
    url(r'^apply/$',Apply),
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

