from django.contrib import admin
from django.urls import path
from home import views

# Django admin customizations

admin.site.site_header = "Developer Udoy"
admin.site.site_title = "Welcome to Udoy's Dashboard"
admin.site.index_title = "Welcome to this Portal"

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('project', views.project, name='project'),
    path('contact', views.contact, name='contact')
]
