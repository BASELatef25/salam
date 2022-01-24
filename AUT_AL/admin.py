from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from .models import *
# Register your models here.
admin.site.register(AUTIP),
admin.site.register(blog),
admin.site.register(why),
admin.site.register(homeslids),
admin.site.register(news),
admin.site.register(faculty_members),
admin.site.register(images),
admin.site.register(Portfolio_Modals),