"""ecea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views, settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 
 


urlpatterns = [
	path('',views.home,name='home'),
	# path('experiences/',views.experience,name='experience'),
	path('placement_hardware/',views.phard,name='phard'),
	path('internship_hardware/',views.ihard,name='ihard'),
	path('placement_software/',views.psoft,name='psoft'),
	path('internship_software/',views.isoft,name='isoft'),
	path('calender/',views.calender,name='calender'),
	path('component/',views.component,name='component'),
	path('academics/',views.academics,name='academics'),
	path('preparation/',views.preparation,name='preparation'),
	path('event/',views.event,name='event'),
	path('gallery/',views.gallery,name='gallery'),
	path('alumni/',views.alumni,name='alumni'),
	path('project/',views.project,name='project'),
	path('team/',views.team,name='team'),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
