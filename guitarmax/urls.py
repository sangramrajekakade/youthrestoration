"""guitarmax URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from guitar import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^videos/$', views.VideosPage.as_view(), name='videos'),
   
    url(r'^transplant-details/$', views.transplantdetails.as_view(), name='transplant-details'),
    url(r'^guitar-details/(?P<pk>[\w-]+)$', views.Detail_Guitar.as_view(), name='guitar-details'),

    url(r'^admission/$', views.Admission.as_view(), name='admission'),
    url(r'^batches/$', views.BatchesPage.as_view(), name='batches'),
    url(r'^Appointment/$', views.Appointment.as_view(), name='Appointment'),
    url(r'^about-us/$', views.AboutPage.as_view(), name='about-us'),
    url(r'^fees/$', views.feestructurePage.as_view(), name='fees'),

    url(r'^buy-guitar/$', views.BuyguitarPage.as_view(), name='buy-guitar'),
    url(r'^buy-guitar-details/(?P<pk>[\w-]+)$', views.Buyguitar_details.as_view(), name='buy-guitar-details'),


    url(r'^blog/$', views.PostPage.as_view(), name='blog'),
    url(r'^blogview/(?P<pk>[\w-]+)$', views.Post_details.as_view(), name='blogview'),
    url(r'^email/$', views.email_tamplate.as_view(), name='email'),
    url(r'^Services/$', views.Services.as_view(), name='Services'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




admin.site.site_header = "Youth Restoration"
# admin.site.site_title = "2"
# admin.site.index_title = "3"
admin.site.site_url = "4"